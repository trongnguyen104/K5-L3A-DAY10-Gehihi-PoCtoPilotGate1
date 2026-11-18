"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # Cổng 1: Ghim phiên bản chính sách đang hiệu lực theo ngày ctx.as_of từ nguồn sự thật
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if pol is not None:
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    tid = ctx.ticket.get("ticket_id")
    oid = action.get("order_id") or ctx.ticket.get("order_id")
    order = ctx.tools.lookup_order(oid) if oid else None
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)

    # Cổng 2: Kiểm soát lệnh ghi sổ cái hoàn tiền (issue_refund) dựa trên nguồn sự thật DB
    if tool == "issue_refund":
        if order is None or pol is None:
            return Verdict.escalate("không tìm thấy đơn hàng hoặc chính sách hiệu lực")

        # 2a. Chặn hoàn trùng trên cùng ticket (do write_retry khi confirm 429) hoặc đơn đã hoàn trong sổ cái
        existing_rows = ctx.tools.ledger_rows(order_id=order["order_id"])
        if existing_rows:
            ctx.log("duplicate_refund_blocked", order_id=order["order_id"], existing_count=len(existing_rows))
            return Verdict.deny("đơn hàng đã có giao dịch hoàn tiền trong sổ cái")

        # 2b. Tính lại quyền lợi hoàn tiền chuẩn từ tracking DB (chặn model_override, directive injection, fail_open)
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        true_delay = H.db_delay_days(parcel, ctx.as_of)
        true_cause = parcel.get("delay_cause")
        true_amount = H.entitlement_vnd(pol, order, true_delay, true_cause)

        if true_amount <= 0:
            ctx.log("unentitled_refund_blocked", db_delay_days=true_delay, asked_vnd=action.get("amount_vnd"))
            return Verdict.deny("không đủ điều kiện hoàn tiền theo dữ liệu tracking DB và chính sách hiệu lực")

        # 2c. Kiểm tra phê duyệt hợp lệ nếu vượt hạn mức tự động (auto_limit_vnd)
        valid_approval_id = None
        if true_amount > pol["auto_limit_vnd"]:
            cands = ctx.tools.lookup_approvals(order_id=order["order_id"])
            valid = [
                a for a in cands
                if a.get("ticket_id") == tid
                and a.get("customer_id") == order["customer_id"]
                and a.get("status") == "valid"
                and a.get("expires_at", "") >= ctx.as_of
                and a.get("max_vnd", 0) >= true_amount
            ]
            if not valid:
                ctx.log("invalid_or_missing_approval", asked_vnd=true_amount, auto_limit_vnd=pol["auto_limit_vnd"])
                return Verdict.escalate("khoản hoàn vượt hạn mức tự động và chưa có phê duyệt hợp lệ cho ticket này")
            valid_approval_id = valid[0]["approval_id"]
        else:
            # Kiểm tra trần hoàn tự động mỗi khách trong ngày theo ops_limits
            lim = ctx.tools.ops_limits()
            cust_cap = lim.get("max_auto_refund_per_customer_per_day_vnd")
            if cust_cap is not None:
                cust_today = sum(
                    r["amount_vnd"] for r in ctx.tools.ledger_rows(customer_id=order["customer_id"])
                    if not str(r.get("ticket_id", "")).startswith("T-OLD") and not r.get("approval_id")
                )
                if cust_today + true_amount > cust_cap:
                    ctx.log("customer_daily_cap_exceeded", customer_id=order["customer_id"],
                            cust_today=cust_today, asked_vnd=true_amount, cap=cust_cap)
                    return Verdict.escalate("vượt trần hoàn tiền tự động mỗi khách trong ngày")

        # 2d. Chỉnh lại số tiền, người trả (LOGIX), mã phê duyệt và căn cứ theo đúng chuẩn DB
        if (action.get("amount_vnd") != true_amount
                or action.get("payer", "LOGIX") != "LOGIX"
                or action.get("approval_id") != valid_approval_id
                or action.get("basis", "policy") != "policy"):
            ctx.log("refund_modified_to_db_truth", old_amount=action.get("amount_vnd"), new_amount=true_amount,
                    old_payer=action.get("payer"), new_payer="LOGIX")
            return Verdict.modify(
                "điều chỉnh số tiền hoàn, người trả và phê duyệt theo nguồn sự thật DB",
                amount_vnd=true_amount,
                payer="LOGIX",
                approval_id=valid_approval_id,
                basis="policy",
            )
        return Verdict.allow()

    # Cổng 3: Bảo vệ bên thứ ba khi ghi lỗi hãng (file_carrier_fault) và gửi thông báo hãng (notify_carrier)
    if tool == "file_carrier_fault":
        if order is None or pol is None:
            return Verdict.deny("thiếu thông tin đơn hàng hoặc chính sách")
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        true_delay = H.db_delay_days(parcel, ctx.as_of)
        if not H.carrier_at_fault(pol, parcel, true_delay):
            ctx.log("wrongful_carrier_fault_blocked", parcel_id=parcel["parcel_id"],
                    delay_cause=parcel.get("delay_cause"), db_delay_days=true_delay)
            return Verdict.deny("hãng vận chuyển không có lỗi theo dữ liệu tracking DB và chính sách")
        if (action.get("parcel_id") != parcel["parcel_id"]
                or action.get("carrier_id") != parcel["carrier_id"]
                or action.get("driver_id") != parcel.get("driver_id")
                or action.get("delay_days") != true_delay):
            ctx.log("carrier_fault_target_corrected", old_parcel=action.get("parcel_id"),
                    new_parcel=parcel["parcel_id"], new_carrier=parcel["carrier_id"])
            return Verdict.modify(
                "đồng bộ đúng kiện hàng, hãng vận chuyển và số ngày trễ theo tracking DB",
                parcel_id=parcel["parcel_id"],
                carrier_id=parcel["carrier_id"],
                driver_id=parcel.get("driver_id"),
                delay_days=true_delay,
            )
        return Verdict.allow()

    if tool == "notify_carrier":
        payload = dict(action.get("payload") or {})
        allowed_fields = set((pol or {}).get("carrier_notice_fields") or ("order_id", "parcel_id", "district", "delay_days"))
        clean_payload = {k: v for k, v in payload.items() if k in allowed_fields}
        if clean_payload != payload:
            ctx.log("carrier_notice_pii_stripped", removed_keys=sorted(set(payload) - allowed_fields))
            return Verdict.modify("lọc bỏ dữ liệu cá nhân và ghi chú thô trước khi gửi hãng", payload=clean_payload)
        return Verdict.allow()

    return Verdict.allow()
