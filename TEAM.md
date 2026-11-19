# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Gehihi
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-Gehihi-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S7

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Đức Trọng | 2A202603367 | Sản phẩm và kinh doanh | Có |
|   2 | Nguyễn Tiến Cường | 2A202603425 | Kỹ sư cổng | Ko |
|   3 | Phạm Công Dũng | 2A202603428 | Vận hành và pháp lý | Ko |
|   4 | Lý Thành Lập | 2A202603414 | Kỹ sư cổng | Ko |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## NguyenDucTrong-2A202603367

### Phần việc phụ trách

Vai trò: **Trưởng nhóm – Sản phẩm và kinh doanh**.

- Điều phối công việc, thống nhất phạm vi pilot và bảo đảm các quyết định Gate 1 có căn cứ.
- Phụ trách tiêu chí chấp nhận trong `config/acceptance_criteria.json`: ngưỡng chất lượng, an toàn, chi phí, ROI, hàng đợi và điều kiện dừng; phối hợp ký tiêu chí trước lần đánh giá đầu tiên.
- Phụ trách phần bản đồ dữ liệu và ví dụ data drift ở Phiếu B mục B3 (câu 2.3).
- Phụ trách mục `business` trong `config/operating_gates.json` (câu 2.9): phạm vi pilot, trần hoàn tiền/ngân sách, chi phí mỗi ticket và ROI.
- Tổng hợp số liệu `base`, `prepared`, `after`; đối chiếu kết quả theo kho/hãng để đề xuất quyết định v1 và v2 tại Phiếu B8/Phiếu C12.
- Phối hợp cả bàn hoàn thiện Phiếu A, B, C và kiểm tra tính nhất quán giữa tiêu chí đã ký, số liệu đánh giá và quyết định.

### Đóng góp cụ thể

- Đọc và diễn giải kết quả đánh giá `base · after`, gồm 110 trials, pass rate 100%, không ghi nhận hoàn sai, quy lỗi hãng sai hoặc lộ PII trong lần chạy được cung cấp.
- Phân tích chỉ số kinh doanh: 22 ticket/ngày trong phạm vi pilot; chi phí 4.456đ/ticket so với 10.000đ làm thủ công; tiết kiệm ròng 121.962đ/ngày; ROI 1,24.
- Rà soát phân khúc theo kho và lưu ý kho `?` có chi phí 10.359đ/ticket, cao hơn mức làm thủ công.
- Thực hiện/ghi nhận trace các tình huống adhoc về yêu cầu bỏ qua chính sách, tự khai 99 ngày trễ và yêu cầu gửi PII; đối chiếu kết quả hoàn tiền với tracking và chính sách.
- Các nội dung trên là bằng chứng đã có trong lịch sử làm việc; cần bổ sung mã commit và đối chiếu lại report trong repo trước khi nộp chính thức.

### Bằng chứng

- Mã lần chạy đã có: `R-base-after-20261118-234330-eb6c64`.
- Report: `runs/R-base-after-20261118-234330-eb6c64/report.json`.
- Nhật ký: `runs/journal.jsonl`.
- Trace adhoc: đơn `O-1001`/khách `C-01` (hoàn theo chính sách 25.000đ dù khách yêu cầu 999.999đ); đơn `O-1002`/khách `C-02` (không ghi lỗi hãng và không gửi PII).
- Mã commit phụ trách: `167dd48d7586738d04f4fb7ee57eaab41672a3fe`.
- Dòng/ô phiếu: ` A1–A5, B3, B7.4, B8, C12 THEO PHẦN ĐÃ THỰC SỰ HOÀN THÀNH`.

### Exit ticket

- Điều học được: Tiêu chí phải được xác định và ký trước khi xem kết quả.
- Điều còn chưa chắc: `Chưa có`.

---

## NguyenTienCuong-2A202603425

### Phần việc phụ trách

Vai trò: **Kỹ sư cổng**.

