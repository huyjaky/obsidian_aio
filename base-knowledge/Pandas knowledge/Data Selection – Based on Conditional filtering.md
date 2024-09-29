## 5. Data Selection – Based on Conditional filtering:
Ta có lấy các hàng trong bảng dữ liệu dựa trên một số điều kiện cần tuân theo. Ví dụ, ta mong muốn lấy các bộ phim từ 2010 tới 2015, với rating nhỏ hơn 6.0 nhưng lại có doanh thu thuộc top 5% trên toàn bộ dataset. Theo đó, ta có thể triển khai code như sau:

```python
data[((data['Year'] >= 2010) & (data['Year'] <= 2015))
      & (data['Rating'] < 6.0)
      & (data['Revenue (Millions)'] > data['Revenue (Millions)'].quantile(0.95))]
```

