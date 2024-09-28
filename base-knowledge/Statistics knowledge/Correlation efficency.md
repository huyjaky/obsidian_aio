
#statistics #correlation #analysis 

**Correlation efficiency** đo lường mức độ liên hệ giữa hai biến. Mối quan hệ này có thể được xác định bằng hệ số tương quan Pearson.

# Công thức hệ số tương quan Pearson

$$
\rho_{X,Y} = \frac{\text{cov}(X, Y)}{\sigma_X \sigma_Y}
$$

Trong đó:
- $\text{cov}$ là **hiệp phương sai** (covariance)
- $\sigma_X$ là **độ lệch chuẩn** của $X$
- $\sigma_Y$ là **độ lệch chuẩn** của $Y$

Công thức cho $\text{cov}(X, Y)$ có thể được biểu diễn theo **kỳ vọng** và **trung bình**. Cụ thể:

$$
\text{cov}(X, Y) = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)]
$$

Công thức cho $\rho$ cũng có thể được viết lại như sau:

$$
\rho_{X,Y} = \frac{\mathbb{E}[(X - \mu_X)(Y - \mu_Y)]}{\sigma_X \sigma_Y}
$$

Trong đó:
- $\sigma_X$ và $\sigma_Y$ được định nghĩa như trên,
- $\mu_X$ là giá trị trung bình của $X$,
- $\mu_Y$ là giá trị trung bình của $Y$,
- $\mathbb{E}$ là **toán tử kỳ vọng** (expectation).

Công thức cho $\rho$ cũng có thể được biểu diễn theo các **khoảnh khắc chưa trung tâm**:

$$
\mu_X = \mathbb{E}[X]
$$

$$
\mu_Y = \mathbb{E}[Y]
$$

$$
\sigma_X^2 = \mathbb{E}[(X - \mathbb{E}[X])^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2
$$

$$
\sigma_Y^2 = \mathbb{E}[(Y - \mathbb{E}[Y])^2] = \mathbb{E}[Y^2] - (\mathbb{E}[Y])^2
$$

$$
\mathbb{E}[(X - \mu_X)(Y - \mu_Y)] = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]
$$

Công thức cho $\rho$ cũng có thể được viết lại như sau:

$$
\rho_{X,Y} = \frac{\mathbb{E}[XY] - \mathbb{E}[X] \mathbb{E}[Y]}{\sqrt{\mathbb{E}[X^2] - (\mathbb{E}[X])^2} \sqrt{\mathbb{E}[Y^2] - (\mathbb{E}[Y])^2}}.
$$


$$
\rho_{X,Y} = \frac{n \sum (xy) - \sum x \sum y}{\sqrt{[n \sum x^2 - (\sum x)^2][n \sum y^2 - (\sum y)^2]}}
$$

**Trong đó**:
- $n$: số lượng các cặp giá trị dữ liệu,
- $x$: giá trị của biến thứ nhất,
- $y$: giá trị của biến thứ hai,
- $\sum xy$: tổng tích các giá trị tương ứng của hai biến,
- $\sum x$: tổng các giá trị của biến thứ nhất,
- $\sum y$: tổng các giá trị của biến thứ hai,
- $\sum x^2$: tổng bình phương các giá trị của biến thứ nhất,
- $\sum y^2$: tổng bình phương các giá trị của biến thứ hai.


