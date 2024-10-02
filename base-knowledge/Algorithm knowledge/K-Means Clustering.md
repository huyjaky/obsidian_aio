#Algorithm #Math #clustering

## 2.1 Lý thuyết

Thuật toán **K-Means** là một thuật toán phân cụm phổ biến và được sử dụng rộng rãi trong các bài toán học máy (machine learning) và khai phá dữ liệu (data mining). Mục tiêu của K-Means là phân chia n điểm dữ liệu thành k cụm sao cho các điểm trong cùng một cụm có độ tương đồng cao nhất.

## Quy trình cơ bản của K-Means bao gồm các bước sau:

![[[Slide]-KNN-KMean_v2.pdf#page=51&rect=109,3,475,403&color=important|[Slide]-KNN-KMean_v2, p.51]]

1. **Khởi tạo**: Lựa chọn ngẫu nhiên k điểm từ tập dữ liệu làm các tâm cụm ban đầu.

2. **Gán nhãn**: Với mỗi điểm dữ liệu, tính khoảng cách từ điểm đó tới mỗi tâm cụm và gán nó vào cụm có tâm gần nhất. Khoảng cách thường được đo bằng khoảng cách Euclid, được tính như sau:

   $$ 
   d(x_i, c_j) = \sqrt{\sum_{l=1}^{m} (x_{il} - c_{jl})^2} 
   $$

   trong đó, \(x_i\) là điểm dữ liệu, \(c_j\) là tâm cụm, và \(m\) là số chiều của dữ liệu.

3. **Cập nhật tâm cụm**: Sau khi đã gán nhãn cho tất cả các điểm, cập nhật lại vị trí của các tâm cụm bằng cách tính trung bình các điểm dữ liệu trong mỗi cụm:

   $$
   c_j = \frac{1}{|C_j|} \sum_{x_i \in C_j} x_i
   $$

   trong đó, \(C_j\) là tập hợp các điểm dữ liệu thuộc cụm \(j\).

4. **Lặp lại**: Lặp lại quá trình gán nhãn và cập nhật tâm cụm cho đến khi các tâm cụm không còn thay đổi đáng kể hoặc đạt đến số lần lặp tối đa.
   
5. **Loss funciont: [[Wcss]]

## Ứng dụng Clustering (phân cụm) trong K-means

-> [[Clustering]]

## Sự quan trọng của Norm trong K-means clustering

-> [[Norm]] 
## Tổng kết

Thuật toán K-Means có độ phức tạp thời gian là 
$O(n \times k \times t \times m)$, <font color="#e5b9b7">trong đó t là số lần lặp và m là số chiều của dữ liệu</font>. K-Means thường được sử dụng vì tính đơn giản và hiệu quả cao trong việc phân cụm dữ liệu lớn, mặc dù nó có thể không tìm được nghiệm tối ưu toàn cục (global optimization) do phụ thuộc vào việc khởi tạo các tâm cụm ban đầu.

```Python
import numpy as np

X = np.array([1.4, 1, 1.5, 3.1, 3.8, 4.1]).reshape(-1, 1)  # init data

# 1. random init centroid 
k = 2
C = X[:k].reshape(1, -1)

while True:
    # 2. find distance from C and X
    DISTANCE = np.abs(X - C)
    # 3. find index belong to k clasifier
    INDEX = np.argmin(DISTANCE, axis=1)  # -> [1,0,1,0,0 ...]
    # 4. find new C with mean C old
    C_NEW = np.array(
        [X[INDEX == i].mean() for i in np.unique(INDEX)]
    )  # -> get unique object in INDEX arr
        
    # dont need give iter number beacause centroid dont change anymore
    if np.all(C_NEW == C):
        break
    C = C_NEW

print(C)
```

