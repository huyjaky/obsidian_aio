#Terminology #statistics 

## Kiến thức cần biết
![[Extra_Decision_Tree.pdf#page=24&rect=32,9,939,452&color=important|Extra_Decision_Tree, p.24]]
<span style="background:#b1ffff">-> Ở đây thì các công thức tính BNN rời rạc và liên tục cần phải biết để tính ENTROPY</span>


## Tỷ lệ càng thấp giá trị càng cao (Tổng của các giá trị là ENTROPY)

$$
Value(x) = - \log_2( P ) 
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

- **Entropy tối đa** xảy ra khi tất cả các kết quả đều có xác suất bằng nhau, cho thấy sự bất định tối đa.
- **Entropy bằng không** xảy ra khi kết quả là chắc chắn (tức không có bất định).

![[Extra_Decision_Tree.pdf#page=29&rect=40,8,415,310&color=important|Extra_Decision_Tree, p.29|300]]

Biểu đồ cho thấy entropy là một hàm của xác suất $p$, trong đó entropy đạt đỉnh tại $p = 0.5$ (bất định tối đa) và giảm về 0 khi $p = 0$ hoặc $p = 1$ (chắc chắn hoàn toàn).