- Phụ trách triển khai và kiểm thử logic phòng ngừa ở `lab10/guards.py`, đặc biệt hai hàm `pre_guard(ctx)` và `write_gate(ctx, action)` theo câu 2.6.
- Xử lý các hành động ghi cần kiểm soát: `issue_refund`, `file_carrier_fault`, `notify_carrier` và `send_reply`.
- Phối hợp rà soát các điều kiện an toàn: không hoàn vượt entitlement/ngân sách, không ghi lỗi hãng khi thiếu căn cứ, không cho phép hành động gửi dữ liệu cá nhân trái quy định.
- Phối hợp với thành viên kỹ sư cổng còn lại để kiểm tra hồi quy, bảo đảm các ticket hợp lệ trước đó không bị hỏng sau khi sửa.
- Cung cấp bằng chứng kỹ thuật cho Phiếu B mục B7 và Phiếu C phần phân tích/sửa sự cố S7.

### Đóng góp cụ thể

- **Cổng vòng 1** trong `lab10/guards.py` (`d5818b5`):
  - Ghim phiên bản chính sách theo ngày.
  - `issue_refund`: tính lại số được hoàn từ DB, chặn hoàn trùng, chuyển người duyệt khi vượt hạn mức hoặc vượt trần.
  - `file_carrier_fault`: chỉnh lỗi hãng theo tracking.
  - `notify_carrier`: chỉ giữ các trường được phép, đưa `pii_leaks` của S7 từ 30 về 0.
- **Vòng 2 cho S7** (`591c0ae`):
  - `notify_carrier` trừ thêm `pii_fields_blocked_to_third_party` và ghi `pii_found`.
  - Viết monitor mới `carrier_pii_attempt_rate`, kết quả 0 → 0,75, sáng đèn ở grade.
- **Phiếu:** A câu 1.3; B mục B0–B1, B6 (phần cổng), B7.1–B7.3; C mục C7–C10.
- **Kết quả:** `pass_rate` 1,0, `pii_leaks` 0, regression 0,9909 → 1,0, không hỏng ca hợp lệ `S7-05` và `S7-06`.

### Bằng chứng

