#Terminology #statistics 

## Kiến thức cần biết
![[Extra_Decision_Tree.pdf#page=24&rect=32,9,939,452&color=important|Extra_Decision_Tree, p.24]]
<span style="background:#b1ffff">-> Ở đây thì các công thức tính BNN rời rạc và liên tục cần phải biết để tính ENTROPY</span>


## Tỷ lệ càng thấp giá trị càng cao (Tổng của các giá trị là ENTROPY)

$$
Value(x) = - \log_2( p(x) ) 
$$
![[Entropy.excalidraw|800]]

## Entropy trung bình

Entropy $H(X)$ của một biến ngẫu nhiên $X$ được cho bởi công thức:

$$
H(X) := - \sum_{x \in X} p(x) \log_2(p(x))
$$

### Giải thích:

- **$H(X)$**: Đại diện cho entropy, là lượng thông tin trung bình hoặc sự bất định trong hệ thống.
- **$p(x)$**: Xác suất của mỗi kết quả có thể xảy ra $x$.
- **$\log(p(x))$**: Logarithm của xác suất, đo lường lượng thông tin (hoặc độ bất ngờ) từ kết quả $x$.
- **$- \sum_{x \in X}$**: Tổng có dấu âm này lấy trung bình trọng số của thông tin trên tất cả các kết quả có thể xảy ra.

### Trực quan:

![[Extra_Decision_Tree.pdf#page=29&rect=40,8,415,310&color=important|Extra_Decision_Tree, p.29|300]]

Biểu đồ cho thấy entropy là một hàm của xác suất $p$, trong đó entropy đạt đỉnh tại $p = 0.5$ (bất định tối đa) và giảm về 0 khi $p = 0$ hoặc $p = 1$ (chắc chắn hoàn toàn).

## Vậy entropy đang đo cái gì?

![[Extra_Decision_Tree.pdf#page=31&rect=48,16,905,452&color=important|Extra_Decision_Tree, p.31]]
Như ta có thể thấy rằng nếu Entropy càng cao (<font color="#e5b9b7">max-entropy = 1</font>) thì tỷ lệ phân phối giữa vàng và đá bằng nhau
-> nếu entropy = 1
	- vàng và đá bằng nhau làm cho máy bối rối không lấy ra được vàng
-> nếu entropy = 0.01
	- vàng thấp hơn đá rất nhiều làm cho máy hiểu được lấy ra vàng vì càng ít thì càng đắt tức giá trị càng cao

-> <span style="background:#b1ffff">ta so sánh được rằng là nếu entropy càng cao thì ta lại càng không lấy ra được thứ mà ta muốn tức đặc trưng (không chắc chắn) vì có quá nhiều thứ ngoại lai làm tỷ lệ entropy quá cao</span>

## Mối quan hệ giữa hai feature bằng entropy

#### Công thức Tính Gain Thông Tin (Information Gain - IG)

Gain thông tin (IG) có thể được tính bằng công thức sau:

$$
IG = Entropy(parent) - \left[ \frac{Average}{Weighted} \right] Entropy(children)
$$

Chi tiết hơn:

$$
IG(S,F) = E(S) - \sum_{f \in F} \frac{|S_f|}{S} E(S_f)
$$
$$ E(S) = - \sum_{c \in C} p_c \log_2 p_c $$

Trong đó:
- $E(S)$ là entropy của tập hợp $S$ (tập cha).
- $S_f$ là tập con tương ứng với đặc trưng $f$.
- $|S_f|$ là kích thước của tập con $S_f$.
- $|S|$ là kích thước của toàn bộ tập hợp $S$.

Slide: ![[Extra_Decision_Tree.pdf]] Slide 36->39 tính toán ví dụ

Giải thích: ![[IG-informationGain.excalidraw|800]]