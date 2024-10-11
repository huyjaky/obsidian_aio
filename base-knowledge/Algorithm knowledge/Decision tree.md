#Algorithm #tree 

## Decision tree là gì?
decision tree cây nhị phân dùng để đánh giá một cá thể xem nó thuộc <span style="background:#b1ffff">class (thuộc tính trong cột) </span>nào trong <span style="background:#b1ffff">feature (cột)</span> của đữ liệu

## Làm thế nào để xây dựng một cây quyết định (Decision tree)

![[Entropy]]

<span style="background:#b1ffff">-> Ở bài này ta sẽ thêm một bước nữa là công thức GINI</span>

#### Công thức GINI là gì?

-> ![[GINI]]
## Vậy làm sao để biết được đâu là node gốc cho decision tree
-> Để có thể xây dựng một cây quyết định (decision tree) thì ta phải xác định được Node gốc của nó 

trước tiên ta cần `Feature` dùng để so sánh và tính GINI tổng cho `Feature` đó với tất cả `Feature` còn lại
-> xem tổng GINI của `Feature` chính với `Feature` phụ nào là bé nhất

![[Excalidraw/GINI.excalidraw.md#^group=UXJxCvzG|GINI_root|800]]

## Trường hợp dữ liệu là dạng số chứ không phải class nữa

![[Decision tree regression]]

## Tỉa cây (prunning tree)
tỉa cây để làm gì?
-> để tránh việc overfitting do dữ liệ mới có gap quá cao 
![[Excalidraw/Decision tree regression.excalidraw.md#^group=vmfEOzlg|prunning |800]]
### làm sao để tỉa cây?
-> để tỉa cây thì ta phải tính được SSR tổng quát cho cây 
bằng cách cộng hết các SSR lại với nhau đồng thời cộng thêm hệ số $\alpha T$ 
$$\text{Tree Score} = \text{Total SSR} + \alpha T$$

$$
Total SSR = \sum_{}^{p} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$
- $\alpha$ là hệ số tự chọn để có thể optimal cây
- $T$ là số lượng nút lá
- 