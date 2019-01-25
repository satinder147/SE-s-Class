import numpy as np
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10]
y=[2,3,4,5,8,5,4,9,7,9]

x=np.array(x)
y=np.array(y)
print(x.shape)

x=np.reshape(x,(10,1))
y=np.reshape(y,(10,1))
print(x.shape)

plt.scatter(x,y,color="r")
plt.show()

alpha=0.001
m=0
c=0
for i in range(100):
    y_pred=m*x+c
    cost=0.1*np.sum(np.square(y_pred-y))
    dm=0.1*np.sum((y_pred-y)*x)
    dc=0.1*np.sum(y_pred-y)


    m=m-alpha*dm
    c=c-alpha*dc



y_pred=m*x+c
plt.plot(x,y)
plt.plot(x,y_pred)
plt.show()
