```Python
import numpy as np

data = np.random.rand(32, 4)
print(data.shape)
centroids = np.random.rand(3, 4)
print(centroids.shape)
distances = np.sqrt((data[:, np.newaxis, :] - centroids) ** 2)
print(distances.shape)
```

![[Pasted image 20240926170242.png]]

its change dim matrix from 32,4 -> 32,1,4 by data[:,np.newaxis,:] np.newaxis used for add one dimension on matrix 
and subtraction  data and centroids with 1,4 and 3,4 and after that we have 3,4 in 32 lines
