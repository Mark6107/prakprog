import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import *
import random

sns.set_palette('colorblind')
sns.set_color_codes(palette='colorblind')
plt.style.use('seaborn-poster')

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

def linterp(x:list,y:list,z:float):
    m = bise(x,z)
    p = (y[m+1]-y[m])/(x[m+1]-x[m])
    return y[m] + p*(z-x[m]),m

def linterp_integ(x:list,y:list,z:float):
    yz,m = linterp(x,y,z)
    x = x[:m+1] + [z]
    y = y[:m+1] + [yz]
    s = 0
    for i in range(len(x)-1):
        a = (y[i+1]-y[i])/(x[i+1]-x[i])
        b = y[i]-a*x[i]
        s += a/2.*(x[i+1]**2-x[i]**2) + b*(x[i+1]-x[i])
    return s

xt = list(range(1,11))
yt = [1,2,4,8,16,32,40,44,46,47]
zt = [min(xt)+random.random()*(max(xt)-min(xt)) for i in range(50)]
zt.sort()
yz = []
At = []
for i in range(len(zt)):
    yl,_ = linterp(xt,yt,zt[i])
    yz += [yl]
    Al = linterp_integ(xt,yt,zt[i])
    At += [Al]
figure, ax = plt.subplots(2,1)
ax[0].plot(zt,yz,'.r',label='Splined points')
ax[0].plot(xt,yt,'*b',label='Data')
ax[0].set_ylabel('y')
ax[0].set_xlabel('x')
ax[0].grid()
ax[0].set_axisbelow(True)
ax[0].legend(numpoints=1,loc=2)
plt.subplots_adjust(hspace=0.25)
ax[1].plot(zt,At,'.r')
ax[1].set_xlabel('z')
ax[1].set_ylabel('Integrated value')
ax[1].grid()
ax[1].set_axisbelow(True)
figure.savefig('figA.pdf')

