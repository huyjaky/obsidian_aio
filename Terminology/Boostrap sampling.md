#Terminology #data

## Định nghĩa

**Bootstrap sampling** là một phương pháp thống kê dùng để ước lượng các đặc trưng (chẳng hạn như trung bình, phương sai) của một phân phối dữ liệu bằng cách lấy mẫu ngẫu nhiên từ tập dữ liệu hiện có. Đây là một kỹ thuật đặc biệt hữu ích khi không có đủ dữ liệu hoặc khi không biết phân phối xác suất thực sự của dữ liệu.

## Cách thực hiện Bootstrap Sampling:
1. Từ tập dữ liệu ban đầu gồm \(n\) điểm dữ liệu, tiến hành chọn ngẫu nhiên \(n\) điểm dữ liệu *có hoàn lại* (có thể chọn lại những phần tử đã chọn).
2. Tạo một mẫu mới (gọi là "bootstrap sample") có kích thước bằng tập dữ liệu ban đầu.
3. Tính toán các chỉ số thống kê từ mẫu mới này, chẳng hạn như trung bình, phương sai, hoặc bất kỳ chỉ số nào khác.
4. Lặp lại quá trình trên nhiều lần (thường là hàng ngàn lần), sau đó phân tích kết quả của tất cả các mẫu để ước lượng chỉ số thống kê của toàn bộ tập dữ liệu.

Phương pháp bootstrap đặc biệt hiệu quả khi cần đánh giá độ tin cậy của các ước lượng thống kê (như tính khoảng tin cậy) mà không cần phải giả định về phân phối của dữ liệu.

<span style="background:#b1ffff">Ví dụ:</span>

![[Excalidraw/Random-forest.excalidraw.md#^group=H5jjdAf9|Pretrain Random Forest | 800]]