import numpy as np
import scipy.optimize as lib
from lin_eq import *
from math import *
from root import *
def f1(p):
    return 1e4*p[0]*p[1]-1
def f2(p):
    return np.exp(-p[0])+np.exp(-p[1])-1-1e-4
def f1x(p):
    return 1e4*p[1]-1
def f1y(p):
    return 1e4*p[0]-1
def f2x(p):
    return -np.exp(-p[0])+np.exp(-p[1])-1-1e-4
def f2y(p):
    return np.exp(-p[0])-np.exp(-p[1])-1-1e-4
def libfun_1(p):
    return [f1(p),f2(p)]
def Rosx(p):
    return -2+2*p[0]-400*p[0]*p[1]+400*p[0]**3
def Rosxx(p):
    return 2-400*p[1]+1200*p[0]**2
def Rosxy(p):
    return -400
def Rosy(p):
    return 200*(p[1]-p[0]**2)
def Rosyy(p):
    return 200
def Rosyx(p):
    return -400*p[0]
def libfun_2(p):
    return [Rosx(p),Rosy(p)]
def Himmelx(p):
    return 4*p[0]*(p[0]**2+p[1]-11)+2*(p[0]+p[1]**2-7) 
def Himmely(p):
    return 2*(p[0]**2+p[1]-11)+4*p[1]*(p[0]+p[1]**2-7)
def Himmelxx(p):
    return 12*p[0]**2+4*p[1]-42
def Himmelyy(p):
    return 12*p[1]**2+4*p[0]-46
def Himmelzz(p):
    return 4*(p[0]+p[1])
def libfun_3(p):
    return [Himmelx(p),Himmely(p)]

def probA():
    f = [f1,f2]
    x0 = [3,-1]
    dx = 1e-9
    x1,_ = Newton_back(f,x0,dx)
    print('Solution to first system: x={},y={}'.format(x1[0],x1[1]))
    f = [Rosx,Rosy]
    x0 = [10,-1]
    dx = 1e-9
    x1,_ = Newton_back(f,x0,dx)
    print('Solution to Rosenbrock\'s function: x={},y={}'.format(x1[0],x1[1]))
    f = [Himmelx,Himmely]
    x0 = [10,-1]
    dx = 1e-9
    x1,_ = Newton_back(f,x0,dx)
    print('Solution to Himmelblau\'s function: x={},y={}'.format(x1[0],x1[1]))

def probB():
    f = [f1,f2]
    J = [[f1x,f1y],[f2x,f2y]]
    x0 = [3,-1]
    dx = 1e-9
    x1,n1 = Newton_back(f,x0,dx)
    x1,n2 = Newton_Jacobian(f,x0,J)
    libres = lib.root(libfun_1,x0)
    print('Solution to first system: x={},y={}'.format(x1[0],x1[1]))
    print('Call to A: {}\nCall to B: {}\nCall to lib: {}'.format(n1,n2,libres.nfev))
    f = [Rosx,Rosy]
    J = [[Rosxx,Rosxy],[Rosyx,Rosyy]]
    x0 = [1.,400.]
    dx = 1e-9
    x1,n1 = Newton_back(f,x0,dx)
    x1,n2 = Newton_Jacobian(f,x0,J)
    libres = lib.root(libfun_2,x0)
    print('Solution to Rosenbrock\'s function: x={},y={}'.format(x1[0],x1[1]))
    print('Call to A: {}\nCall to B: {}\nCall to lib: {}'.format(n1,n2,libres.nfev))
    f = [Himmelx,Himmely]
    J = [[Himmelxx,Himmelzz],[Himmelzz,Himmelyy]]
    x0 = [-5,5]
    dx = 1e-9
    x1,n1 = Newton_back(f,x0,dx)
    x1,n2 = Newton_Jacobian(f,x0,J)
    libres = lib.root(libfun_3,x0)
    print('Solution to Himmelblau\'s function: x={},y={}'.format(x1[0],x1[1]))
    print('Call to A: {}\nCall to B: {}\nCall to lib: {}'.format(n1,n2,libres.nfev))
probB()
