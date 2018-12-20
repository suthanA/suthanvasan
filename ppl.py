import numpy as np 
X= np.array([[1,-2,0,-1],[0,1.5,-0.5,-1],[-1,1,0.5,-1]])

w1 = ([1,-1,0,0.5])
d=[-1,-1,1]
def perceptron(X, w1):
    w = np.zeros(len(X[0]))
    c = 0.1
    

    for t in range(2):
        for i, x in enumerate(X):
            if (np.dot(X[i], w)*w1[i]) <= 0:
                w = w + c*X[i]*w1[i]

    return w

w = perceptron(X,w1)
print(w)