#random-forest #tree 

## AdaBoost là gì?
-> AdaBoost là tập hợp một nhóm [[Random forest]] các [[Stump]] để giải quyết điểm yếu của [[Random forest]]: 
![[Adaboost_AIO2024.pdf#page=21&rect=50,50,878,448|Adaboost_AIO2024, p.21|800]]
-> điểm yếu của [[Random forest]] normal là tất cả các cây đề có weight bằng nhau -> dẫn đến những cây tốt bị những cây bị [[Overfitting]] và [[Underfitting]] làm cho yếu đi => toàn bộ rừng cây [[Random forest]] bị làm yếu đi

-> để giải quyết vấn đề trên thì <font color="#f79646">AdaBoost</font> ra đời:
![[Adaboost_AIO2024.pdf#page=22&rect=47,53,925,429|Adaboost_AIO2024, p.22]]
- những [[Stump]] không có we