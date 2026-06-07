> **Lưu ý kiểm chứng:** Tài liệu này được migrate từ thư viện nghiệp vụ cũ. Mọi quy định, thuế suất, ngưỡng, thủ tục và cơ quan có thẩm quyền phải được kiểm tra lại bằng nguồn chính thức còn hiệu lực tại ngày sử dụng.

# Document Ops Report — Short Example

## Mẫu gọn
- **Scope:** Đổi tên và phân loại 48 file hồ sơ đầu vào theo bộ tên chuẩn đã thống nhất.
- **Actions completed:** rename file; gom theo nhóm pháp lý đất / đầu tư / xây dựng; giữ nguyên nội dung file.
- **Exceptions:** 5 file chưa rename dứt điểm vì tên source quá mơ hồ hoặc trùng logic phân loại.
- **Output status:** Document set đã sạch hơn để review pháp lý bước đầu, nhưng chưa phải data room orchestration hoàn chỉnh.
- **Next step:** Cần xác nhận 5 file exception trước khi chốt final naming set.
- **Owner boundary:** `doc-renamer` xử lý document ops nhẹ; nếu phát sinh tracker nhiều owner hoặc data room flow lớn thì route `RE-HQ`.

## Lỗi thường gặp
- Biến report này thành tracker nhiều owner.
- Không nói rõ exceptions nên người đọc tưởng toàn bộ set đã final.
