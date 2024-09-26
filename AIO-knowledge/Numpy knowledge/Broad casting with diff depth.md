```Python
import numpy as np

data = np.random.rand(32, 4)
print(data.shape)
centroids = np.random.rand(3, 4)
print(centroids.shape)
distances = np.sqrt((data[:, np.newaxis, :] - centroids) ** 2)
print(distances.shape)
```