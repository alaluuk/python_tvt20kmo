import numpy as np
A=np.matrix(
    [
        [1,0,2],
        [1,2,5],
        [1,5,-1]
    ]
)

B=np.matrix(
    [
        [1],
        [1],
        [22]
    ]
)

Ainv=np.linalg.inv(A)

X=Ainv*B
print(X)