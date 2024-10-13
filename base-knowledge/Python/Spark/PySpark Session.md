#Codes #pyspark #python 

![[PySpark.pdf#page=50&rect=50,21,805,456|PySpark, p.50]]

```Python
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('PySparkExample.com').getOrCreate()
```
-> Khởi động session chạy dashboard <span style="background:#b1ffff">(Bắt buộc phải chạy session trước)</span>
