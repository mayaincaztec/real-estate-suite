> **Lưu ý kiểm chứng:** Tài liệu này được migrate từ thư viện nghiệp vụ cũ. Mọi quy định, thuế suất, ngưỡng, thủ tục và cơ quan có thẩm quyền phải được kiểm tra lại bằng nguồn chính thức còn hiệu lực tại ngày sử dụng.

# PDF export workflow for legal reports on Windows

Dùng reference này khi Sếp yêu cầu **deliverable dạng PDF** cho báo cáo pháp lý, memo hoặc note trong agent `RE-Legal` và môi trường không có sẵn `pandoc`, `wkhtmltopdf`, `weasyprint` hoặc Python PDF package.

## Khi nào áp dụng

- Đã có nội dung pháp lý tương đối hoàn chỉnh.
- Cần giao **artifact thực tế là file PDF**, không chỉ là text trong chat.
- Môi trường có `node` / `npm`, nhưng chưa chắc có tool chuyển đổi tài liệu chuyên dụng.
- Đặc biệt hữu ích trên Windows host khi có thể tận dụng font hệ thống như `C:\Windows\Fonts\times.ttf`, `timesbd.ttf`, `timesi.ttf`, `timesbi.ttf`.

## Cách làm thực dụng

### Phương án ưu tiên 1 — dùng tool có sẵn
Nếu có sẵn `pandoc`, `wkhtmltopdf` hoặc công cụ tương đương, có thể dùng pipeline quen thuộc để render PDF.

### Phương án fallback bền vững — Node + `pdf-lib`
Khi không có tool render PDF sẵn có:
1. Tạo thư mục làm việc riêng cho deliverable.
2. Chạy `npm init -y`.
3. Cài `pdf-lib` và `@pdf-lib/fontkit`.
4. Viết script Node để:
   - nhúng font hệ thống tiếng Việt;
   - khai báo metadata PDF;
   - chia section rõ ràng;
   - wrap text theo chiều rộng trang;
   - tự xuống trang và thêm header/footer/page number;
   - xuất ra file PDF thật.
5. Chạy script và kiểm tra file đầu ra tồn tại, có header `%PDF-` và kích thước hợp lý.

## Nội dung nên có trong PDF legal report

- tiêu đề báo cáo;
- định danh văn bản / chủ đề;
- phần tóm tắt điều hành;
- các section phân tích có heading rõ;
- nguồn văn bản / căn cứ;
- lưu ý phạm vi sử dụng hoặc disclaimer ngắn nếu phù hợp.

## Pitfalls

1. Không dừng ở việc soạn nội dung text khi user đã yêu cầu PDF.
2. Nếu converter quen thuộc không có sẵn, đừng bỏ cuộc sớm; thử fallback bằng Node trước.
3. Với tiếng Việt, phải dùng font có hỗ trợ Unicode/Vietnamese; font nhúng từ Windows system fonts là cách nhanh, ổn định trong môi trường local Windows.
4. Phải xác minh file PDF đã được tạo thật, thay vì chỉ tin vào log script.

## Verification tối thiểu

- file tồn tại đúng path;
- file mở đầu bằng `%PDF-`;
- kích thước file khác 0 và hợp lý;
- tên file rõ ràng, chuyên nghiệp, phù hợp deliverable.
