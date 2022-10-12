import numpy as np
from sympy import Symbol,solve,diff
import matplotlib.pyplot as plt
#import sys
import subprocess
import shlex

#Gradient Descend Algorithm

x = np.linspace(-5,5,20)
o = Symbol('o')
y = o - 1/o + 2/(o - 1/o)

old_min = 0
temp_min = 15
step_size = 0.01
precision = 0.001

def f_derivative(m):
    p = diff(y,o)
    p = p.subs(o,m)
    return p


mins = []

while abs(temp_min - old_min) > precision:
    old_min = temp_min
    gradient = f_derivative(old_min)
    move = gradient * step_size
    temp_min = old_min - move
    mins.append(temp_min)

print("Local minimum occurs at {}".format(round(temp_min, 2)))
z = y.subs(o,temp_min)
print ("and the local minimum is",z)


#plotting

y = x - 1/x + 2/(x - 1/x)
B = np.array([1.98, 2.83069711913966])
O = np.array([0,0])
plt.plot(x, y, 'r', label='$y = (x - (1/x)) + (2/(x - (1/x)))$')
tri_coords = np.vstack((B, O)).T
plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = ['B', 'O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
                 (tri_coords[0, i], tri_coords[1, i]),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.legend(loc='best')
    plt.grid()
    plt.axis('equal')

plt.savefig('/sdcard/Download/iith/python/Assignment-7/figure7.pdf')
subprocess.run(shlex.split("termux-open /sdcard/Download/iith/python/Assignment-7/figure7.pdf"))
