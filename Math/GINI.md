#Math #tree #Algorithm 

Bài được link đến để ví dụ: [[Decision tree]]

#### Tổng quan
$$ Gini(D) = 1 - \sum_{i=1}^{k} p_i^2 $$
- $p_i$ là tỷ lệ xuất hiện của một class trong đặc trưng cụ thể
	- ![[Excalidraw/GINI.excalidraw.md#^area=nBLaPiob|GINI]]
#### Độ tinh khiết là gì? 
![[Excalidraw/GINI.excalidraw.md#^group=vCxcQPVr|GINI_terminology|800]]
-> công thức GINI có tác dụng tính độ <font color="#e5b9b7">không thuần khiết </font>của dữ liệu khi chuẩn bị rẻ nhánh trong cây quyết định
![[Excalidraw/GINI.excalidraw.md#^group=ryAL7Xvf|GINI_explain|800]]

#### GINI tổng?
GINI tổng là công thức tính tổng GINI của hai nhánh chung một gốc hay nói cách khác là tổng GINI của các lần phân nhánh xem GINI có giảm hay không:
$$
Gini(Internal_j) = \sum_{k'th\ leaf=1}^{K\ leaf\ nodes} \left( \frac{count(L_k)}{count(L_1, \dots, L_k)} \right) Gini(L_k)
$$
$$ Gini(D) = 1 - \sum_{i=1}^{k} p_i^2 $$

![[Excalidraw/GINI.excalidraw.md#^group=VlyvCPgg|GINI_total|800]]

## Làm sao để quyết định đâu là node gốc cho cây Decision tree khi xây bằng GINI
-> Ta phải tính GINI tổng cho từng Feature để lấy được gini nhỏ nhất 
![[[Slide]-Decision-Tree_v2.pdf#page=23&rect=27,11,940,409|[Slide]-Decision-Tree_v2, p.23]]
-> Ở đây ta có thể thấy được rằng là khi tính Gini()
![[Excalidraw/GINI.excalidraw.md#^group=9UjEbpwkDbsIefRibufZW|gini_example|800]]

