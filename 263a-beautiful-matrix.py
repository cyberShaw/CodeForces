import numpy as np
mat=np.zeros((5,5))

for i in range(5):
   mat[i]=input().split(" ")

for i in range(0,5):
    for j in range(0,5):
        if(mat[i][j]==1):
            x = abs(i+1-3)
            y = abs(j+1-3)
            break
print(x+y)