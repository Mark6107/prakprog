import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import *
import random

sns.set_palette('colorblind')
sns.set_color_codes(palette='colorblind')
plt.style.use('seaborn-poster')

def intex(y,b,c,xi,z):
    """Analytical solution to integral of S_i(x), to avoid complicated expressions"""
    return y*z+b*(z**2/2.-xi*z)+c*(z**3/3.-xi*z**2+xi**2*z)

def bise(x:list,z:float):
    """Binary search for z in x. If no exact value, return integer of closest lower value"""
    L = 0; R = len(x)-1; F = False;
    m = floor((L+R)/2.)
    while(L<=R):
        if x[m]==z:
            break
        elif x[m]<z:
            L = m+1
        elif x[m]>z:
            R = m-1
        m = floor((L+R)/2.)
    return m

def qspline(x:list,y:list,z:float,res:int):
    p = [(y[i+1]-y[i])/(x[i+1]-x[i]) for i in range(len(x)-1)]
    c = [0]
    for i in range(len(x)-2):
        c += [(p[i+1]-p[i]-c[i]*(x[i+1]-x[i]))/(x[i+2]-x[i+1])]
    b = [p[i]-c[i]*(x[i+1]-x[i]) for i in range(len(x)-1)]
    m = bise(x,z)
    yz = y[m] + b[m]*(z-x[m])+c[m]*(z-x[m])**2
    if res==1:
        return b[m]+2*c[m]*(z-x[m])
    elif res==-1:
        x = x[:m+1] + [z]
        y = y[:m+1] + [yz]
        s = 0
        for i in range(len(x)-1):
            s += intex(y[i],b[i],c[i],x[i],x[i+1])-intex(y[i],b[i],c[i],x[i],x[i])
        return s
    elif res==0:
        return yz
    else:
        print("Invaled definition of res")
        return None



xt = list(range(1,11))
yt = [1,2,4,8,16,32,40,44,46,47]
zt = [min(xt)+random.random()*(max(xt)-min(xt)) for i in range(50)]
zt.sort()

st = [qspline(xt,yt,zt[i],res= 0) for i in range(len(zt))]
dt = [qspline(xt,yt,zt[i],res= 1) for i in range(len(zt))]
at = [qspline(xt,yt,zt[i],res=-1) for i in range(len(zt))]

figure, ax = plt.subplots(3,1,figsize=(10,12))
plt.subplots_adjust(hspace=0.3)
ax[0].plot(zt,st,'.r',label='Spline')
ax[0].plot(xt,yt,'*b',label='Data')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].legend(numpoints=1,loc=2)
ax[0].grid()
ax[0].set_axisbelow(True)

ax[1].plot(zt,dt,'.r')
ax[1].set_ylabel('S\'(z)')
ax[1].set_xlabel('z')
ax[1].grid()
ax[1].set_axisbelow(True)

ax[2].plot(zt,at,'.r')
ax[2].set_xlabel('z')
ax[2].set_ylabel('Integrated value')
ax[2].grid()
ax[2].set_axisbelow(True)

figure.savefig('figB.pdf')

