#Codes #python #pyspark #Syntax 
#### CSV
```Python
df_csv = spark.read.csv("./people.csv", 
                        header=True, 
                        inferSchema=True)
df_csv.prinSchema()
```
- <font color="#00b0f0">inferSchema</font>: Dùng để thêm tên của các cột bị thiếu trong metadata
![[Excalidraw/PySpark.excalidraw.md#^group=euUGCNoM|inferSchema|800]]

`output`:
```Bash
root
 |-- _c0: integer (nullable = true)
 |-- person_id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- sex: string (nullable = true)
 |-- date of birth: timestamp (nullable = true)
```

#### JSON
```Python
df_json = spark.read.json("./people.json") 
```

#### TXT
```Python
df_text = spark.read.text("./text_data.txt") 
```

