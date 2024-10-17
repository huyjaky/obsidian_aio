#Terminology #statistics 
## Precision là gì?

**Precision** là một chỉ số trong học máy, đặc biệt trong các bài toán phân loại, dùng để đo lường độ chính xác của các dự đoán dương (positives). Precision trả lời câu hỏi: "Trong số các mẫu được dự đoán là dương, có bao nhiêu mẫu thực sự dương?"

## Định nghĩa:

Precision đo lường tỷ lệ các **dự đoán dương chính xác** trong số các mẫu được dự đoán là dương. Nó cho biết mức độ chính xác của các dự đoán mà mô hình cho là dương.

## Công thức tính:

$$
\text{Precision} = \frac{\text{Số lượng True Positives}}{\text{Số lượng True Positives} + \text{Số lượng False Positives}}
$$

- **True Positives (TP)**: Số lượng mẫu thực sự dương được dự đoán đúng là dương.
- **False Positives (FP)**: Số lượng mẫu thực sự âm nhưng bị dự đoán sai là dương.

## Ví dụ:

Giả sử bạn đang xây dựng một mô hình phát hiện email spam. Mô hình của bạn dự đoán tổng cộng 90 email là spam, nhưng trong số đó chỉ có 80 email thực sự là spam và 10 email còn lại không phải là spam (dự đoán sai).

- **True Positives (TP)**: 80 email spam được dự đoán đúng.
- **False Positives (FP)**: 10 email không phải spam nhưng bị dự đoán sai là spam.

Khi đó, precision của mô hình sẽ là:

$$
\text{Precision} = \frac{80}{80 + 10} = 0.89 \, \text{(89\%)}
$$

## Ý nghĩa của Precision:

- **Precision cao**: Điều này có nghĩa là khi mô hình dự đoán dương (ví dụ như email spam), thì đa số các dự đoán đó là chính xác. Điều này rất quan trọng trong các bài toán như phát hiện gian lận, chẩn đoán bệnh, khi dự đoán sai có thể gây tốn kém hoặc gây hại.
- **Precision thấp**: Có nghĩa là mô hình có nhiều dự đoán dương bị sai, tức là mô hình dự đoán nhiều mẫu là dương nhưng thực sự lại là âm (gây ra nhiều cảnh báo sai).

## So sánh với [[Recall]]:

- **Precision** tập trung vào việc giảm số lượng dự đoán dương sai (False Positives), còn **Recall** tập trung vào việc phát hiện tất cả các mẫu dương thực sự (True Positives).
- Trong nhiều tình huống, **Precision** và **Recall** cần được cân bằng, ví dụ: một mô hình có thể có Precision cao nhưng Recall thấp, hoặc ngược lại. Vì vậy, việc sử dụng chỉ số **F1-score**, kết hợp cả Precision và Recall, giúp đánh giá tốt hơn hiệu suất của mô hình.

