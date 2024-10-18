#Terminology
## Định nghĩa Bias là gì?
-> Bias ở đây có khá nhiều nghĩa :
- Có nghĩa là thiên vị về một label hoặc một feature nào đó lúc train
- có nghĩa là độ phức tạp của mô hình $Bias^2$ 

## Bias (Thiên vị):
Trong bối cảnh huấn luyện trí tuệ nhân tạo (AI), **bias (thiên vị)** đề cập đến sự thiên lệch hoặc sai lệch trong cách mà mô hình học máy đưa ra quyết định hoặc dự đoán dựa trên dữ liệu được huấn luyện. Bias theo nghĩa thiên vị xảy ra khi dữ liệu huấn luyện có những mẫu không đồng đều hoặc không đại diện cho toàn bộ dân số, từ đó dẫn đến các kết quả không công bằng hoặc sai lệch.

### Một số dạng bias trong huấn luyện AI:

1. **Selection bias (Thiên vị chọn lọc):** Xảy ra khi dữ liệu huấn luyện không được lấy mẫu ngẫu nhiên hoặc không đại diện, làm cho mô hình học máy phản ánh sự thiên vị của dữ liệu này. Ví dụ: nếu một mô hình nhận diện khuôn mặt được huấn luyện chủ yếu trên dữ liệu người da trắng, mô hình đó có thể hoạt động kém khi nhận diện người da màu.

2. **Confirmation bias (Thiên vị xác nhận):** Là xu hướng chỉ tập trung vào những dữ liệu khớp với các giả định ban đầu hoặc những gì đã được mong đợi, làm bỏ qua các mẫu hoặc dữ liệu ngược lại.

3. **Historical bias (Thiên vị lịch sử):** Xảy ra khi mô hình học máy được huấn luyện dựa trên dữ liệu lịch sử có tính thiên vị. Ví dụ: nếu trong lịch sử, các quyết định tuyển dụng có tính thiên vị giới tính hoặc chủng tộc, mô hình học máy học từ dữ liệu này có thể duy trì và phản ánh những thiên vị này.

4. **Implicit bias (Thiên vị ngầm):** Là những thiên vị không nhận thức được, nhưng vẫn tồn tại trong quá trình huấn luyện. Các đặc điểm không rõ ràng trong dữ liệu (ví dụ: tên, ngôn ngữ) có thể ngầm ảnh hưởng đến kết quả dự đoán của mô hình.

### Cách giảm thiểu bias trong AI:

- **Thu thập dữ liệu đa dạng và đại diện:** Đảm bảo rằng dữ liệu huấn luyện phản ánh đủ các đặc điểm của toàn bộ dân số để mô hình không thiên vị.
- **Kiểm tra và điều chỉnh mô hình:** Sử dụng các phương pháp kiểm tra và hiệu chỉnh mô hình để phát hiện các dấu hiệu thiên vị và đưa ra các điều chỉnh phù hợp.
- **Đảm bảo tính minh bạch và trách nhiệm giải trình:** Việc công khai quá trình phát triển, dữ liệu sử dụng, và phương pháp kiểm tra bias sẽ giúp phát hiện và giải quyết các vấn đề thiên vị sớm hơn.

Thiên vị trong AI có thể dẫn đến hậu quả nghiêm trọng nếu không được kiểm soát, do đó việc giảm thiểu bias là yếu tố then chốt để tạo ra những mô hình học máy công bằng và chính xác.


---
## $Bias^2$ (Độ phức tạp của mô hình):
![[DecisionTree_Regression_AIO2024.pdf#page=45&rect=1,31,955,450&color=important|DecisionTree_Regression_AIO2024, p.45]]

Từ hình ảnh này, ta có thể giải thích khái niệm **bias (độ lệch)** trong bối cảnh các mô hình học máy.

1. **Bias (độ lệch)** đề cập đến lỗi gây ra bởi các mô hình quá đơn giản, không thể nắm bắt đầy đủ các mẫu hoặc quy luật ẩn trong dữ liệu. Trong biểu đồ đầu tiên ở bên trái (biểu đồ về sự cân bằng giữa Bias và Variance), đường cong **Bias²** di chuyển xuống khi độ phức tạp của mô hình tăng lên. Điều này thể hiện rằng các mô hình đơn giản (ở phía bên trái) có **bias cao** do chúng giả định quá nhiều điều về dữ liệu và do đó không thể mô hình hóa dữ liệu một cách chính xác.

2. Các mô hình có bias cao thường [[Underfitting]] (khớp kém) dữ liệu. Điều này có nghĩa là chúng không nắm bắt được những mối quan hệ quan trọng trong dữ liệu huấn luyện, dẫn đến lỗi lớn (bias cao). Như biểu đồ cho thấy, **tổng lỗi** (total error) cao hơn khi bias chiếm ưu thế (ở phía bên trái trục độ phức tạp của mô hình). Bias giảm dần khi mô hình phức tạp hơn (di chuyển về phía giữa biểu đồ, nơi mô hình phù hợp tốt hơn).

3. Ngược lại, khi bias giảm (khi mô hình phức tạp hơn), **variance (phương sai)** có xu hướng tăng, như được thể hiện bởi đường cong phương sai đi lên trong biểu đồ. Các mô hình có phương sai cao có thể trở nên quá phức tạp, khiến chúng [[Overfitting]] (quá khớp) dữ liệu huấn luyện, dẫn đến hiệu suất tổng quát kém trên dữ liệu chưa từng thấy.

#### Như thế nào là low và high $Bias^2$

![[Random Forest_AIO2024.pdf#page=14&rect=10,1,869,469|Random Forest_AIO2024, p.14]]

$$
RSS = \sum_{i=1}^{n} \left( y_i - f(x_i) \right)^2
$$
- $y_i$: là giá trị thực tế của điểm dữ liệu thứ $i$.
- $f(x_i)$: là giá trị dự đoán của mô hình hồi quy cho điểm dữ liệu $x_i$.
- $n$: là số lượng dữ liệu hoặc mẫu.

![[Random Forest_AIO2024.pdf#page=14&rect=12,223,488,466|Random Forest_AIO2024, p.14|400]]
Dựa vào bức hình này ta có thể thấy $RSS$ lớn hơn không chứng tỏ là độ sai lệch là có nên ta có thể hiểu là mô hình có $Bias^2$ (độ phức tạp) khá đơn giản làm cho mô hình học không quá sát với dữ liệu 
-> high $Bias^2$

![[Random Forest_AIO2024.pdf#page=14&rect=21,2,505,212|Random Forest_AIO2024, p.14 | 400]]
Ngược lại với ở trên thì mô hình khá phức tạp và nó đa

---


