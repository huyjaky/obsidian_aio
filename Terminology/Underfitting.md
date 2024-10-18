#Terminology 
## Underfitting là gì?
![[DecisionTree_Regression_AIO2024.pdf#page=45&rect=1,31,955,450&color=important|DecisionTree_Regression_AIO2024, p.45]]
- [[Bias]]

Underfitting là hiện tượng xảy ra khi một mô hình học máy (machine learning) **không học đủ từ dữ liệu huấn luyện**, dẫn đến khả năng dự đoán kém cả trên dữ liệu huấn luyện và dữ liệu mới. Mô hình quá đơn giản để nắm bắt được các mối quan hệ quan trọng trong dữ liệu, dẫn đến hiệu suất thấp.

## Đặc điểm chính của underfitting:

1. **Hiệu suất kém trên dữ liệu huấn luyện**: Mô hình không thể dự đoán tốt ngay cả trên dữ liệu huấn luyện, cho thấy nó chưa học được các mẫu quan trọng.
2. **Hiệu suất kém trên dữ liệu kiểm tra**: Do mô hình quá đơn giản, nó không thể tổng quát hóa tốt cho dữ liệu mới, và kết quả dự đoán không chính xác.
3. **Mô hình đơn giản quá mức**: Underfitting thường xảy ra khi mô hình quá đơn giản, có quá ít tham số hoặc không đủ độ phức tạp để nắm bắt hết các đặc điểm quan trọng trong dữ liệu.

## Ví dụ

Nếu bạn xây dựng một mô hình tuyến tính đơn giản để dự đoán giá nhà, nhưng giá nhà phụ thuộc vào nhiều yếu tố phức tạp như diện tích, vị trí, tình trạng nhà... Mô hình của bạn chỉ xem xét một vài yếu tố và bỏ qua các yếu tố khác, dẫn đến dự đoán không chính xác. Đây là hiện tượng underfitting vì mô hình quá đơn giản so với dữ liệu thực tế.

## Cách giảm underfitting:

- **Tăng độ phức tạp của mô hình**: Sử dụng các mô hình phức tạp hơn (như thêm nhiều tham số, sử dụng các phương pháp phi tuyến tính) để nắm bắt được các đặc điểm phức tạp trong dữ liệu.
- **Tính năng chọn lọc**: Chọn những đặc điểm liên quan và thêm chúng vào mô hình để nó có thể học được các mối quan hệ quan trọng.
- **Tăng thời gian huấn luyện**: Đảm bảo rằng mô hình được huấn luyện đủ lâu để học được từ dữ liệu.

Underfitting thường xảy ra khi mô hình hoặc thuật toán không đủ mạnh để học từ dữ liệu, dẫn đến hiệu suất kém trên cả tập huấn luyện và tập kiểm tra.
