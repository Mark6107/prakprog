import numpy as np
from integ import *
import math

def probA():
    funcs = [lambda x: x**(1./2),lambda x: 1./np.sqrt(x),
             lambda x: np.log(x)/np.sqrt(x), lambda x: 4*np.sqrt((1-(1-x)**2))]
    desc = ['x^(1/2)','x^(-1/2)','ln(x)*x^(-1/2)','4*(1-(1-x)^2)^(1/2)']
    w = 'Testing recursive adaptive integration\nQ=Integral,E=Error,S=Recursive steps taken\n\n'
    for i in range(len(funcs)):
        w += 'f(x)={}, a=0, b=1\n'.format(desc[i])
        Q, err, steps = integ_rec(funcs[i],0,1,acc=1e-7,eps=1e-7)
        w += 'Q={} , E={}, S={}\n\n'.format(Q,err,steps)
    f = open('outA.txt','w')
    f.write(w)

def probB():
    w = 'Testing recursive adaptive integration with infinite limits\n'
    w += 'Q=Integral,E=Error,S=Recursive steps taken\n\n'
    w += 'f(x)=exp(-x^2), a=-inf, b=inf\n'
    Q, err, steps = integ_rec(lambda x: np.exp(-(x*x)),-math.inf,math.inf,acc=1e-7,eps=1e-7)
    w += 'Q={} , E={}, S={}\n\n'.format(Q,err,steps)
    w += 'f(x)=exp(-3x), a=1, b=inf\n'
    Q, err, steps = integ_rec(lambda x: np.exp(-3*x),1,math.inf,acc=1e-7,eps=1e-7)
    w += 'Q={} , E={}, S={}\n\n'.format(Q,err,steps)
    w += 'f(x)=exp(3x), a=-inf, b=-1\n'
    Q, err, steps = integ_rec(lambda x: np.exp(3*x),-math.inf,-1,acc=1e-7,eps=1e-7)
    w += 'Q={} , E={}, S={}\n\n'.format(Q,err,steps)
    f = open('outB.txt','w')
    f.write(w)
probB()
