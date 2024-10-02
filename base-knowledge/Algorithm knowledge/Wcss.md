#Algorithm #Math #Loss

**WCSS** (<font color="#e5b9b7">Within-Cluster Sum of Squares</font>) là một khái niệm trong học máy, cụ thể là trong phương pháp phân cụm (clustering) như **K-Means**. WCSS đo lường độ chênh lệch giữa các điểm dữ liệu trong cùng một cụm và tâm của cụm đó.

Nói cách khác, WCSS tính tổng bình phương khoảng cách từ mỗi điểm dữ liệu trong một cụm đến trung tâm cụm. Mục tiêu của K-Means là giảm thiểu WCSS, nghĩa là các điểm dữ liệu trong một cụm sẽ càng gần nhau càng tốt.

Công thức tổng quát của WCSS:

$$
WCSS = \sum_{i=1}^{k} \sum_{x \in C_i} (x - \mu_i)^2
$$

Trong đó:
- $k$ là số lượng cụm.
- $C_i$ là cụm thứ $i$.
- $x$ là một điểm dữ liệu trong cụm $C_i$.
- $\mu_i$ là tâm cụm của $C_i$.

Trong thực tế, WCSS thường được sử dụng trong phương pháp **Elbow Method** để xác định số lượng cụm phù hợp cho một bộ dữ liệu khi sử dụng K-Means.

