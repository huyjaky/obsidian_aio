6. **Resampling**: Là kỹ thuật dùng để thay đổi tần số biểu diễn của bộ dữ liệu time series, có thể gia tăng hoặc giảm đi tần số lấy mẫu. Ví dụ, ta có thể giảm tần số của bộ dữ liệu hiện tại từ ngày sang tháng. Điều này đồng nghĩa với việc bộ dữ liệu mới của chúng ta sẽ có ít mẫu dữ liệu hơn bản gốc.

Resampling thường hữu dụng với **time series** cho **lower** hoặc **higher frequency**. Resampling cho **lower frequency** (**downsampling**) thường liên quan tới hoạt động tổng hợp, ví dụ mức doanh thu trong tháng từ dữ liệu ngày. Resampling cho **higher frequency** (**upsampling**) ít phổ biến hơn, thường dùng trong việc nội suy. Ở đây, ta thử áp dụng **downsampling** cho bộ dữ liệu hiện tại như sau:

```python
# Specify the data columns we want to include (i.e. exclude Year, Month, Weekday Name)
data_columns = [’Consumption’, ’Wind’, ’Solar’, ’Wind+Solar’]
# Resample to weekly frequency, aggregating with mean
opsd_weekly_mean = opsd_daily[data_columns].resample(’W’).mean()
opsd_weekly_mean.head(3)
```