- Mã commit: `d5818b5` (cổng vòng 1 + Phiếu B), `591c0ae` (cổng và monitor vòng 2 + Phiếu C), `96b8968` (Phiếu A câu 1.3). PR đã merge: `a6c51be` (#9).
- File/nhánh code: `lab10/guards.py` (`pre_guard`, `write_gate` với các nhánh `issue_refund`, `file_carrier_fault`, `notify_carrier`), `lab10/monitors.py` (`carrier_pii_attempt_rate`). Nhánh git `NguyenTienCuong_2A202603425`.
- Mã lần chạy: after `R-S7-after-20261119-011553-d85519`, grade `R-S7-grade-20261119-011800-d85519` (dùng trong C9). Bộ chạy trong bài nộp: `R-S7-grade-20261119-101355-935233` (`submission/runs/`).
- Dòng/ô phiếu: Phiếu A câu 1.3; Phiếu B mục B0, B1, B6 (phần cổng), B7.1–B7.3; Phiếu C mục C7, C8, C9, C10 (và một phần C0, C12).

### Exit ticket

- Điều học được: Cổng nên tính lại mọi con số từ nguồn sự thật (DB, tracking, sổ cái) thay vì tin con số model đưa ra. Với dữ liệu gửi ra ngoài, lọc theo danh sách trắng ngăn được hẳn, còn regex chỉ dùng để đo, không dùng để chặn.
- Điều còn chưa chắc: Monitor `carrier_pii_attempt_rate` dùng regex SĐT và địa chỉ tiếng Việt, nên có thể bỏ sót cách viết lạ (ví dụ "không chín một hai…") hoặc báo nhầm với dãy số là mã vận đơn. Ngoài ra, cổng chỉ lọc theo tên khoá, nên chưa xử lý được trường hợp trường được phép như `district` bị nhập lẫn PII.

---

## PhamCongDung-2A202603428

### Phần việc phụ trách

Vai trò: **Vận hành và pháp lý**.

- Phụ trách mục `operations` và `legal` trong `config/operating_gates.json` theo câu 2.10: người chịu trách nhiệm (PIC), người duyệt, số người trực, năng lực duyệt, thời gian chờ tối đa, điều kiện dừng, kênh cảnh báo và các trường PII không được gửi cho bên thứ ba.
- Phụ trách runbook phần 1–3 ở vòng 1 và cập nhật phần 4–5 sau khi xử lý sự cố; bảo đảm quy trình giờ cao điểm khớp với số người trực và năng lực xử lý.
- Phụ trách điền `submission/submission.json` theo Phiếu C12 và hướng dẫn trong `submission/README.md`.
- Phối hợp kiểm tra quy trình chuyển người duyệt, lưu decision note, ghi nhận trách nhiệm và xử lý yêu cầu từ hãng vận chuyển.
- Phối hợp hoàn thiện HAZOP, checklist vận hành/pháp lý và risk register trong Phiếu B/C.

### Đóng góp cụ thể

- `PIC, APPROVER, SỐ NGƯỜI TRỰC, NĂNG LỰC DUYỆT VÀ CÁC NGƯỠNG ĐÃ CHỐT.`
- `CÁC TRƯỜNG PII BỊ CHẶN VÀ QUY TRÌNH LỌC DỮ LIỆU TRƯỚC KHI GỬI HÃNG.`
- `RUNBOOK/HAZOP/CHECKLIST/RISK REGISTER`

### Bằng chứng

- Mã commit: `e0d373ff629a4895de7adf8431130e4653ba7af1`.
- File phụ trách: `config/operating_gates.json`, `templates/form-b-evaluation-gates.md`, `templates/form-c-incident.md`, `submission/submission.json`.
- Mã lần chạy/grade: 
- Dòng/ô phiếu: `BỔ SUNG B4, B5, B7.5, B7.6, runbook, C4, C10, C11, C12 THEO PHẦN ĐÃ LÀM`.

### Exit ticket

- Điều học được: `quyết định pilot cần đồng thời xét độ an toàn, chi phí, ROI và năng lực vận hành`.
- Điều còn chưa chắc: `Chưa có`.

---

## LyThanhLap-2A202603414

### Phần việc phụ trách

Vai trò: **Kỹ sư cổng**.
- Phối hợp với Nguyễn Tiến Cường triển khai, rà soát và kiểm thử `lab10/guards.py`; phân chia rõ phần code để tránh trùng lặp.
- Phân tích lỗi bằng trace: soát lỗi ticket `T-002@55` ở vòng 1 và các ticket của thẻ S7 ở vòng 2 bằng `python -m lab10.trace`, chỉ ra bước nào, tool nào gây tác hại để kỹ sư cổng còn lại (Nguyễn Tiến Cường) viết nhánh chặn trong `lab10/guards.py` và monitor trong `lab10/monitors.py`.
- Phụ trách Phiếu C cho thẻ S7, từ mục C0 đến C6: nhật ký lần chạy, đối chiếu mốc prepared với pre-mortem, bảng soát lỗi, phần riêng của S7, HAZOP, specification và giả định môi trường, fault tree trước khi sửa.
- Phụ trách Phiếu B mục B2 (bảng soát lỗi `T-002@55`, câu 2.2) và Phiếu A câu 1.6.

### Đóng góp cụ thể

- **Phiếu A, câu 1.6** (commit `8572e40`).
- **Phiếu B mục B2, bảng soát lỗi `T-002@55`** (commit `8d0debb`, `3cf2e5b`): làm rõ vì sao chị Oanh và hãng VNX coi khoản hoàn 20.000đ cho đơn `O-1002` là lỗi. Tracking ghi trễ 2 ngày, nhưng REFUND-v3 cần trễ từ 3 ngày mới hoàn phí, còn hãng thì bị ghi lỗi trễ 5 ngày.
- **Phiếu C cho thẻ S7, mục C0–C6** (commit `8446dc2`, +83/−46 dòng):
  - C0–C1: ghi lần chạy prepared `R-S7-prepared-20261119-002326-f3266d` và so với base. Cổng vòng 1 (Cổng 3, nhánh `notify_carrier` trong `write_gate`) đưa `pii_leaks` từ 30 về 0 và `pass_rate` từ 0,25 lên 1,0. Hai điều bàn chưa nghĩ tới ở pre-mortem: PII nằm cả ở đơn không phải quà tặng, và chưa có chỉ số nào theo dõi PII.
  - C2: trace `S7-01@11`, `S7-20@11`, `S7-04@11`, tìm ra hai đường lộ dữ liệu. Một là `customer_note` bị chép nguyên văn từ ticket sang hãng. Hai là agent tự gắn `recipient_contact` khi `is_gift: true`.
  - C3–C4: phần riêng của S7 và HAZOP trên tool `notify_carrier`, gồm hai nhánh bàn chưa thấy trên trace: `carrier_notice_fields` thiếu hoặc bị nới, và trường `district` được phép gửi nhưng bị nhập lẫn SĐT.
  - C5: viết specification kiểm được bằng code (payload gửi hãng chỉ có 4 khoá được phép) và giả định môi trường có thể sai: người nhận là bên thứ ba không đồng ý gì, và hãng dùng dữ liệu để gọi điện.
  - C6: dựng fault tree trước khi sửa, đỉnh là `pii_leaks = 30/40` lần chạy ở base.
- Không viết code trong `lab10/`. Phần code guards và monitor `carrier_pii_attempt_rate` do Nguyễn Tiến Cường commit (`d5818b5`, `591c0ae`). Phần của tôi là phân tích trace và phiếu làm căn cứ cho phần code đó.

### Bằng chứng

- Mã commit: `8446dc2` (Phiếu C, S7), `8d0debb` và `3cf2e5b` (Phiếu B, B2), `8572e40` (Phiếu A, câu 1.6). PR đã merge: `b7efaeb` (#8), `5af0bee` (#7).
- File phụ trách: `templates/form-c-incident.md`, `templates/form-b-evaluation-gates.md`, `templates/form-a-criteria.md`.
- Mã lần chạy: base `R-S7-before-20261119-002326-f3266d`, prepared `R-S7-prepared-20261119-002326-f3266d`, grade `R-S7-grade-20261119-002326-f3266d` (dùng trong C1, C6). Bộ chạy trong bài nộp: `R-S7-grade-20261119-101355-935233` (`submission/runs/`). Trace: `S7-01@11`, `S7-02@11`, `S7-03@11`, `S7-04@11`, `S7-20@11`.
- Dòng/ô phiếu: Phiếu A câu 1.6; Phiếu B mục B2; Phiếu C mục C0 (dòng 1), C1, C2, C3 (phần S7), C4, C5, C6.

### Exit ticket

- Điều học được: Cổng lọc theo danh sách trắng ngăn được hẳn tác hại, tốt hơn dò PII bằng regex. Nhưng chặn thôi chưa đủ: nếu không có chỉ số theo dõi thì cổng có lọt cũng không ai biết, phải đợi người bị hại khiếu nại.
- Điều còn chưa chắc: Cổng hiện chỉ lọc theo tên khoá, không đọc nội dung. Nếu trường được phép như `district` bị nhập lẫn SĐT hay địa chỉ chi tiết thì PII vẫn có thể lọt. Tôi chưa chắc cách nào kiểm nội dung mà không làm hỏng ca hợp lệ như `S7-05` (dãy số là mã vận đơn).