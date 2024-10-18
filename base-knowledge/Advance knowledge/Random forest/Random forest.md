#tree #Algorithm 

## Pipeline Random forest

-> dùng [[Bootstrap sampling]]

![[Excalidraw/Random-forest.excalidraw.md#^group=H5jjdAf9|Pretrain Random Forest | 800]]

Lưu ý:
- Vì dùng [[Bootstrap sampling]] nó random nên có thể có những sampling không được random ra và không được trainning, ta có thể dùng những sample đó để làm bộ test 
- Trong dữ liệu thực tế thì bị những sample có giá trị <font color="#f79646">nan/null</font>. Để giải quyết chúng ta có thể dùng trung bình của hàng trên và dưới

#### Chuẩn bị dữ liệu 
![[Excalidraw/Random-forest.excalidraw.md#^group=r8qh9MGj|Image2|800]]

#### Bắt đầu train từng cây
![[Excalidraw/Random-forest.excalidraw.md#^group=mJyoHKhO|Image3|500]]

#### Bước quyết định kết quả
![[Slide-Random-Forest_v2.pdf#page=39&rect=38,6,916,405|Slide-Random-Forest_v2, p.39|800]]
-> ta có Test sample cho qua từng cây chứa feature trong test sample và cho ra kết quả phân loại 

Các trường hợp:
-  <span style="background:#b1ffff">kết quả là class chiếm tỷ lệ nhiều nhất </span>
- nếu như dataset là một dãy số thì khi dùng [[Decision tree regression]] mỗi cây cho ra một dãy số và ta tính mean của tất cả các cây

---
## Các Esemple learning trong random forest
![[Random Forest_AIO2024.pdf#page=25&rect=7,8,938,457|Random Forest_AIO2024, p.25]]

#### Boosting method
![[Random Forest_AIO2024.pdf#page=27&rect=222,25,873,537|Random Forest_AIO2024, p.27]]

#### Stacking method
![[Random Forest_AIO2024.pdf#page=28&rect=169,38,898,537|Random Forest_AIO2024, p.28]]
