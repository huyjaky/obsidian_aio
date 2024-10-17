#tree #data #Terminology 
## Cây quyết định với K-fold cross-validation

---

## K-fold cross-validation là gì?

**K-fold cross-validation** là một kỹ thuật dùng để đánh giá mô hình trong học máy. Quy trình gồm các bước chính:

1. **Chia dữ liệu** thành \( K \) nhóm (folds) bằng nhau.
	-> ý ở đây là chia dữ liệu thành bộ train, validation và test để đánh giá acc của mô hình cũng như làm đa dạng khả năng học của mô hình
2. **Huấn luyện mô hình** trên \( K-1 \) nhóm và **kiểm tra** trên nhóm còn lại. Quá trình này lặp lại \( K \) lần, mỗi lần sử dụng một nhóm khác nhau làm tập kiểm tra.
3. **Tính toán độ chính xác trung bình** từ các lần kiểm tra để đánh giá tổng thể hiệu suất của mô hình.

---

## Ví dụ với Cây quyết định và K-fold cross-validation

Dưới đây là một ví dụ sử dụng mô hình **Cây quyết định** cùng với kỹ thuật **K-fold cross-validation** với \( K = 5 \).

### Bước 1: Chia tập dữ liệu thành 5 nhóm (folds)

Giả sử bạn có một tập dữ liệu nhỏ với 10 điểm dữ liệu. Sử dụng 5-fold cross-validation, bạn chia tập dữ liệu này thành 5 phần:

- Fold 1: Dùng làm tập kiểm tra ở vòng lặp 1.
- Fold 2: Dùng làm tập kiểm tra ở vòng lặp 2.
- Fold 3: Dùng làm tập kiểm tra ở vòng lặp 3.
- Fold 4: Dùng làm tập kiểm tra ở vòng lặp 4.
- Fold 5: Dùng làm tập kiểm tra ở vòng lặp 5.

### Bước 2: Huấn luyện và kiểm tra mô hình

Với mỗi vòng lặp, bạn sử dụng 4 fold để **huấn luyện mô hình cây quyết định**, và fold còn lại để **kiểm tra mô hình**:

- **Vòng 1**: Huấn luyện trên Fold 2, 3, 4, 5, kiểm tra trên Fold 1.
- **Vòng 2**: Huấn luyện trên Fold 1, 3, 4, 5, kiểm tra trên Fold 2.
- **Vòng 3**: Huấn luyện trên Fold 1, 2, 4, 5, kiểm tra trên Fold 3.
- **Vòng 4**: Huấn luyện trên Fold 1, 2, 3, 5, kiểm tra trên Fold 4.
- **Vòng 5**: Huấn luyện trên Fold 1, 2, 3, 4, kiểm tra trên Fold 5.

### Bước 3: Tính toán độ chính xác

Sau khi thực hiện 5 lần kiểm tra, ta tính trung bình của các kết quả đó để có được độ chính xác cuối cùng của mô hình.

### Mã Python (Giả định) cho ví dụ này:

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris

# Tải dữ liệu
data = load_iris()
X = data.data
y = data.target

# Mô hình cây quyết định
model = DecisionTreeClassifier()

# Sử dụng K-fold cross-validation với K=5
scores = cross_val_score(model, X, y, cv=5)

# In ra độ chính xác trung bình
print(f"Độ chính xác trung bình: {scores.mean()}")
```

