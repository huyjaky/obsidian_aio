#Terminology #object-model


Feed forward trong mô hình AI là một quá trình trong đó thông tin được truyền qua mạng từ các đầu vào (input) qua các tầng (layers) trung gian (còn gọi là hidden layers) và cuối cùng đến đầu ra (output), mà không có bất kỳ phản hồi (feedback) hoặc vòng lặp nào quay lại tầng trước đó. Đây là một dạng mô hình mạng nơ-ron đơn giản, đặc biệt là mạng nơ-ron nhân tạo (Artificial Neural Network - ANN) được sử dụng phổ biến.

Cơ chế này thường được sử dụng trong các mô hình học sâu (Deep Learning), đặc biệt trong mạng nơ-ron truyền thẳng (Feedforward Neural Network). Dưới đây là các bước cơ bản của feed forward:

## 1. Đầu vào (Input)
Dữ liệu từ thế giới bên ngoài được đưa vào mạng.

## 2. Truyền qua các tầng (Layers)
Dữ liệu được truyền qua từng tầng của mạng nơ-ron. Mỗi nơ-ron trong một tầng sẽ tính toán đầu ra dựa trên hàm kích hoạt (activation function).

## 3. Đầu ra (Output)
Sau khi dữ liệu đi qua tất cả các tầng, kết quả cuối cùng được đưa ra ở tầng đầu ra.

Mô hình feed forward không có cơ chế điều chỉnh thông tin từ các tầng sau về lại các tầng trước, và vì vậy nó phù hợp cho các tác vụ đơn giản như phân loại hoặc dự đoán mà không cần sự hồi tiếp.

<span style="background:#b1ffff">-> ý nói ở đây là truyền thẳng từ đầu đến cuối</span>
