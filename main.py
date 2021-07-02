from random import random
import matplotlib.pyplot as plt
import numpy as np
from celluloid import Camera
fig = plt.figure()
n = 100  # количество х
x = []
m = 0  # мат ожидание
p = 0.8  # порядок квантили
mu = 0.2
T = 100

def ksi():
    a = 0
    for i in range(12):
        a += random()
    return a - 6

def mo(a, x):
    a += mu * (x - a)
    return a

def kv(a, x, qu):
    if (x >= a):
        a += mu * qu
    else:
        a += mu * (qu - 1)
    return a

for i in range(n):
    x.append(ksi())
q = np.quantile(x, p)
m1 = x[0]
q1 = 2
camera = Camera(fig)
for i in range(n - 1):
    plt.yticks([])
    plt.hist(x, color='yellow')
    plt.vlines(m, -n / 2, 0, color='g')
    plt.vlines(q, -n / 2, 0, color='r')
    plt.plot(m, linewidth=2)
    m1 = mo(m1, x[i])
    q1 = kv(q1, x[i], p)
    plt.plot(m1, [-n / 4], 'go')
    plt.plot([x[i]], [-n / 4], 'ko')
    plt.plot([q1], [-n / 4], 'ro')
    camera.snap()
animation = camera.animate(interval=T, repeat=True)
plt.show()
