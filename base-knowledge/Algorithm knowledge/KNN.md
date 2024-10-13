# 1. K-Nearest Neighbors
#Algorithm #Math

K-Nearest Neighbors (KNN) là một trong những thuật toán học máy có giám sát cơ bản. KNN còn được gọi là Lazy Learning, Memory-Based Learning,... Với bước huấn luyện mô hình, chỉ đơn giản là lưu trữ lại giá trị của dữ liệu huấn luyện, vì vậy KNN là phương pháp học máy không tham số (Non-Parametric). Ở bước dự đoán sẽ lấy những điểm gần với nó nhất để dự đoán xem nó thuộc Class nào hoặc dùng knn để dự đoán xem giá trị trong tương lai

Một số độ đo thường được sử dụng trong KNN như:

1. [[Euclidean]] (p=2)
2. [[Chebyshev]] (p=1)
3. [[Manhattan]] (p=norm)
4. [[Minkowski]] (p=\infty)

Các độ đo này tính toán dữ liệu dự đoán với các điểm dữ liệu khác được lưu trữ trong mô hình huấn luyện. Từ đó xếp hạng và tìm ra **K** điểm dữ liệu huấn luyện có kết quả gần với dữ liệu dự đoán nhất. Cuối cùng dựa vào phương pháp biểu quyết của các dữ liệu hàng xóm trong tập huấn luyện để đưa ra kết quả dự đoán.

![[Pasted image 20240926164105.png]]

<span style="background:#b1ffff">Knn classifier != knn regression</span>
1. classifier: để phân loại
2. regression: dùng để dự đoán với công thức $Y_{\text{pred}} = \frac{1}{k} \sum_{x \in NB} y_x$

## Sự quan trọng của Norm trong KNN

-> ![[Norm]]

## Tối ưu tính distance trong KNN bằng KD-tree

-> ![[KD-tree]]

