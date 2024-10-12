
## CLIP 
CLIP (Contrastive Language-Image Pretraining) huấn luyện mô hình trên một tập dữ liệu lớn gồm các cặp hình ảnh-văn bản từ Internet.


CLIP sử dụng một phương pháp học **contrastive learning** (học tương phản) giữa hình ảnh và văn bản để tạo ra các biểu diễn vector không gian tương ứng cho cả hai.

Đầu vào:
- **Hình ảnh**: 
	- Hình ảnh đầu vào được mã hóa thành các vector đặc trưng bởi một bộ mã hóa hình ảnh (image encoder).
	- **Vision Transformer (ViT)** hoặc **ResNet** 
- **Văn bản**: 
	- Câu văn bản đầu vào được mã hóa thành vector đặc trưng bởi một bộ mã hóa văn bản (text encoder).
	- **Transformer**

#### **Học tương phản (Contrastive Learning):**

- CLIP được huấn luyện với một mục tiêu học tương phản gọi là **contrastive loss**.
- Quá trình huấn luyện diễn ra trên một tập dữ liệu lớn với các cặp hình ảnh-văn bản (ví dụ như các hình ảnh được lấy từ mạng Internet kèm theo mô tả ngắn gọn).
- Mỗi cặp hình ảnh và văn bản được xử lý đồng thời qua bộ mã hóa tương ứng (image encoder và text encoder), tạo ra hai vector đại diện cho hình ảnh và văn bản.
- **Mục tiêu**: CLIP tối ưu hóa sao cho vector của các cặp hình ảnh-văn bản có liên quan sẽ gần nhau trong không gian vector, còn các cặp không liên quan sẽ cách xa nhau.
- Trong quá trình huấn luyện, CLIP sẽ có nhiều cặp hình ảnh và văn bản dương (liên quan) và âm (không liên quan). CLIP sử dụng **dot product** để đo độ tương đồng giữa các vector hình ảnh và văn bản, sau đó dùng **softmax loss** để tối ưu hóa việc kéo các cặp liên quan lại gần nhau và đẩy các cặp không liên quan ra xa.

Huy nói xong mở bút viết lên múa ví dụ nhé

**Zero-shot learning** là một kỹ thuật trong học máy mà mô hình có thể **giải quyết các tác vụ** hoặc **phân loại dữ liệu** mà **không cần phải được huấn luyện trước** trên các ví dụ của chính tác vụ đó.

**Tính năng Zero-shot của CLIP**

biến các label thành prompt sao cho tốt, ....
ảnh cx encoder 

rồi chạy luôn như bình thường



## BLIP

### Phần ảnh

Xử dụng ViT

### Phần văn bản
Chia thành 3 module chính

## Cách thức hoạt động
#### Unimodel encoder
- **Cấu trúc**:
    - Text encoder được xây dựng dựa trên kiến trúc **BERT**, nơi mà token **[CLS]** được thêm vào đầu vào văn bản.
    - Token **[CLS]** có vai trò tổng hợp thông tin từ toàn bộ câu, giúp mô hình có một đại diện cho câu đó.
- **Cách hoạt động**:
    - Khi văn bản được đưa vào, đầu vào sẽ có dạng: `[CLS] token1 token2 ... tokenN`.
    - Mô hình sẽ mã hóa cả hình ảnh và văn bản để tạo ra các representation riêng biệt, phục vụ cho các tác vụ downstream khác nhau.
#### Image-grounded text encoder
- **Cấu trúc**:
    - Trong kiến trúc này, một lớp cross-attention (CA) được chèn vào giữa lớp self-attention (SA) và mạng feed-forward (FFN) cho mỗi khối transformer trong text encoder.
    - Một token đặc biệt gọi là **[Encode]** được thêm vào văn bản đầu vào, và đầu ra của token này được sử dụng như một đại diện đa phương thức cho cặp hình ảnh-văn bản.
