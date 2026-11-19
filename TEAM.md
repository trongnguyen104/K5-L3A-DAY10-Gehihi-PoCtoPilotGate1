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

- `CÁC NHÁNH GUARD.`
- `CÁC TEST/TRACE.`
- `XỬ LÝ THẺ S7.`

### Bằng chứng

- Mã commit: `a6c51beeeb0d3ba077b509fa04a734547214706e`.
- File/nhánh code: `lab10/guards.py`.
- Mã lần chạy: `[BỔ SUNG MÃ RUN/TRACE THỰC TẾ]`.
- Dòng/ô phiếu: `[BỔ SUNG MỤC PHIẾU THỰC TẾ]`.

### Exit ticket

- Điều học được: `Chưa có`.
- Điều còn chưa chắc: `Chưa có`.

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
- Phụ trách hoặc phối hợp phần trace và kiểm thử các ticket biên bằng `python -m lab10.trace`, bao gồm kiểm tra hành vi phân loại intent, truy xuất tracking, đề xuất hoàn tiền, ghi lỗi hãng và thông báo hãng.
- Phụ trách hoặc phối hợp `lab10/monitors.py`: bổ sung ít nhất một monitor mới ở vòng 2, đăng ký trong dict `MONITORS`, kiểm tra monitor trên bộ incident.
- Chạy unit tests, regression và các lệnh `lab10.grade --incident S7`; báo lại lỗi và bằng chứng cho cả bàn.
- Phối hợp đánh giá bộ lọc PII và tính đúng đắn của parcel/carrier trước khi ghi lỗi hoặc gửi thông báo.

### Đóng góp cụ thể

- `CÁC TRACE/TEST ĐÃ TỰ CHẠY; TICKET, ORDER, CUSTOMER VÀ KẾT QUẢ.`
- `MONITOR MỚI ĐÃ VIẾT, CÔNG THỨC/TÊN CHỈ SỐ VÀ KẾT QUẢ.`
- `CÁC LỖI ĐÃ PHÁT HIỆN VÀ CÁCH PHỐI HỢP SỬA.`

### Bằng chứng

- Mã commit: `b7efaeb26c406004e8675144ca7852530c8ff6e0`.
- File phụ trách/phối hợp: `lab10/guards.py`, `lab10/monitors.py`, `tests/`.
- Mã lần chạy/trace/grade: `MÃ RUN/TRACE/GRADE`.
- Dòng/ô phiếu: `BỔ SUNG B2, B7.1–B7.3, B7.6, C2, C6–C9`.

### Exit ticket

- Điều học được: `Chưa có`.
- Điều còn chưa chắc: `Chưa có`.