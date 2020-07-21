import numpy as np
import sys
import matplotlib.pyplot as plt
from tqdm import tqdm
x = np.array([-2,-1,0,1,2])
y = np.array([1,0.25,0,0.25,1])
print(np.polyfit(x,y,2))
x = x.reshape((5,1))
y = y.reshape((5,1))
def forward(params, x):
    return params[0]*(x**2) + params[1]*x +params[2]

params = np.zeros((3,1))
epochs = 10000
lr = 0.001
print(x.shape)
print(y.shape)
print(params.shape)
for _ in (range(epochs)):
    output = forward(params,x)
    loss = (output-y)**2
    print("\r Loss is {:.5f}".format(loss.mean()),end = "")
    term = 2*(params[0]*(x**2)+params[1]*x+params[2] - y)
    params[0] -= (np.matmul(lr*term.T,(x**2)))[0]
    params[1] -= np.matmul(lr*term.T,x)[0]
    params[2] -= np.matmul(lr*term.T,np.ones((5,1)))[0]

print()
print("parameters")
print(params)
print("Original labels")
print(y)
print("predicted output")
print(forward(params,x))