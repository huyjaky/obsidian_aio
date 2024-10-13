#Codes #python #pyspark 
#### CSV
```Python
df_csv = spark.read.csv("./people.csv", 
                        header=True, 
                        inferSchema=True)
df_csv.prinSchema()
```
- <font color="#00b0f0">inferSchema</font>: Dùng để thêm tên của các cột bị thiếu trong metadata
