# 1. K-Nearest Neighbors
#Algorithm #Math

K-Nearest Neighbors (KNN) là một trong những thuật toán học máy có giám sát cơ bản. KNN còn được gọi là Lazy Learning, Memory-Based Learning,... Với bước huấn luyện mô hình, chỉ đơn giản là lưu trữ lại giá trị của dữ liệu huấn luyện, vì vậy KNN là phương pháp học máy không tham số (Non-Parametric). Ở bước dự đoánđ, mô hình sẽ sử dụng cácng xóộ o khoản cách để tìm các hà cgận.m lân đ

Một số độ đo thường được sử dụng trong KNN như:

1. Euclidean
2. Chebyshev
3. Manhattan
4. Minkowski

Các độ đo này tính toán dữ liệu dự đoán với các điểm dữ liệu khác được lưu trữ trong mô hình huấn luyện. Từ đó xếp hạng và tìm ra **K** điểm dữ liệu huấn luyện có kết quả gần với dữ liệu dự đoán nhất. Cuối cùng dựa vào phương pháp biểu quyết của các dữ liệu hàng xóm trong tập huấn luyện để đưa ra kết quả dự đoán.

![[Pasted image 20240926164105.png]]

<font color="#f79646">Knn classifier != knn regression because knn regression is used for predicting the new value. opposite, knn classifier is used for classification</font>