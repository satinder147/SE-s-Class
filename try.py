import numpy as np
import time


a=[]
b=[]
for i in range(1000):
    a.append([1,2,3])
for i in range(3):
    b.append([1]*1000)
c=[]
for i in range(1000):
    c.append([0]*1000)
o=time.time()
for i in range(1000):
    for j in range(1000):
        c[i][j]=0
        for k in range(3):
            c[i][j]+=a[i][k]*b[k][j]

print(c)
print(time.time()-o)


a=np.array(a)
b=np.array(b)
o=time.time()
print(np.dot(a,b))
print(time.time()-o)
