#python #pyspark #Codes #Syntax 

#### PySpark DataFrame: select()
![[PySpark.pdf#page=55&rect=559,48,875,418|PySpark, p.55]]

#### PySpark DataFrame: filter()
![[PySpark.pdf#page=56&rect=557,49,913,415|PySpark, p.56]]

#### PySpark DataFrame: groupby()
```Python
# Grouping the CSV DataFrame by the 'sex' column
df_groupby_sex = df_csv.groupBy('sex')

# Displaying the type of the grouped data
print(type(df_groupby_sex))

# Counting the number of occurrences for each group and showing the result
df_groupby_sex.count().show()
```

`output`:
```Bash
+------+-------+
|sex   |count  |
+------+-------+
|NULL  |1920   |
|female|49014  |
|male  |49066  |
+------+-------+
```

