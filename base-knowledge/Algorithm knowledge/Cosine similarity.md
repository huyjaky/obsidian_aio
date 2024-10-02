#Algorithm #Math #similarity

**Cosine similarity** là <span style="background:#b1ffff">một phương pháp để đo lường mức độ tương đồng giữa hai vector trong không gian vector</span> bằng cách tính góc giữa chúng. Cosine similarity thường được sử dụng trong xử lý ngôn ngữ tự nhiên và học máy để so sánh các tài liệu hoặc từ khoá, vì nó đánh giá sự khác biệt theo hướng giữa hai vector thay vì độ lớn của chúng.



## Công thức

Công thức của **cosine similarity** giữa hai vector A và B được biểu diễn như sau:

$$
\text{Cosine similarity}(A, B) = \frac{A\cdot B}{||A|| \times ||B||}
$$

Trong đó:
- $A\cdot B$ là tích vô hướng của hai vector.
- $||A||$ và $||B||$ là độ dài của vector A và B (norm hay độ lớn vector).
- Kết quả sẽ nằm trong khoảng từ -1 đến 1:
  - **1**: Hai vector hoàn toàn tương đồng.
  - **0**: Hai vector vuông góc, không tương đồng.
  - **-1**: Hai vector hoàn toàn ngược hướng.

## Ứng dụng

Cosine similarity đặc biệt hữu ích trong các bài toán xử lý văn bản, khi các văn bản được chuyển đổi thành các vector (chẳng hạn sử dụng phương pháp Bag of Words hoặc TF-IDF). Kỹ thuật này bỏ qua yếu tố độ dài, tập trung vào góc giữa các vector đại diện cho văn bản, giúp đo lường nội dung mà không bị ảnh hưởng bởi độ dài của tài liệu.
