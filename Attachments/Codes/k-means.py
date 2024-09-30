import numpy as np

X = np.array([1.4, 1, 1.5, 3.1, 3.8, 4.1]).reshape(-1, 1)  # init data

# 1. random init centroid 
k = 2
C = X[:k].reshape(1, -1)

while True:
    # 2. find distance from C and X
    DISTANCE = np.abs(X - C)
    # 3. find index belong to k clasifier
    INDEX = np.argmin(DISTANCE, axis=1)  # -> [1,0,1,0,0 ...]
    # 4. find new C with mean C old
    C_NEW = np.array(
        [X[INDEX == i].mean() for i in np.unique(INDEX)]
    )  # -> get unique object in INDEX arr
        
    # dont need give iter number beacause centroid dont change anymore
    if np.all(C_NEW == C):
        break
    C = C_NEW

print(C)
