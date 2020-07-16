import matplotlib.pyplot as plt
import numpy as np

def func(XX, value, arr):
    j = 0
    ret = 0
    # ret = arr[value]
    while j <= value:
        ret = ret + (arr[j]*(XX**(value-j)))
        j+=1

    return ret 

min_order = 1 # Grau mínimo do polinômio
max_order = 10 # Grau máximo do polinômio

lim, npts = 10, 10

plt.xlim(-lim, lim)
plt.ylim(-lim, lim)
plt.grid()
pts = plt.ginput(npts)
plt.close()

pts = np.array(pts)


x = pts[:, 0]
y = pts[:, 1]

order = 1
poly_list = []
while order < min_order:
    poly_list.insert(0,x**order)
    order +=1 

while order <= max_order:
    poly_list.insert(0,x**order)
    polynomial = np.array(poly_list)

    A = np.array([np.ones(len(x))])
    A = np.concatenate((polynomial,A)).T  # Regressão 

    m = np.matmul(np.matmul(np.linalg.inv(np.matmul(A.T, A)), A.T), y)
    print(m)

    X = np.linspace(-lim, lim, 200)
    Y = func(X, order, m)

    plt.figure(order)
    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)
    plt.plot(x, y, "+")
    plt.plot(X, Y)
    plt.grid()      

    order += 1

plt.show()
