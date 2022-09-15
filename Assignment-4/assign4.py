

from sympy import symbols,Eq,solve
import numpy as np

#given that resultant line passes through point(2,2) and intercepts on axes whose sum is 9 (let x intercept is p (p,0) and y intercept is q (0,q) therefore,p+q=9) so, q=9-p
#let P=(p,0),Q=(0,9-p),R=(2,2)
#now we have 3 points which lies on same line so we need to find the value of p,q to find equation of the line so we find the value of p using slope(PR)=slope(RQ)

c= [1,-9,18]   # p**2-9*p+18=0
sol=np.roots(c) # with the roots of p we find p,q respectively
#now we have points P,Q,R we find equation of the line using points P(x1,y1),Q(x2,y2)
P = np.array([0,sol[0]])
Q = np.array([sol[1],0])
S = (P-Q)
print("P=",P,"Q=",Q)
#equation of a line in general form
x1=P[0]
y1=P[1]
x2=Q[0]
y2=Q[1]

A = int(x2-x1)
B = int(y2-y1)
C = int(x1*B - y1*A)
#equation of line = x(y2-y1)-y(x2-x1)-(x1(y2-y1)-y1(x2-x1))
x,y,a,b,c = symbols('x y a b c')
e = a * x - b * y - c
eq = e.subs(a,B)
eq = eq.subs(b,A)
eq = eq.subs(c,C)
print("Equation of the line in general form: ",eq)

#equation of a line in vector form = P+h(P-Q)

print("Equation of the line in Vector Form: ",P,"+h",S)

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math

def line_gen(A,B):
   len =10
   dim = A.shape[0]
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
     temp1 = A + lam_1[i]*(B-A)
     x_AB[:,i]= temp1.T
   return x_AB



#Given points
P = np.array(([3,0]))
Q = np.array(([0,6]))
R = np.array(([2,2]))


x_PQ = line_gen(P,Q)
x_PR = line_gen(P,R)
x_QR = line_gen(Q,R)

#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_PR[0,:],x_PR[1,:],label='$PR$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')

#Labeling the coordinates
tri_coords = np.vstack((P,Q,R)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q','R']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x_axis$')
plt.ylabel('$y_axis$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.title('equation of straight line')
#if using termux
#plt.savefig('/home/par.pdf')  
plt.show()
