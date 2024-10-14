#python #Codes #Syntax #pyspark 

#### PySpark convert type data

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

#### Filter on spark
```Python
# Filter record with invalid year

df_spark = df_spark.filter((col("year") > 1900) & (col("year") <= 2024))

df_spark.select("year").distinct().orderBy("year").show()
```
-> distinc(): tách cột được chọn ra 

`output`:
```Bash
+----+
|year|
+----+
|1901|
|1902|
|1903|
|1905|
|1909|
|1910|
|1913|
|1915|
|1916|
|1918|
|1920|
|1921|
|1922|
|1923|
|1924|
|1925|
|1926|
|1927|
|1928|
|1929|
+----+
only showing top 20 rows
```

#### Describe()

```Python
# Descriptive statistics for numeric columns

df_spark.describe(["price", "odometer", "age"]).show()
```

`output`:
```Bash
+-------+--------------------+------------------+-----------------+
|summary|               price|          odometer|              age|
+-------+--------------------+------------------+-----------------+
|  count|              425827|            421332|           425929|
|   mean|   75279.43337552574| 98224.43318807971|12.76114563694888|
| stddev|1.2197335159309383E7|214118.86783963133|9.431055628948746|
|    min|                 0.0|               0.0|                2|
|    max|       3.736928711E9|             1.0E7|              123|
+-------+--------------------+------------------+-----------------+
```