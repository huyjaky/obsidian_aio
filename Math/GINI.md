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
<span style="background:#b1ffff">-> Gini tổng lấy hai nhánh cộng lại và độ sâu của cây là 1</span>
## Làm sao để quyết định đâu là node gốc cho cây Decision tree khi xây bằng GINI
-> Ta phải tính GINI tổng cho từng Feature để lấy được gini nhỏ nhất 
![[[Slide]-Decision-Tree_v2.pdf#page=23&rect=27,11,940,409|[Slide]-Decision-Tree_v2, p.23]]
-> Ở đây ta có thể thấy được rằng là khi tính Gini(cho Age <= 26) là min nhất và lấy Raise Salary làm mốc để xét node lá

Ví dụ: dưới đây là cách tính Gini(Likes English)
![[Excalidraw/GINI.excalidraw.md#^group=9UjEbpwkDbsIefRibufZW|gini_example|800]]

ví dụ dưới đây là Gini(Age <= 26):
![[Excalidraw/GINI.excalidraw.md#^group=uxZG8yk9NvZ5mSzBN3N9P|GIni_numb|800]]
![[Pasted image 20241014132355.png]]
- `+` = 1
- `-` = 0
-> Cứ xuống một bậc là phải tính lại gini tổng từ đầu với dữ liệu còn xót lại để xây dựng cây 