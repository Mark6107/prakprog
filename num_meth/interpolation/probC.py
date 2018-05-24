import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import *
import random
from scipy import interpolate

sns.set_palette('colorblind')
sns.set_color_codes(palette='colorblind')
plt.style.use('seaborn-poster')

def intex(y,h,b,c,d):
    """Integral of cubic spline, with Int(S_i) from x_i to x_i+1 substituted to h_i=x_i+1 - x_i
    Int(S_i) = y*h+1/2*b*h**2+1/3*c*h**3+1/4*d*h**4, suppresed _i on all"""
    return y*h+1/2*b*h**2+1/3*c*h**3+1/4*d*h**4

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

def cspline(x:list,y:list,z:float,res=0):
    """ Makes cubic spline of x and y to x value z, res defines whether to return spline value, differential value, or integral value"""
    n = len(x)
    h = [x[i+1]-x[i] for i in range(n-1)]
    p = [(y[i+1]-y[i])/h[i] for i in range(n-1)]
    D = [2]; Q = [1]; B = [3*p[0]];
    D += [2*h[i]/h[i+1]+2 for i in range(n-2)]
    D += [2]
    Q += [h[i]/h[i+1] for i in range(n-2)]
    B += [3*(p[i]+p[i+1]*h[i]/h[i+1]) for i in range(n-2)]
    B += [3*p[-1]]
    for i in range(1,n):
        D[i] -= Q[i-1]/D[i-1]
        B[i] -= B[i-1]/D[i-1]
    b = [0 for i in range(n)]
    b[n-1] = B[-1]/D[-1]
    for i in range(n-2,-1,-1):
        b[i]=(B[i]-Q[i]*b[i+1])/D[i];
    c = [(-2*b[i]-b[i+1]+3*p[i])/h[i] for i in range(n-1)]
    d = [(b[i]+b[i+1]-2*p[i])/h[i]/h[i] for i in range(n-1)]
    m = bise(x,z)
    yz = y[m] + b[m]*(z-x[m]) + c[m]*(z-x[m])**2 + d[m]*(z-x[m])**3
    if res==0:
        return yz
    elif res==-1:
        x = x[:m+1] + [z]
        y = y[:m+1] + [yz]
        h = h[:m] + [z-x[m]]
        s = 0
        for i in range(len(x)-1):
            s += intex(y[i],h[i],b[i],c[i],d[i])
        return s
    elif res==1:
        return b[m]+2*c[m]*(z-x[m])+3*d[m]*(z-x[m])**2
    else:
        print('Invalid task type passed...')
        return None


xt = list(range(1,11))
yt = [1,2,4,8,16,32,40,44,46,47]
zt = [min(xt)+random.random()*(max(xt)-min(xt)) for i in range(50)]
zt.sort()
st = [cspline(xt,yt,zt[i],0) for i in range(len(zt))]
dt = [cspline(xt,yt,zt[i],1) for i in range(len(zt))]
it = [cspline(xt,yt,zt[i],-1) for i in range(len(zt))]

tck = interpolate.splrep(xt,yt,s=0)
ynew = interpolate.splev(zt,tck,der=0)

figure, ax = plt.subplots(4,1,figsize=(10,18),sharex=True)
ax[0].plot(zt,st,'.r',label='Spline')
ax[0].plot(xt,yt,'.b',label='Data')
#ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].legend(numpoints=1,loc=2)
ax[0].grid()
ax[0].set_axisbelow(True)

ax[1].plot(zt,dt,'.r')
ax[1].set_ylabel('S\'(z)')
#ax[1].set_xlabel('z')
ax[1].grid()
ax[1].set_axisbelow(True)

ax[2].plot(zt,it,'.r')
#ax[2].set_xlabel('z')
ax[2].set_ylabel('Integrated value')
ax[2].grid()
ax[2].set_axisbelow(True)

ax[3].plot(zt,st-ynew,'.b')
ax[3].set_xlabel('z')
ax[3].set_ylabel('Deviation from library')
ax[3].grid()
ax[3].set_axisbelow(True)

plt.subplots_adjust(hspace=0.1)
figure.tight_layout()
figure.savefig('figC.pdf')
