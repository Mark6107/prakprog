import numpy as np
import scipy.optimize as lib
import matplotlib.pyplot as plt
from lin_eq import *
from minima import *


def Rosf(p):
    return (1-p[0]**2)+100*(p[1]-p[0]**2)**2
def Rosdf(p):
    x =  -2+2*p[0]-400*p[0]*p[1]+400*p[0]**3
    y = 200*(p[1]-p[0]**2)
    return [x,y]
def RosH(p):
    xx = 2-400*p[1]+1200*p[0]**2
    xy = -400
    yy =  200
    yx = -400*p[0]
    return [[xx,xy],[yx,yy]]
def Himmelf(p):
    return (p[0]**2+p[1]-11)**2+(p[0]+p[1]**2-7)**2
def Himmeldf(p):
    x = 4*p[0]*(p[0]**2+p[1]-11)+2*(p[0]+p[1]**2-7) 
    y = 2*(p[0]**2+p[1]-11)+4*p[1]*(p[0]+p[1]**2-7)
    return [x,y]
def HimmelH(p):
    xx = 12*p[0]**2+4*p[1]-42
    yy = 12*p[1]**2+4*p[0]-46
    zz =  4*(p[0]+p[1])
    return [[xx,zz],[zz,yy]]
def life_f(p,t):
    return p[0]*np.exp(-t/p[1])+p[2]
def master(t,y,s,p):
    S = 0
    for i in range(len(t)):
        S += (life_f(p,t[i])-y[i])**2/(s[i]*s[i])
    return S
def masterdf(t,y,s,p):
    f = np.zeros(3)
    for i in range(len(t)):
        f[0] += 2*(life_f(p,t[i])-y[i])/(s[i]*s[i])*np.exp(-t[i]/p[1])
        f[1] += 2*(life_f(p,t[i])-y[i])/(s[i]*s[i])*p[0]*t[i]/(p[1]*p[1])*np.exp(-t[i]/p[1])
        f[2] += 2*(life_f(p,t[i])-y[i])/(s[i]*s[i])
    return f

def probA():
    x0 = [3,-1]
    x1,n1 = newton(Rosf,Rosdf,RosH,x0)
    print('Minima of Rosenbrock\'s function using A: x={},y={}'.format(x1[0],x1[1]))
    print('Steps taken: n={}\n'.format(n1))
    x0 = [-3,-3]
    x2,n2 = newton(Himmelf,Himmeldf,HimmelH,x0)
    print('Minima of Himmelblau\'s function using A: x={},y={}'.format(x2[0],x2[1]))
    print('Steps taken: n={}\n'.format(n2))

def probB1():
    probA()
    print('Problem B.1:\n')
    x0 = [4,1]
    x1,n1 = q_newton_broyden(Rosf,Rosdf,x0)
    print('Minima of Rosenbrock\'s function using B: x={},y={}'.format(x1[0],x1[1]))
    print('Steps taken: n={}\n'.format(n1))
    x0 = [-3,-3]
    x2,n2 = q_newton_broyden(Himmelf,Himmeldf,x0)
    print('Minima of Himmelblau\'s function using B: x={},y={}'.format(x2[0],x2[1]))
    print('Steps taken: n={}\n\n'.format(n2))
    print('Call to root:')
    f = open('root_out.txt','r')
    for i in range(4):
        f.readline()
    for i in range(8):
        print(f.readline())
    f.close()

def probB2():
    print('\nProblem B.2:\n')
    t,y,s = np.loadtxt('dat.txt').T
    f = lambda p: master(t,y,s,p)
    df = lambda p: masterdf(t,y,s,p)
    x0 = [1,1,1]
    x1,n1 = q_newton_broyden(f,df,x0)
    print('Fitted decay function\'s parameters:')
    print('A={}\nT={}\nB={}'.format(x1[0],x1[1],x1[2]))
    print('\nFit can be seen in plotB2.pdf')
    tt = np.linspace(0,10,100)
    fig,ax = plt.subplots(1,1)
    ax.plot(tt,life_f(x1,tt),'-b',label='Fit')
    ax.errorbar(t,y,yerr=s,fmt='.r',label='Data')
    ax.set_xlabel('t')
    ax.set_ylabel('y')
    ax.legend(numpoints=1)
    plt.savefig('plotB2.pdf')

