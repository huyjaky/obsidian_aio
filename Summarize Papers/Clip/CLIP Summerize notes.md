 #paper #summerize #esti
đầu tiên là ta phải hiểu CLIP nó bắt nguồn từ ý tưởng nào:
==nó bắt nguồn từ ý tưởng về sự ngược lại của model DALL-E== và dùng nó để phân loại label cho các bức ảnh

![[CLIP ideas.excalidraw|800]]

vậy ta có thể hiểu là một nhà sáng tạo nào đó đã tự hỏi là làm sao để có thể làm ngược lại từ model ==DALL-E== thì ta có một mô hình mới là ==CLIP==:

đầu tiên ta cùng xem qua biểu đồ này:
![[CLIP compatitive.excalidraw|800]]

ta có thể thấy là khi sử dụng ==CLIP== thì lượng ==Aurgmentation== càng lớn thì độ chính xác của ![[Zero-shot classifier accuracy]] càng cao

<span style="background:#b1ffff">pipline of CLIP</span>
![[CLIP pipeline.excalidraw|800]]

![[Pasted image 20240927204526.png]]

## Vậy lợi ích ở đây là gì?

1. Tránh việc gộp một đống label lại vào một chỗ
	1. VD: ở đây ta đánh label cho một con chó -> nó sẽ bị mất nhiều label như chó già, chó trẻ, chó khỏe, chó đẹp, ...
	2. <span style="background:#affad1">-> để tránh điều đó thì ta thử từng text đi kèm với bức ảnh để tránh việc đó xảy ra</span>

3. <span style="background:#affad1">Không cần </span><span style="background:#affad1">pre-training phức tạp</span> vì ở đây khi ta cào dữ liệu về thì bắc buộc nó phải đi kèm với tên của bức ảnh đó rồi

## Khả năng mở rộng của CLIP với những mô hình ResNet
![[Pasted image 20240928082219.png]]

