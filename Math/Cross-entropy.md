 #Loss #Terminology #entropy #Math 

**Cross-Entropy Loss** là một hàm mất mát thường được sử dụng trong các bài toán phân loại, đặc biệt là trong mạng nơ-ron. Nó <span style="background:#b1ffff">đo lường sự khác biệt giữa hai phân phối xác suất</span>: phân phối dự đoán ($p$) và phân phối mục tiêu thực sự ($q$). Hàm mất mát này càng nhỏ khi phân phối dự đoán càng gần với phân phối mục tiêu.

Công thức của hàm mất mát Cross-Entropy cho một mẫu duy nhất là:

$$
L = - \sum_{i=1}^{N} q_i \log(p_i)
$$

Trong đó:

- $N$ là số lượng lớp (classes),
- $q_i$ là xác suất mục tiêu của lớp $i$ (thường là 1 cho lớp chính xác và 0 cho các lớp khác trong trường hợp one-hot encoding),
- $p_i$ là xác suất dự đoán của lớp $i$.

Đối với bài toán phân loại nhị phân (<font color="#f79646">Binary Cross-Entropy Loss</font>), công thức đơn giản hơn:

$$
L = - (y \log(p) + (1 - y) \log(1 - p))
$$

Trong đó:
- $y$ là nhãn thực sự (0 hoặc 1),
- $p$ là xác suất dự đoán cho lớp 1.
