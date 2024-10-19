#Algorithm #tree 

<span style="background:#b1ffff">-> code mẫu: trong mục TA-ex 8-9-2024</span>
## Decision tree là gì?
decision tree cây nhị phân dùng để đánh giá một cá thể xem nó thuộc <span style="background:#b1ffff">class (thuộc tính trong cột) </span>nào trong <span style="background:#b1ffff">feature (cột)</span> của đữ liệu

## Làm thế nào để xây dựng một cây quyết định (Decision tree)

Ta có hai cách để xây dựng một cây quyết định là :
1. [[Entropy]]
2. [[GINI]] 

#### Entropy là gì?
-> [[Entropy]]


#### Công thức GINI là gì?
-> [[GINI]]

---
## Vậy làm sao để biết được đâu là node gốc cho decision tree
-> Để có thể xây dựng một cây quyết định (decision tree) thì ta phải xác định được Node gốc của nó 

trước tiên ta cần `Feature` dùng để so sánh và tính GINI tổng cho `Feature` đó với tất cả `Feature` còn lại
-> xem tổng GINI của `Feature` chính với `Feature` phụ nào là bé nhất

![[Excalidraw/GINI.excalidraw.md#^group=UXJxCvzG|GINI_root|800]]

---

## Trường hợp dữ liệu là dạng số chứ không phải class nữa

-> [[Decision tree regression]]

---
## Tỉa cây (prunning tree)
tỉa cây để làm gì?
-> để tránh việc overfitting do dữ liệu mới có gap quá cao 
![[Excalidraw/Decision tree regression.excalidraw.md#^group=vmfEOzlg|prunning |800]]
#### làm sao để tỉa cây?
-> để tỉa cây thì ta phải tính được SSR tổng quát cho cây 
bằng cách cộng hết các SSR lại với nhau đồng thời cộng thêm hệ số $\alpha T$ 
$$\text{Tree Score} = \text{Total SSR} + \alpha T$$

$$
Total SSR = \sum_{}^{p} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$
- $\alpha$ là <font color="#00b0f0">hệ số tự chọn</font> để có thể optimal cây
- $T$ là số lượng nút lá trong cây
cách tìm Tree score:
![[DecisionTree_Regression_AIO2024.pdf#page=73&rect=3,31,916,465&color=important|DecisionTree_Regression_AIO2024, p.73]]
![[DecisionTree_Regression_AIO2024.pdf#page=74&rect=4,8,943,461&color=important|DecisionTree_Regression_AIO2024, p.74]]
như ở trên ta có thể thấy rằng là Tree score càng nhỏ càng tốt -> chúng ta tránh việc [[Overfitting]] <font color="#00b0f0">(tức học quá sát với dữ liệu làm sai lệch với dữ liệu test)</font> bằng cách prunnin tức xóa bớt nút lá 

#### Vâỵ làm sao để tìm được $\alpha$ để tìm được tree score tối ưu nhất ?

-> Dùng [[K-fold cross-validation]]
-> Chúng ta tăng từ từ $\alpha$ lên trong lúc chặt nhánh để xem tree score chỗ nào tốt nhất 
<span style="background:#ff4d4f">warning</span>: $\alpha$ quyết định tree score tức hình dáng của cây như thế nào 
![[Excalidraw/Decision tree regression.excalidraw.md#^group=LNsv09uQ|Cấu  trúc tổng quát]]
![[DecisionTree_Regression_AIO2024.pdf#page=83&rect=62,26,912,460|DecisionTree_Regression_AIO2024, p.83]]
ở đây ta đánh giá các split (tức các cây) trên từng $\alpha$ xem với $\alpha$ nào thì dẫn đến <span style="background:#b1ffff">tree score trung bình bé nhất</span> trong tất cả các tree score 
Ví dụ: 
![[DecisionTree_Regression_AIO2024.pdf#page=82&rect=6,6,951,464|DecisionTree_Regression_AIO2024, p.82]]
mũi tên màu đen đi từ trên xuống dưới 

---

## Đánh giá cây

ở đây ta dùng [[K-fold cross-validation]] để có thể đánh giá cây bằng cách chia bộ dữ liệu ra và train K lần giống như một mô hình học máy bình thường 
-> Đánh giá cây để có thể cắt tỉa cây một cách chính xác (cắt tỉa đến khi acc từ bộ test là lớn nhất)

## Advantage và disadvantage của decision tree 
![[Random Forest_AIO2024.pdf#page=10&rect=18,124,941,416|Random Forest_AIO2024, p.10]]

| **Ưu điểm**                                                                                   | **Nhược điểm**                                                                             |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Rất dễ giải thích (Bạn nghĩ có dễ hiểu hơn hồi quy tuyến tính không?)                         | Không có cùng mức độ chính xác dự đoán như một số phương pháp hồi quy và phân loại khác    |
| Giống với suy nghĩ của con người hơn (Bạn nghĩ sao về điều này?)                              | Thay đổi nhỏ trong dữ liệu có thể gây ra sự thay đổi lớn trong cây ước lượng               |
| Có thể dễ dàng xử lý các biến định tính mà không cần tạo các biến giả (Dummy variable là gì?) | Ít hiệu quả hơn trong việc dự đoán khi mục tiêu chính là dự đoán kết quả của biến liên tục |
-> <span style="background:#b1ffff">Ít hiệu quả trong những bài toán regression (Hồi quy) vì số gap khá lớn ở một bộ phận dữ liệu do tính trung bình</span>
