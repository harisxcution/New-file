import numpy as np
x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[0],[0],[1]])
def sigmoid(x):
    return 1/1+ exp(-x)

def derivative_sigmoid(x):
    return x*(1-x)

np.random.seed(1)
w=np.random.rand(2,1)
b = np.random.rand(1)
lr=0.05
for epoch in range(5000):
    z=np.dot(x,w)+b
    output=sigmoid(x)
    error=y-output
    d_output=error*derivative_sigmoid(output)
    w+=np.dot(x.T,d_output) * lr
    b += np.sum(d_output)

print(y)
print(np.random(output,3))
