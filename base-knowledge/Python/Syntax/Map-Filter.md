#Codes #python #Syntax 

#### Map
```Python
numbers = [1,2,3]

result = list(map(lambda x: x ** 2, numbers))
print(result)
```

`output`: [1,4,9]

#### Filter
```Python
numbers = [1,2,3]

result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)
```

`output`: [2]

-> map(<function>, <variable input>) 
filter(<function>, <variable input>)