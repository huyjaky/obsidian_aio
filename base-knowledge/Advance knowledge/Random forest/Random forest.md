#tree #Algorithm #random-forest #advance 

## Pipeline Random forest

-> dùng [[Boostrap sampling]]

![[Excalidraw/Random-forest.excalidraw.md#^group=H5jjdAf9|Pretrain Random Forest | 800]]

Lưu ý:
- Vì dùng [[Boostrap sampling]] nó random nên có thể có những sampling không được random ra và không được trainning, ta có thể dùng những sample đó để làm bộ test OOB (out-of-bag)
	- ![[Random Forest_AIO2024.pdf#page=47&rect=111,8,925,435|Random Forest_AIO2024, p.47|400]]
- Trong dữ liệu thực tế thì bị những sample có giá trị <font color="#f79646">nan/null</font>. Để giải quyết chúng ta có thể dùng <font color="#f79646">trung bình</font> của hàng trên và dưới 
	- ![[Random Forest_AIO2024.pdf#page=49&rect=11,43,946,409|Random Forest_AIO2024, p.49|400]]
- Ta có một cách khác để tìm null/nan value là dùng [[Proximity matrix]] (<font color="#f79646">Bình thường trong cây quyết định thì dùng cách này nhiều hơn</font>)

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

---
## Random forest giải quyết overfitting hoặc underfitting ntn?

-> <span style="background:#b1ffff">bằng cách lấy trung bình nhiều cây quyết định, làm giảm phương sai</span>

---

## Đưa dữ liệu từ Time series thành dữ liệu cho supervise learning 

![[Excalidraw/Random-forest.excalidraw.md#^group=SifvI0Mz|image4|800]]

để có thể chuyển hóa bộ dữ liệu time-series thành bộ dữ liệu supervise learning (<font color="#f79646">input và predict chung một hàng - predict là kết quả cho giây tiếp theo</font>)
Ta dùng `pandas.shift()` 
```embed
title: "Python | Pandas dataframe.shift() - GeeksforGeeks"
image: "https://media.geeksforgeeks.org/wp-content/cdn-uploads/gfg_200x200-min.png"
description: "A Computer Science portal for geeks. It contains well written, well thought and well explained computer science and programming articles, quizzes and practice/competitive programming/company interview Questions."
url: "https://www.geeksforgeeks.org/python-pandas-dataframe-shift/"
```

![[Excalidraw/Random-forest.excalidraw.md#^group=B1BAdPq7|image2|800]]

#### Đối với những loại dữ liệu kiểu này thì có có cách validation khác chứ không phải dùng [[K-fold cross-validation]] 

-> [[Time-series cross-validation]] 