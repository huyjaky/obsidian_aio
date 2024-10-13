#Codes #Syntax #python #pyspark
#### Load Data
`sparkContext.parallelize`

```Python
import spark

num_data = [1,2,3,4,5]
num_rdd = spark.sparkContext.parallelize(num_data)
```

```Python
import spark
text_data = ['Huy1',
			'huy dep train vl', 
			'pyspark is a great tool for bigg data analysis']
text_rdd = spark.sparkContext.parallelize(text_data)
```

#### RDD: map()
```Python
import spark
text_data = ['Huy1',
			'huy dep train vl', 
			'pyspark is a great tool for bigg data analysis']
			
text_rdd = spark.sparkContext.parallelize(text_data)
text_rdd2 = text_rdd.map(lambda x: (x, len(x.split(" "))))
text_rdd2.collect()
```

`output`: 
```Bash
[('Hello this is an example of Spark WordCount Example', 9),
 ('we are using PySpark', 4),
 ('PySpark is a great tool for Big Data Analysis', 9)]
```

#### RDD: filter()
```Python
import spark
num_data = [1,2,3,4,5]
			
num_rdd = spark.sparkContext.parallelize(text_data)
num_rdd2 = text_rdd.map(lambda x: x % 2 == 0)
num_rdd2.collect()
```

`output`: 
```Bash
[2,4]
```

