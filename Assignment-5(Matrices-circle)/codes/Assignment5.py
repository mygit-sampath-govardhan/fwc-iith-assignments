import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import linalg as LA
import sympy
import sys
import subprocess
import shlex
sys.path.insert(0,'/sdcard/Download/iith/python/Assignment-5/CoordGeo')

#system imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#a = np.array([-1,-k])
#b = np.array([0,-k])
#r1 = sqrt(k**2 - 5)
#r2 = sqrt(k**2 - k)
#pythagoreus theorem
#r1**2 + r2**2 = np.LA.norm(a-b)
#eq = 2*(k**2)-k-6
sympy.var('k')
p = sympy.solve((2*(k**2))+1)
print("The possible values of k are",p)

### plotting ###

a = np.array([-1,-0.707])
b = np.array([0,-0.707])
c = np.array([0,-0.707])
r1 = 1
r2 = 0
#triangle
x_ab = line_gen(a,b)
x_bc = line_gen(b,c)
x_ac = line_gen(a,c)
#circle
c_one = circ_gen(a,r1)
c_two = circ_gen(b,r2)
#ploting lines
plt.plot(x_ab[0,:],x_ab[1,:])
plt.plot(x_bc[0,:],x_bc[1,:])
plt.plot(x_ac[0,:],x_ac[1,:])
#plotting circes
plt.plot(c_one[0,:],c_one[1,:],label = '$Circle-1$')
plt.plot(c_two[0,:],c_two[1,:],label = '$Circle-2$')
#labeling coordinates
tri_coords = np.vstack((a,b,c)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['C1','C2','P']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, #this is text
                  (tri_coords[0,i], tri_coords[1,i]),
                      textcoords="offset points",
                      xytext=(0,10),
                      ha='center')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.savefig('/sdcard/Download/iith/python/Assignment-5/figure.pdf')
subprocess.run(shlex.split("termux-open /sdcard/Download/iith/python/Assignment-5/figure.pdf"))
plt.show()







