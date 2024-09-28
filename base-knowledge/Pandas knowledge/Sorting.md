## 7. Sorting Operations:
Sorting cho phép ta sắp xếp các hàng trong bảng dữ liệu theo thứ tự tăng/giảm dần dựa theo giá trị của cột nào đó trong bảng dữ liệu. Ví dụ, dựa trên kết quả groupby phần trước, ta có thể tìm top 5 đạo diễn đạt số rating trung bình cao nhất như sau:

```python
data.groupby('Director')[['Rating']].mean().sort_values(['Rating'], ascending=False).head()
