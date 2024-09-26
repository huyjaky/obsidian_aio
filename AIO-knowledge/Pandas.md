Video must watch:
[How to fill null value on timeseries dataset](https://www.youtube.com/watch?v=yNQeH7bp8JM) 2:07:49

Knowledge usually use:
![[Pasted image 20240926112024.png]]

![[Pasted image 20240926112106.png]]

## 6. Groupby Operations
Groupby là một phép gom nhóm dữ liệu dựa trên một hoặc nhiều biến (ở đây là cột dữ liệu trong bảng). Ví dụ, ta có thể tìm số rating trung bình mà các đạo diễn đạt được bằng cách gom nhóm các chỉ số Rating của các bộ phim theo Director.

```python
data.groupby('Director')[['Rating']].mean().head()
