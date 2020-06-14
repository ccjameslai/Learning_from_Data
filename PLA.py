# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt

# Sample data
a = [(1,2,1),(2,1,1),(2,3,1),(3,2,1),(4,4,1)] # y = 1
b = [(4,0.5,-1),(5,2,-1),(6,1.5,-1),(6,3,-1),(7,1,-1)] # y = -1
c = [(1,2,1),(2,1,1),(2,3,1),(3,2,1),(4,4,1),(4,0.5,-1),(5,2,-1),(6,1.5,-1),(6,3,-1),(7,1,-1)]

# Set parametors
y_hat = 0
cnt = 0
w = np.array([-1, 1.5, -1])
w_list = []
err_cnt = 1

# PLA algorithm
while err_cnt != 0 and cnt < 20:
  err_cnt = 0
  for i in range(len(c)):
    x_1, x_2, y = c[i]
    x = np.array([1, x_1, x_2])
    w_p = [0,0,0]
    if np.dot(x, w) > 0:
      y_hat = 1
    else:
      y_hat = -1
    
    if y != y_hat:
      err_cnt += 1
      w = w + y * x
      w_p = w
      w_list.append(w_p)
      cnt += 1

# Plot the seperated line
x2=[0, 1, 2, 3, 4]
x1 = []
for w in w_list:
  c = w[0]
  a = w[1]
  b = w[2]
  temp = []
  for i in x2:
    temp.append((b*i+c)/a*-1)
  x1.append(temp)

xa= [1,2,2,3,4]
ya = [2,1,3,2,4]
xb = [4,5,6,6,7]
yb = [0.5,2, 1.5, 3, 1]
x2=[0, 1, 2, 3, 4]

plt.plot(xa, ya, '*')
plt.plot(xb, yb, '^')
plt.plot(x1[len(w_list)-1], x2, '-')





