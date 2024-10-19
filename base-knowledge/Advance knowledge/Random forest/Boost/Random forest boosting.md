#advance #tree #random-forest 

![[Adaboost_AIO2024.pdf#page=4&rect=47,5,907,465|Adaboost_AIO2024, p.4]]

---
## Boosting Technique là gì?
![[Adaboost_AIO2024.pdf#page=13&rect=6,93,937,426|Adaboost_AIO2024, p.13]]

Ý tưởng ở đây là dùng bộ dữ liệu dự đoán 
sai của cây cũ bỏ vào cây mới và làm tương 
tự

-> chúng ta thay vì chia bộ dataset ra làm
nhiều phần như trong [[Boostrap sampling]]  
chúng ta chỉ cần cho cả bộ dataset (bộ 
dataset này phải là bộ dataset cho 
[[Dataset cho supervise learning]]

và khi tạo xong cây đầu thì ta tiếp tục 
chạy validate để xem cây dự đoán có đúng 
hay không và những sample mà cây này dự
đoán không đúng sẽ được gom lại và chuyển
thành đầu vào cho cây tiếp theo cho đến 
khi đã dự đoán đúng hoàn toàn
![[Adaboost_AIO2024.pdf#page=14&rect=4,98,948,397|Adaboost_AIO2024, p.14]]

