#python  #pyspark #Codes #Syntax 

<font color="#00b0f0">Temp view</font>: là bảng tạm như trong SQL và dùng câu lệnh SQL để nạp dữ liệu vào trong bảng tạm và hiện nó ra
```Python
# Load your CSV file into a Spark DataFrame
df_csv = spark.read.csv("path_to_your_csv_file.csv", header=True)

# Create a temporary SQL view
df_csv.createOrReplaceTempView("people")

# Define your SQL query
query = '''SELECT name, sex FROM people '''

# Execute the query and store the result in df2
df2 = spark.sql(query)

# Show the result
df2.show(truncate=True)
```
