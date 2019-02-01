import matplotlib.pyplot as plt
import numpy as np
import sklearn.datasets

cos=[]
e=[]
np.random.seed(0)
X, y = sklearn.datasets.make_moons(200, noise=0.20)
cx=y
plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)
plt.show()
w=0
b=0
def init(s):
    global w,b
    w=np.zeros((s,1))
    b=0
    return w,b

def sigmoid(x):
    return (1/(1+np.exp(-x)))

def forward():
    z=np.dot(X,w)+b
    a=sigmoid(z)
    return a

w,b=init(X.shape[1])
print(X.shape)
print(y.shape)
y=y.reshape(200,1)
lr=0.009
def lo():
    a=forward()
    m=X.shape[0]
    cost=(-1/m)*np.sum(y*np.log(a)+(1-y)*np.log(1-a))
    dw=(1/m)*np.dot(X.T,(a-y))
    db=(1/m)*np.sum(a-y)
    return dw,db,cost

for i in range(50000):
    dw,db,cost=lo()
    cos.append(cost)
    e.append(i)
    w=w-dw*lr
    b=b-db*lr
    if(i%100==0):
        print(cost)

def pre(x):
    xP=np.dot(x,w)+b
    test=np.full(xP.shape,0.5)
    test=xP>test
    return test*1

def plot_decision_boundary():
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = pre(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z)
    plt.scatter(X[:, 0], X[:, 1], c=cx,cmap=plt.cm.Spectral)

plot_decision_boundary()
plt.title("Logistic Regression")
plt.show()
plt.plot(e,cos)
plt.show()
