9. **Deal with missing values - Deleting** Đối với phương án loại bỏ, ta có thể loại bỏ toàn bộ cột chứa nhiều giá trị null (nếu có thể) hoặc chỉ loại bỏ các hàng chứa giá trị null. Đối với xóa cột, ta thực hiện:

```python
# Use drop function to drop columns
data.drop(’Metascore’, axis=1).head()
```


Đối với xóa hàng, ta dùng: