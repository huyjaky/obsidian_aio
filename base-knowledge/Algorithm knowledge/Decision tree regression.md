#tree #Math #regression #Algorithm 

<span style="background:#b1ffff">WARNING</span>: Cần phải đọc bài [[Decision tree]] để hiểu rõ về decision tree và cách tạo lên nó

## Dữ liệu dạng số
bình thường khi xây dựng cây decision tree thì dữ liệu trông như này:
![[Extra_Decision_Tree.pdf#page=36&rect=28,79,336,401&color=important|Extra_Decision_Tree, p.36|400]]
-> dữ liệu này có các class cụ thể trong từng feature vì thế rất dễ để xây dựng cây

nhưng nếu là dữ liệu dạng số thì sao để xây dựng cây?
![[DecisionTree_Regression_AIO2024.pdf#page=18&rect=251,156,673,331&color=important|DecisionTree_Regression_AIO2024, p.18|400]]

Ví dụ:
![[DecisionTree_Regression_AIO2024.pdf#page=24&rect=287,189,675,367&color=important|DecisionTree_Regression_AIO2024, p.24|400]]
![[DecisionTree_Regression_AIO2024.pdf#page=25&rect=144,38,645,426&color=important|DecisionTree_Regression_AIO2024, p.25|400]]
-> Dữ liệu hiệu quả của vaccince khi tiêm theo liều lượng unit(đơn vị)

![[Excalidraw/Decision tree regression.excalidraw.md#^group=yLxxxaY5|Cách xác định loss SSR (summer square error) |800]]
-> nếu như chúng ta tiếp tục tính SSR tổng của các node tiếp theo thì ta được một đồ thị SSR tổng như sau:
![[DecisionTree_Regression_AIO2024.pdf#page=34&rect=172,8,808,456&color=important|DecisionTree_Regression_AIO2024, p.34|400]]
ta có thể thấy SSR (sum square error) tổng nhỏ nhất ở ngưỡng 14.5

-> vậy ta có được node gốc là tại 14.5 với SSR bé nhất
và sau đó chúng ta cho chạy ngưỡng qua hai bên 14.5 để
tìm nhánh cho SSR

Ví dụ: 
![[Excalidraw/Decision tree regression.excalidraw.md#^group=2zbHcghI|Rẻ nhánh |800]]
như vậy ta tìm được nhánh bên trái của node gốc là 11.5 và có thể dừng được 

-> ta tiếp tục đánh giá toàn bộ dữ liệu bên phải của 14.5 tức toàn bộ dữ liệu > 14.5 unit