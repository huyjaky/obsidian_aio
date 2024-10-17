#Terminology #statistics 

## Recall là gì?

**Recall**, hay còn gọi là **Sensitivity** (độ nhạy), là một trong những chỉ số quan trọng dùng để đánh giá hiệu suất của các mô hình phân loại, đặc biệt là trong các tình huống mà việc phát hiện các mẫu thuộc một lớp cụ thể là quan trọng. Recall được sử dụng phổ biến trong các bài toán phân loại nhị phân và nhiều lớp.

## Định nghĩa:

Recall đo lường tỷ lệ các **dự đoán đúng** trong số các **mẫu thực sự dương**. Nói cách khác, nó trả lời câu hỏi: "Trong số tất cả các mẫu dương thực sự, mô hình đã phát hiện được bao nhiêu mẫu?"

## Công thức tính:

$$
\text{Recall} = \frac{\text{Số lượng True Positives}}{\text{Số lượng True Positives} + \text{Số lượng False Negatives}}
$$

- **True Positives (TP)**: Số lượng mẫu thực sự dương (positives) được dự đoán đúng là dương.
- **False Negatives (FN)**: Số lượng mẫu thực sự dương nhưng lại bị dự đoán sai là âm (negatives).

## Ví dụ:

Giả sử bạn đang xây dựng một mô hình phát hiện email spam. Trong tổng số 100 email spam thực sự, mô hình của bạn chỉ phát hiện được 80 email là spam và bỏ sót 20 email.

- **True Positives (TP)**: 80 email spam được phát hiện đúng.
- **False Negatives (FN)**: 20 email spam nhưng không được phát hiện.

Khi đó, recall của mô hình sẽ là:

$$
\text{Recall} = \frac{80}{80 + 20} = 0.8 \, \text{(80\%)}
$$

## Ý nghĩa của Recall:

- **Recall cao**: Điều này có nghĩa là mô hình phát hiện gần như tất cả các trường hợp dương (positives). Ví dụ, trong một bài toán chẩn đoán bệnh, recall cao có nghĩa là mô hình gần như không bỏ sót các bệnh nhân mắc bệnh.
- **Recall thấp**: Mô hình bỏ sót nhiều trường hợp dương. Điều này có thể là vấn đề trong các bài toán mà việc bỏ sót là nguy hiểm hoặc tốn kém (ví dụ: phát hiện ung thư, phát hiện gian lận, v.v.).

## So sánh với [[Precision]]:

Trong khi **recall** tập trung vào việc phát hiện tất cả các trường hợp dương, **precision** lại tập trung vào việc đảm bảo rằng các dự đoán dương là chính xác. Cả recall và precision đều quan trọng, và việc đạt được cân bằng giữa chúng là một thách thức trong nhiều bài toán.
