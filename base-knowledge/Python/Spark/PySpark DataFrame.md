#Codes #python #pyspark #Syntax 

#### RDD to DataFrame
-> giúp quản lý dễ dàng hơn

```Python
# Creating an RDD with scores
scores = [
    ("Nguyen Van A", 10.0),
    ("Le Van Quy", 9.5),
    ("Tran Duc", 8.0),
    ("Pham Thi Nhung", 9.0)
]

# Parallelizing the scores list to create an RDD
rdd = spark.sparkContext.parallelize(scores)

# Defining the columns for the DataFrame
scoreColumns = ["name", "score"]

# Converting the RDD to a DataFrame with the specified columns
df2 = rdd.toDF(scoreColumns)

# Printing the schema of the DataFrame
df2.printSchema()

# Showing the DataFrame content without truncation
df2.show(truncate=False)
```

`output`:
```Bash
root
 |-- name: string (nullable = true)
 |-- score: double (nullable = true)

+--------------+------+
|name          |score |
+--------------+------+
|Nguyen Van A  |10.0  |
|Le Van Quy    |9.5   |
|Tran Duc      |8.0   |
|Pham Thi Nhung|9.0   |
+--------------+------+
```

