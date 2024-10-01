# 1. K-Nearest Neighbors
#Algorithm #Math

K-Nearest Neighbors (KNN) là một trong những thuật toán học máy có giám sát cơ bản. KNN còn được gọi là Lazy Learning, Memory-Based Learning,... Với bước huấn luyện mô hình, chỉ đơn giản là lưu trữ lại giá trị của dữ liệu huấn luyện, vì vậy KNN là phương pháp học máy không tham số (Non-Parametric). Ở bước dự đoán sẽ lấy những điểm gần với nó nhất để dự đoán xem nó thuộc Class nào hoặc dùng knn để dự đoán xem giá trị trong tương lai

Một số độ đo thường được sử dụng trong KNN như:

1. Euclidean
2. Chebyshev
3. Manhattan
4. Minkowski
## Euclidean (p=2)
$$
d(\mathbf{x}, \mathbf{y}) = \sqrt{\sum_{i=1}^{n}(x_i - y_i)^2}
$$

## Manhattan (p=1)
$$
d(\mathbf{x}, \mathbf{y}) = \sum_{i=1}^{n} |x_i - y_i|
$$

## Minkowski (p=norm)
$$
d(\mathbf{x}, \mathbf{y}) = \left( \sum_{i=1}^{n} |x_i - y_i|^p \right)^{\frac{1}{p}}
$$

## Chebyshev (p=\infty)
$$
d(\mathbf{x}, \mathbf{y}) = \lim_{p \to \infty} \left( \sum_{i=1}^{n} |x_i - y_i|^p \right)^{\frac{1}{p}} = \max_i |x_i - y_i|
$$


Các độ đo này tính toán dữ liệu dự đoán với các điểm dữ liệu khác được lưu trữ trong mô hình huấn luyện. Từ đó xếp hạng và tìm ra **K** điểm dữ liệu huấn luyện có kết quả gần với dữ liệu dự đoán nhất. Cuối cùng dựa vào phương pháp biểu quyết của các dữ liệu hàng xóm trong tập huấn luyện để đưa ra kết quả dự đoán.

![[Pasted image 20240926164105.png]]

Knn classifier != knn regression
1. classifier: để phân loại
2. regression: dùng để dự đoán với công thức $Y_{\text{pred}} = \frac{1}{k} \sum_{x \in NB} y_x$


