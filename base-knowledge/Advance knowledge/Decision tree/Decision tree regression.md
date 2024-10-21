#tree #Math #regression #Algorithm #advance 

<span style="background:#b1ffff">WARNING</span>: Cần phải đọc bài [[Decision tree]] để hiểu rõ về decision tree và cách tạo lên nó

## Dữ liệu dạng số
bình thường khi xây dựng cây decision tree thì dữ liệu trông như này:
![[Extra_Decision_Tree.pdf#page=36&rect=28,79,336,401&color=important|Extra_Decision_Tree, p.36|400]]
-> dữ liệu này có các class cụ thể trong từng feature vì thế rất dễ để xây dựng cây

## nhưng nếu là dữ liệu dạng số thì sao để xây dựng cây?

![[DecisionTree_Regression_AIO2024.pdf#page=18&rect=251,156,673,331&color=important|DecisionTree_Regression_AIO2024, p.18|400]]

Ví dụ:
![[DecisionTree_Regression_AIO2024.pdf#page=24&rect=287,189,675,367&color=important|DecisionTree_Regression_AIO2024, p.24|400]]
![[DecisionTree_Regression_AIO2024.pdf#page=25&rect=144,38,645,426&color=important|DecisionTree_Regression_AIO2024, p.25|400]]
-> Dữ liệu hiệu quả của vaccince khi tiêm theo liều lượng unit(đơn vị)

để giải bài toán này ta dùng SSE (sum square error)
$$
SSE = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$
- $n$ là số lượng node cần tính 
- $y_i$ là giá trị của từng node cần tính
- $\hat{y}_i$ là giá trị trung bình của tất cả các node cần tính  

![[[Slide]-Decision-Tree_v2.pdf#page=47&rect=9,15,938,413|[Slide]-Decision-Tree_v2, p.47]]

#### Giải thích 
![[Excalidraw/Decision tree regression.excalidraw.md#^group=yLxxxaY5|Cách xác định loss SSR (summer square error) |800]]
-> nếu như chúng ta tiếp tục tính SSE tổng của các node tiếp theo thì ta được một đồ thị SSE tổng như sau:


![[DecisionTree_Regression_AIO2024.pdf#page=34&rect=172,8,808,456&color=important|DecisionTree_Regression_AIO2024, p.34|400]]
ta có thể thấy SSE (sum square error) tổng nhỏ nhất ở ngưỡng 14.5

-> vậy ta có được node gốc là tại 14.5 với SSE bé nhất
và sau đó chúng ta cho chạy ngưỡng qua hai bên 14.5 để
tìm nhánh cho SSE

Ví dụ: 
![[Excalidraw/Decision tree regression.excalidraw.md#^group=2zbHcghI|Rẻ nhánh |800]]
như vậy ta tìm được nhánh bên trái của node gốc là 11.5 và có thể dừng được 

-> ta tiếp tục đánh giá toàn bộ dữ liệu bên phải của 14.5 tức toàn bộ dữ liệu > 14.5 unit

![[DecisionTree_Regression_AIO2024.pdf#page=49&rect=159,5,951,459|DecisionTree_Regression_AIO2024, p.49]]
-> cây hoàn thiện và kết quả dự đoán khi cho một unit

#### Ví dụ về cắt nhánh (prunning tree) 
![[Excalidraw/Decision tree regression.excalidraw.md#^group=e369VFe7|Ví dụ về việc cắt nhánh |800]]

--- 
## MSE (Mean square error): 

công thức: 
$$
MSE = \frac{SSE}{n} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$
$$
SSE = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$
-> Công thức này để thay cho $SSE$ bên trên và dựa vào cái cày để xây dựng cây

| Tiêu chí                          | SSE (Sum of Squared Errors)                                          | MSE (Mean Squared Error)                                                                               |
| --------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Công thức**                     | Tổng các sai số bình phương                                          | Trung bình các sai số bình phương                                                                      |
| **Phạm vi giá trị**               | Tăng lên khi số lượng quan sát tăng                                  | Chuẩn hóa theo số lượng quan sát                                                                       |
| **Đơn vị**                        | Cùng đơn vị với biến dự đoán, nhưng không chuẩn hóa theo số quan sát | Cùng đơn vị với biến dự đoán, nhưng chuẩn hóa theo số quan sát                                         |
| **So sánh giữa các mô hình**      | Khó so sánh nếu kích thước tập dữ liệu khác nhau                     | Dễ so sánh vì được chuẩn hóa theo số lượng quan sát                                                    |
| **Ứng dụng trong cây quyết định** | Ít được sử dụng do không chuẩn hóa                                   | <span style="background:#b1ffff">Thường được dùng </span>để chọn cách phân tách trong bài toán hồi quy |
### Khi nào sử dụng SSE và MSE?

- **SSE**: Sử dụng khi bạn muốn biết tổng sai số của mô hình mà không cần phải chuẩn hóa theo kích thước tập dữ liệu.
- **MSE**: Sử dụng khi bạn cần đánh giá sai số trung bình và so sánh giữa các mô hình hoặc các tập dữ liệu có kích thước khác nhau.
