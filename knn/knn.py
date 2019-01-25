import cv2
import numpy as np
import os
from  scipy.spatial import distance


folder='cats'
f=os.listdir(folder)
cats=[]
dogs=[]
for i in f:
    print(i)
    img=cv2.imread(folder+'/'+i,0)
    img=cv2.resize(img,(100,100))
    img=img.flatten()
    img=np.reshape(img,(10000,1))
    cats.append(img)


folder='dogs'
f=os.listdir(folder)
for i in f:
    img=cv2.imread(folder+'/'+i,0)
    img=cv2.resize(img,(100,100))
    img=img.flatten()
    img=np.reshape(img,(10000,1))
    dogs.append(img)


img=cv2.imread('test.jpeg',0)

img=cv2.resize(img,(100,100))
img=img.flatten()
img=np.reshape(img,(10000,1))

cats_dist=[]
for i in range(len(cats)):
    cats_dist.append(distance.euclidean(img,cats[i]))
dogs_dist=[]
for i in range(len(dogs)):
    dogs_dist.append(distance.euclidean(img,dogs[i]))

cats_dist.sort()
dogs_dist.sort()


print(cats_dist)
print(dogs_dist)
if(cats_dist[0]<dogs_dist[0]):
    print("cat")
else:
    print("dog")
