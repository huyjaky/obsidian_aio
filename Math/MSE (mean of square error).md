#Math #Loss 
## MSE (Mean square error) là gì: 

công thức: 
$$
MSE = \frac{SSE}{n} = \frac{1}{n} \cdot \frac{1}{2} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$
$$
SSE = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$
- $n$ là số lượng node cần tính 
- $y_i$ là giá trị của từng node cần tính
- $\hat{y}_i$ là giá trị trung bình của tất cả các node cần tính  

-> Công thức này để thay cho $SSE$ bên trên và dựa vào cái cày để xây dựng cây

| Tiêu chí                          | SSE (Sum of Squared Errors)                                          | MSE (Mean Squared Error)                                                                               |
| --------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Công thức**                     | Tổng các sai số bình phương                                          | Trung bình các sai số bình phương                                                                      |
| **Phạm vi giá trị**               | Tăng lên khi số lượng quan sát tăng                                  | Chuẩn hóa theo số lượng quan sát                                                                       |
| **Đơn vị**                        | Cùng đơn vị với biến dự đoán, nhưng không chuẩn hóa theo số quan sát | Cùng đơn vị với biến dự đoán, nhưng chuẩn hóa theo số quan sát                                         |
| **So sánh giữa các mô hình**      | Khó so sánh nếu kích thước tập dữ liệu khác nhau                     | Dễ so sánh vì được chuẩn hóa theo số lượng quan sát                                                    |
| **Ứng dụng trong cây quyết định** | Ít được sử dụng do không chuẩn hóa                                   | <span style="background:#b1ffff">Thường được dùng </span>để chọn cách phân tách trong bài toán hồi quy |
### Khi nào sử dụng SSE và MSE?

- **SSE**: Sử dụng khi bạn muốn biết tổng sai số của mô hình mà không cần phải chuẩn hóa theo kích thước tập dữ liệu.
- **MSE**: Sử dụng khi bạn cần đánh giá sai số trung bình và so sánh giữa các mô hình hoặc các tập dữ liệu có kích thước khác nhau.

## Tầm quan trọng của MSE (mean of square error):

-> Loss function này thường xuyên được áp dụng tron các bài toàn hồi quy tuyến tính nên phải học chắc phần này 