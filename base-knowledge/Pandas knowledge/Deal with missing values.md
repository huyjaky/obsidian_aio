9. **Deal with missing values - Deleting** Đối với phương án loại bỏ, ta có thể loại bỏ toàn bộ cột chứa nhiều giá trị null (nếu có thể) hoặc chỉ loại bỏ các hàng chứa giá trị null. Đối với xóa cột, ta thực hiện:

```python
# Use drop function to drop columns
data.drop(’Metascore’, axis=1).head()
```

Lệnh trên vẫn chưa drop data thực trên server cho tới khi ta thêm `inplace=True`.

Đối với xóa hàng, ta dùng:
```Python
data.dropna()
```

10. **Dealing with missing values - Filling**: Đối với phương án thế giá trị mới vào các ô trống, ta có thể sử dụng các giá trị mean, median... của cột dữ liệu tương ứng để thay thế (việc chọn giá trị để thay thế còn tùy thuộc vào tính chất của bộ dữ liệu, bài toán đang giải quyết...). Ví dụ, có một vài hàng có Revenue mang giá trị null, ta có thể gán cho nó giá trị trung bình như sau:

```python
revenue_mean = data_indexed[’Revenue (Millions)’].mean()
print("The mean revenue is: ", revenue_mean)

# We can fill the null values with this mean revenue
data_indexed[’Revenue (Millions)’].fillna(revenue_mean, inplace=True)
