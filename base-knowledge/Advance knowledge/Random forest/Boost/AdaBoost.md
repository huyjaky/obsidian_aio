#random-forest #tree 

## AdaBoost là gì?
-> AdaBoost là tập hợp một nhóm [[Random forest]] các [[Stump]] để giải quyết điểm yếu của [[Random forest]]: 
![[Adaboost_AIO2024.pdf#page=21&rect=50,50,878,448|Adaboost_AIO2024, p.21|800]]
-> điểm yếu của [[Random forest]] normal là tất cả các cây đề có weight bằng nhau -> dẫn đến những cây tốt bị những cây bị [[Overfitting]] và [[Underfitting]] làm cho yếu đi => toàn bộ rừng cây [[Random forest]] bị làm yếu đi

-> để giải quyết vấn đề trên thì <font color="#f79646">AdaBoost</font> ra đời:
![[Adaboost_AIO2024.pdf#page=22&rect=47,53,925,429|Adaboost_AIO2024, p.22]]
- những [[Stump]] không có weight bằng nhau trong [[Random forest]] [[Stump]] 
=> những [[Stump]] có độ lỗi cũng như bị [[Overfitting]] và [[Underfitting]] bị giảm ảnh hưởng tới toàn bộ [[Random forest]] 

## AdaBoost hoạt động như thế nào?

![[Adaboost_AIO2024.pdf#page=24&rect=11,91,802,455|Adaboost_AIO2024, p.24]]

-> vì AdaBoost sử dụng cơ chế [[Random forest boosting]] nên cây trước là tiền đề để tạo nên cây sau dẫn đến sự phụ thuộc lẫn nhau giữa các [[Stump]] 

## AdaBoost được xây dựng như thế nào?

-> chúng ta sử dụng quy trình [[GINI]] để có thể xây dựng [[Stump]] -> lấy ra được feature [[GINI]] tổng tránh xa khỏi số 0.5 nhất 

ví dụ:

![[Adaboost_AIO2024.pdf#page=30&rect=43,4,927,444|Adaboost_AIO2024, p.30]]
-> Dựa vào dữ liệu trên thì ta lấy <font color="#f79646">PATIENT WEIGHT</font> làm cây [[Stump]] gốc vì [[GINI]] tổng của nó thấp nhất so với 2 feature còn lại

1. Theo như [[Random forest boosting]] thì cây trước tạo cây sau chính vì thế nó có mối liên hệ => mỗi cây sẽ có khả năng đưa ra trọng số có thể ảnh hưởng lớn hoặc bé tới kết quả quyết định
2. <font color="#f79646">AdaBoost</font> cũng vậy sau khi tính toán xong một node thì ta phải đánh giá tiếng nói của cây đó trong việc đưa ra quyết định cuối cùng dựa vào công thức:
	- 