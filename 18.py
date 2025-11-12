import numpy as np

relu= lambda x: np.maximum(0, x)
sigmoid = lambda x: 1/(1+np.exp(-x))
identity = lambda x:x

def forward(x, layers, acts):
    for (w,b), act in zip(layers, acts):
        x=act(x@w+b)
    return x
x= np.array([2,3])
w1=np.array([[0,1,2],[0.5,-.5,1]])
b1=np.array([3,1,2])
w2=np.array([[0,1,],[0.5,-.5,],[2,1]])
b2=np.array([0.02])
layers=[(w1,b1),(w2,b2)]
acts=[relu,identity]
y1=forward(x,layers,acts)
print(y1)
acts=[sigmoid, sigmoid]
y2=forward(x,layers,acts)
print(y2)

