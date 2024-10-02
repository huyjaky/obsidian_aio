#Terminology 

**Anomaly detection** (phát hiện bất thường) là quá trình nhận diện các điểm dữ liệu, sự kiện hoặc quan sát khác biệt so với mẫu hành vi thông thường trong một tập dữ liệu. Những bất thường này có thể biểu thị các sự kiện quan trọng như lỗi hệ thống, gian lận, hoặc các hành vi không mong muốn trong một hệ thống.

![[Anomaly.excalidraw|800]]

## Các loại bất thường
Có ba loại bất thường chính:

1. **Point anomalies** (Bất thường điểm): Một điểm dữ liệu đơn lẻ khác biệt rõ ràng so với phần còn lại. Ví dụ, một giao dịch tài chính có giá trị rất lớn so với mức trung bình của người dùng.
   
2. **Contextual anomalies** (Bất thường theo ngữ cảnh): Một điểm dữ liệu có thể bất thường trong một bối cảnh cụ thể nhưng lại bình thường trong các bối cảnh khác. Ví dụ, nhiệt độ 30°C có thể bình thường vào mùa hè nhưng là bất thường vào mùa đông.

3. **Collective anomalies** (Bất thường tập hợp): Một tập hợp các điểm dữ liệu cùng nhau bất thường, ngay cả khi mỗi điểm dữ liệu có thể không bất thường khi xem xét riêng lẻ. Ví dụ, một loạt giao dịch nhỏ nhưng liên tiếp có thể báo hiệu gian lận tài chính.

## Ứng dụng
- **Phát hiện gian lận**: Trong các giao dịch tài chính hoặc thanh toán.
- **Giám sát hệ thống**: Để phát hiện các vấn đề như lỗi máy chủ, hiệu suất kém.
- **An ninh mạng**: Phát hiện các cuộc tấn công hoặc xâm nhập mạng.
- **Y học**: Nhận diện các dấu hiệu bệnh lý hoặc tình trạng sức khỏe không bình thường.

## Phương pháp phát hiện bất thường

1. **Phương pháp dựa trên thống kê**: Phát hiện các điểm dữ liệu nằm ngoài phạm vi mong đợi của phân phối xác suất của tập dữ liệu.
2. **Phương pháp dựa trên học máy**: Sử dụng các thuật toán học có giám sát hoặc không giám sát để phát hiện bất thường.
   - **Học có giám sát**: Yêu cầu dữ liệu được gán nhãn để mô hình học cách phân biệt giữa dữ liệu bình thường và bất thường.
   - **Học không giám sát**: Tìm kiếm các mẫu bất thường mà không cần nhãn dữ liệu.
