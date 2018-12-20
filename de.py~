import numpy as np 
X= np.array([
    [1,-2,0,-1],
    [0,1.5,-0.5,-1],
    [-1,1,0.5,-1],
    ])
d=[-1,-1,1]
w = ([1,-1,0,0.5])
c = 0.2
    
for t in range(0,50):
    for i, x in enumerate(X):
        net=np.dot(X[i],w)
        print(net)
        if net>=0:
            o=1
        else:
            o=-1
        if(d[i]==o):
            print("same",d[i])
        else:
            print("notsame",d[i])
        r=d[i]-o
        delta_w=0.1*r*X[i]
        print(delta_w)
        w = w+ delta_w

    print(w)
for i, x in enumerate(X):
    net=np.dot(X[i],w)
    print(net)
    if net>=0:
        o=1
    else:
        o=-1
    if(d[i]==o):
        print("same",d[i])
    else:
        print("notsame",d[i])
    r=d[i]-o
    delta_w=0.1*r*X[i]
    print(delta_w)
    w = w+ delta_w
print(w)