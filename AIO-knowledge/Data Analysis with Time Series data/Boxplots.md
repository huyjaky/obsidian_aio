# Cách đọc biểu đồ Boxplot
#Graph
Biểu đồ boxplot, còn gọi là **box-and-whisker plot**, là một cách chuẩn hóa để hiển thị phân phối của dữ liệu dựa trên năm thống kê tóm tắt chính: giá trị nhỏ nhất (minimum), **first quartile** (Q1), **median**, **third quartile** (Q3), và giá trị lớn nhất (maximum). Nó giúp nhận diện các outlier và hiểu được độ phân tán và độ lệch của tập dữ liệu.
![[Pasted image 20240926120930.png]]

## Các thành phần của Boxplot

1. **Box**: Hộp (box) đại diện cho **interquartile range** (IQR), là khoảng cách giữa **first quartile** (Q1, phân vị thứ 25) và **third quartile** (Q3, phân vị thứ 75). Nó bao gồm 50% dữ liệu nằm giữa.
![[Pasted image 20240926121734.png]]
   ![[Pasted image 20240926121827.png]]
   - **Q1 (First Quartile)**: 25% các giá trị dữ liệu nằm dưới giá trị này.
   - **Median**: Đường bên trong hộp biểu diễn giá trị trung vị (phân vị thứ 50). Một nửa số dữ liệu nằm dưới giá trị này.
   - **Q3 (Third Quartile)**: 75% các giá trị dữ liệu nằm dưới giá trị này.

2. **Whiskers**: Các đường kéo dài từ hộp gọi là **whiskers**.
![[Pasted image 20240926121901.png]]
   
   - **Lower whisker** kéo dài từ Q1 đến giá trị nhỏ nhất trong tập dữ liệu không được coi là outlier.
   - **Upper whisker** kéo dài từ Q3 đến giá trị lớn nhất không được coi là outlier.
   
   **Whiskers** thường kết thúc ở một giá trị nằm trong khoảng 1.5 lần IQR từ các quartile (Q1 hoặc Q3).

3. **Outliers**: Các điểm nằm ngoài **whiskers** được coi là **outliers** và được vẽ thành các điểm riêng lẻ. **Outliers** là các giá trị nhỏ hơn Q1 - 1.5 * IQR hoặc lớn hơn Q3 + 1.5 * IQR.

4. **Notches (tùy chọn)**: Một số **boxplot** hiển thị các rãnh (**notches**) xung quanh **median**. Độ rộng của rãnh cho thấy ước tính độ không chắc chắn quanh **median**. Nếu **notches** trong hai **boxplot** không trùng lặp, điều này cho thấy các **median** của hai nhóm là khác nhau.

## Cách diễn giải Boxplot

1. **Spread (độ phân tán)**: Độ rộng của hộp biểu thị độ phân tán của 50% dữ liệu ở giữa. Hộp rộng hơn biểu thị độ biến động lớn hơn, hộp hẹp hơn biểu thị độ biến động nhỏ hơn.

2. **Symmetry/Skewness (Đối xứng/Độ lệch)**: 
   - Nếu đường **median** nằm giữa hộp, dữ liệu phân phối đối xứng.
   - Nếu đường **median** gần với Q1 hoặc Q3, dữ liệu bị lệch.
     - **Left-skewed (lệch trái)**: **Median** gần Q3, và **lower whisker** dài hơn.
     - **Right-skewed (lệch phải)**: **Median** gần Q1, và **upper whisker** dài hơn.

3. **Outliers**: Các điểm nằm ngoài **whiskers** cho thấy các giá trị cực đoan. Sự xuất hiện của nhiều **outliers** có thể chỉ ra dữ liệu có đuôi dài hoặc không phân phối chuẩn.

4. **So sánh Boxplots**: Khi so sánh nhiều **boxplot**:
   - Xem **median** để so sánh xu hướng trung tâm.
   - So sánh độ phân tán (độ rộng của các hộp) để hiểu về độ biến động.
   - Kiểm tra sự trùng lặp của **notches** để xem có sự khác biệt đáng kể giữa các **median** hay không.

## Ví dụ về Boxplot

Dưới đây là một ví dụ đơn giản về cách diễn giải **boxplot**:

- **Median**: **Median** là giá trị mà 50% dữ liệu nằm dưới. Trong một tập dữ liệu bị lệch phải, **median** sẽ gần Q1 hơn.
- **IQR (Interquartile Range)**: Khoảng giữa Q1 và Q3 cho thấy độ phân tán trung bình của dữ liệu.
- **Whiskers**: **Whiskers** giúp nhận diện khoảng dữ liệu trừ các outlier.
- **Outliers**: Các điểm nằm ngoài **whiskers**, có thể chỉ ra các giá trị bất thường.

**Boxplot** là một cách tuyệt vời để hình dung và so sánh các phân phối dữ liệu nhanh chóng, đặc biệt là khi xử lý tập dữ liệu lớn.
