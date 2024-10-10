#Terminology
## Overfitting là gì?

![[DecisionTree_Regression_AIO2024.pdf#page=45&rect=1,31,955,450&color=important|DecisionTree_Regression_AIO2024, p.45]]

Overfitting là hiện tượng xảy ra khi một mô hình học máy (machine learning) **quá phù hợp với dữ liệu huấn luyện**, đến mức nó học cả những nhiễu loạn hoặc đặc điểm không liên quan trong dữ liệu. Điều này dẫn đến việc mô hình hoạt động rất tốt trên dữ liệu huấn luyện nhưng kém hiệu quả khi áp dụng vào dữ liệu mới, chưa từng thấy trước đó.

## Đặc điểm chính của overfitting:

1. **Hiệu suất cao trên dữ liệu huấn luyện**: Mô hình có thể dự đoán rất chính xác trên tập huấn luyện.
2. **Hiệu suất thấp trên dữ liệu kiểm tra**: Khi áp dụng mô hình vào dữ liệu kiểm tra (hoặc dữ liệu mới), mô hình thường cho kết quả sai lệch hoặc không chính xác vì nó không thể tổng quát hóa tốt.
3. **Mô hình phức tạp quá mức**: Overfitting thường xảy ra khi mô hình có quá nhiều tham số hoặc các lớp phức tạp hơn mức cần thiết, khiến nó học cả những chi tiết nhỏ không quan trọng trong dữ liệu.

## Ví dụ

Nếu bạn xây dựng một mô hình phân loại hình ảnh để nhận diện mèo và chó, nhưng dữ liệu huấn luyện của bạn chứa những bức ảnh có nền màu đặc trưng (ví dụ, tất cả ảnh mèo có nền xanh và tất cả ảnh chó có nền đỏ), mô hình có thể học nhầm rằng **màu nền** là yếu tố quan trọng để phân biệt mèo và chó. Điều này dẫn đến việc mô hình không thể hoạt động tốt trên ảnh mèo hoặc chó có nền khác màu xanh hoặc đỏ.

## Cách giảm overfitting:

- **Tăng kích thước dữ liệu**: Cung cấp thêm dữ liệu để mô hình có thể học được các đặc điểm thực sự quan trọng.
- **Sử dụng regularization**: Áp dụng các kỹ thuật như L1, L2 để giới hạn độ phức tạp của mô hình.
- **Cross-validation**: Sử dụng phương pháp kiểm tra chéo để đảm bảo mô hình không chỉ hoạt động tốt trên một tập dữ liệu cụ thể.
- **Early stopping**: Dừng quá trình huấn luyện sớm nếu thấy lỗi trên dữ liệu kiểm tra bắt đầu tăng.

Overfitting là một trong những thách thức phổ biến khi xây dựng mô hình học máy.
