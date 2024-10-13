#tech #Knowledge #data 

## Vậy tại sao lại cần PySpark để quản lý dữ liệu
![[PySpark.pdf#page=18&rect=23,36,936,459|PySpark, p.18]]
như chúng ta có thể thấy đây là trích đoạn của một paper về mô hình Gen hỉnh ảnh AI. Ở đây họ có đề cập là họ đã train cái mô hình này dựa trên 400M hình, nhưng họ sẽ không public mô hình cũng như là data vì 400M hình là quá lớn để họ có thể kiểm soát vì vậy trong dataset có thể chứa những bức hình độc hại làm cho poor model khiến cho hình ảnh gen ra bị độc hại và không đúng với ban đầu do mô hình học được từ dataset không được kiểm soát
-> <font color="#00b0f0">vì thế dữ liệu là một phần rất quan trọng trong việc trainning AI </font>

#### Các tools dùng để quản lý data phổ biến
![[PySpark.pdf#page=20&rect=15,37,939,457|PySpark, p.20]]
-> ở đây có những cái phổ biến ta cần quan tâm là spark, hadoop, kafka

#### Pipline của data
![[PySpark.pdf#page=21&rect=8,9,939,455|PySpark, p.21]]
- <font color="#00b0f0">Streaming Data</font>: là loại được sinh ra liên tục -> data trong mạng xã hội, web
- <font color="#00b0f0">Static Data</font>: là loại được tạo ra trước và không được sinh ra liên tục -> thông tin hàng hóa,...
#### Hadoop hoạt động như thế nào? (để so sánh với spark)
![[PySpark.pdf#page=23&rect=25,60,910,454|PySpark, p.23]]
Hadoop là một loại dữ liệu phân tán, hadoop chia data lớn thành nhiều phần data nhỏ lưu trong <span style="background:#b1ffff">ổ đĩa (disk)</span> từng máy riêng biệt và khi nào người dùng cần thì nó mới tìm máy lư trữ data người dùng cần và lấy nó ra -> tốc độ cực thấp vì lưu tại ổ đĩa
-> pipline của hadoop: 
![[PySpark.pdf#page=24&rect=117,24,852,324|PySpark, p.24]]

#### Spark hoạt động như thế nào? 
![[PySpark.pdf#page=25&rect=39,33,499,352|PySpark, p.25]]
Spark cũng giống hadoop ở chỗ là cũng chia dữ liệu ra thành nhiều phần và lưu ở từng máy riêng biệt, nhưng nó khác ở chỗ là thay vì lưu trên ổ đĩa (disk) như hadoop thì spark lại <span style="background:#b1ffff">lưu số dữ liệu đấy trên ram</span> -> tốc độ truy suất cực nhanh 

Và Spark rất linh hoạt vì nó có thể tích hợp với hầu hết các công cụ SQL thịnh hành hiện nay: 
![[PySpark.pdf#page=25&rect=493,58,933,365|PySpark, p.25]]
## Kiến trúc lõi của Spark
![[Excalidraw/Drawing 2024-10-13 09.58.28.excalidraw.md#^group=3fkPKNhA|core architechture|800]]
- <font color="#00b0f0">Resilient</font>: Khả năng giải quyết lỗi
- <font color="#00b0f0">Distributed dataset</font>: là khả năng phân tán dữ liệu ra nhiều máy tính
#### Hadoop vs Spark
![[PySpark.pdf#page=28&rect=139,27,817,405|PySpark, p.28]]

![[PySpark.pdf#page=29&rect=112,157,852,389|PySpark, p.29]]
