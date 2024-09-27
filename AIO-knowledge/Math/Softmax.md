#Math 
# Giải thích về hàm Softmax

Hàm **Softmax** là một hàm thường được sử dụng trong học máy, đặc biệt trong các bài toán phân loại nhiều lớp (*multi-class classification*). Nó chuyển đổi một vector giá trị thực (*real-valued vector*) thành một phân phối xác suất, mà tổng các giá trị của nó bằng 1.

Công thức của hàm Softmax cho một vector $z$ có các thành phần $z_1, z_2, ..., z_n$ là:

$$
\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{n} e^{z_j}}
$$

Trong đó:

- $e^{z_i}$ là hàm mũ của $z_i$,
- $\sum_{j=1}^{n} e^{z_j}$ là tổng của tất cả các phần tử trong vector $z$,
- Kết quả trả về là một giá trị từ 0 đến 1, thể hiện xác suất của từng phần tử trong vector.

## Tính chất của Softmax

- Hàm **Softmax** biến các giá trị đầu ra thành một phân phối xác suất: các giá trị trong khoảng từ 0 đến 1, và tổng của chúng bằng 1.
- Nó thường được sử dụng trong lớp cuối cùng của các mô hình học sâu (*deep learning models*) trong các bài toán phân loại.

## Ví dụ

Giả sử chúng ta có một vector $z = [z_1, z_2, z_3] = [1, 2, 3]$. Khi áp dụng hàm Softmax, chúng ta sẽ tính toán:

$$
\text{Softmax}(z_1) = \frac{e^1}{e^1 + e^2 + e^3}, \quad \text{Softmax}(z_2) = \frac{e^2}{e^1 + e^2 + e^3}, \quad \text{Softmax}(z_3) = \frac{e^3}{e^1 + e^2 + e^3}
$$

Sau khi tính toán, chúng ta sẽ thu được một phân phối xác suất tương ứng cho các giá trị trong vector $z$.