- **Cách hoạt động**:
    - Token **[Encode]** sẽ nhận thông tin từ cả văn bản và hình ảnh thông qua lớp cross-attention, cho phép mô hình nắm bắt các mối quan hệ giữa hình ảnh và văn bản hiệu quả hơn.
#### Image-grounded text decoder
- **Cấu trúc**:
    - Trong mô hình này, các lớp self-attention hai chiều trong text encoder được thay thế bằng các lớp causal self-attention. Điều này có nghĩa là mô hình sẽ chỉ chú ý đến các token trước nó trong quá trình sinh.
    - Một token **[Decode]** được sử dụng để chỉ định bắt đầu của một chuỗi, và một token kết thúc chuỗi cũng được sử dụng để chỉ định khi nào chuỗi kết thúc.
- **Cách hoạt động**:
    - Khi tạo ra văn bản, token **[Decode]** sẽ được đưa vào đầu vào của decoder, và quá trình sinh sẽ diễn ra dựa trên các đại diện đã được tạo ra từ encoder, cho phép mô hình sinh ra văn bản có liên quan đến hình ảnh đầu vào.

### BLIP tối ưu hóa ba mục tiêu trong quá trình huấn luyện để cải thiện khả năng hiểu và sinh ngôn ngữ dựa trên hình ảnh.

- **Một lần forward pass qua visual transformer**: Để tiết kiệm thời gian tính toán, chỉ cần thực hiện một lần forward pass qua visual transformer cho mỗi cặp hình ảnh-văn bản.
- **Ba lần forward pass qua text transformer**: Mỗi cặp hình ảnh-văn bản cần ba lần forward pass qua text transformer, trong đó các chức năng khác nhau sẽ được kích hoạt để tính toán ba loại loss khác nhau.
### **Ba loại Loss**

- **Image-Text Contrastive Loss (ITC)**:
	- Actives Unimodel encoder
    - Mục tiêu: Định hình không gian đặc trưng của visual transformer và text transformer sao cho các cặp hình ảnh-văn bản tích cực (positive
image-text pairs) (đúng) có đại diện tương tự nhau, trong khi các cặp tiêu cực (negative pairs) (sai) có đại diện khác nhau (representations). Giống như cách nói bên CLIP, tăng giảm độ tương đồnge
    - Sử dụng momentum encoder để tạo ra đặc trưng và soft labels (nhãn mềm) từ momentum encoder làm mục tiêu huấn luyện, giúp tăng cường khả năng nhận diện các cặp tích cực trong số các cặp tiêu cực.
- **Image-Text Matching Loss (ITM)**:
    - Activess (active) image-grounded text encoder.
    - Mục tiêu: Học đại diện đa phương thức cho cặp hình ảnh-văn bản (image-text mul-
timodal representation) , hiểu liên kết chi tiết giữa hình ảnh và ngôn ngữ.
    - Được xây dựng như một bài toán phân loại nhị phân, mô hình sẽ dự đoán xem cặp hình ảnh-văn bản có phải là cặp tích cực (khớp) hay tiêu cực (không khớp) dựa trên các đặc trưng đa phương thức.
    - Sử dụng chiến lược mining tiêu cực mạnh mẽ (hard negative mining) để chọn các cặp tiêu cực có độ tương đồng cao hơn trong một lô (batch) để tính toán loss, giúp cải thiện khả năng phân loại.
- **Language Modeling Loss (LM)**:
    
    - Actives image-grounded text decoder.
    - Mục tiêu: Tạo ra mô tả bằng văn bản cho hình ảnh.
    - Tối ưu hóa loss entropy chéo (cross entropy loss) để tối đa hóa xác suất của văn bản theo cách autoregressive (từng bước một).
    - Sử dụng label smoothing 0.1 trong quá trình tính toán loss, giúp mô hình có khả năng tổng quát tốt hơn trong việc chuyển đổi thông tin hình ảnh thành các chú thích mạch lạc.

## BLIP 2