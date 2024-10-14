#python #Codes #Syntax #pyspark 

```Python
# Convert columns to appropriate data types for analysis and modeling
df_spark = df_spark.withColumn("price", col("price").cast("double")) # Price should be numeric

df_spark = df_spark.withColumn("year", col("year").cast("int")) # Year should be an integer

df_spark = df_spark.withColumn("odometer", col("odometer").cast("double")) # Odometer should be numeric

# Print the updated schema to verify data types
df_spark.printSchema()
```
-> `col(<Tên cột>).cast(<loại dữ liệu cần đổi>)`

`output`:
```Bash
root
 |-- id: string (nullable = true)
 |-- price: double (nullable = true)
 |-- year: integer (nullable = true)
 |-- manufacturer: string (nullable = true)
 |-- model: string (nullable = true)
 |-- condition: string (nullable = true)
 |-- cylinders: string (nullable = true)
 |-- fuel: string (nullable = true)
 |-- odometer: double (nullable = true)
 |-- transmission: string (nullable = true)
 |-- drive: string (nullable = true)
 |-- type: string (nullable = true)
 |-- paint_color: string (nullable = true)
 |-- state: string (nullable = true)
 |-- posting_date: string (nullable = true)
```