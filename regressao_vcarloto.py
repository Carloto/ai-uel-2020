import matplotlib.pyplot as plt
import numpy as np


def func(XX, value, arr):
    j = 0
    ret = 0
    while j <= value:
        ret = ret + (arr[j]*(XX**(value-j)))
        j += 1

    return ret


min_order = 5  # Grau mínimo do polinômio
max_order = 10  # Grau máximo do polinômio

lim, npts = 10, 10

plt.xlim(-lim, lim)
plt.ylim(-lim, lim)
plt.grid()
pts = plt.ginput(npts)
plt.close()

pts = np.array(pts)
fig, axs = plt.subplots(-(-(max_order - (min_order-1))//2), 2)
fig.set_size_inches(11,10)
n_subplot = 0
col = 0


x = pts[:, 0]
y = pts[:, 1]

order = 1
poly_list = []
while order < min_order:
    poly_list.insert(0, x**order)
    order += 1

while order <= max_order:
    poly_list.insert(0, x**order)
    polynomial = np.array(poly_list)

    A = np.array([np.ones(len(x))])
    A = np.concatenate((polynomial, A)).T  # Regressão

    m = np.matmul(np.matmul(np.linalg.inv(np.matmul(A.T, A)), A.T), y)
    print(m)

    X = np.linspace(-lim, lim, 200)
    Y = func(X, order, m)

    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)
    axs[n_subplot, col].plot(x, y, "+")
    axs[n_subplot, col].plot(X, Y)
    axs[n_subplot, col].grid()
    axs[n_subplot, col].set_title("Grau " + str(order))

    if col == 0:
        col = 1
    else:
        col = 0
        n_subplot += 1

    order += 1

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.show()
