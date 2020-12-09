import numpy as np

J = 1.0
h = 0.6
k = int(np.ceil(2.*J/h))
p1 = 0.5
p2 = 0
p3 = 1 - p1 - p2
X = np.zeros((2*k, 2*k))
X[0,0] = p1+p2
X[0,2*k-1] = p1
X[0,1] = p1
for i in np.arange(1,k-1,1):
    X[i,i-1] = p3
    X[i,i] = p2
    X[i, i+1] = p1
X[k-1,k-2] = p3
X[k-1,k-1] = p2
X[k, k-1] = p1

X[k,k]=p2+p3
X[k,k+1] = p3
for i in np.arange(k+1,2*k-1,1):
    X[i,i-1] = p1
    X[i,i] = p2
    X[i, i+1] = p3
X[2*k-1, 2*k-2] = p1
X[2*k-1, 2*k-1] = p2
print(X)
print(np.sort(np.abs(np.linalg.eig(X)[0])))
print(2*np.sqrt(p1-p1*p1)*np.cos(np.pi/(k+1)))


