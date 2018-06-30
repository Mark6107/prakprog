import numpy as np
from integ import *
import math

def probA():
    print('Problem A:\n')
    funcs = [lambda x: x**(1./2),lambda x: 1./np.sqrt(x),
             lambda x: np.log(x)/np.sqrt(x), lambda x: 4*np.sqrt((1-(1-x)**2))]
    desc = ['x^(1/2)','x^(-1/2)','ln(x)*x^(-1/2)','4*(1-(1-x)^2)^(1/2)']
    print('Testing recursive adaptive integration\nQ=Integral,E=Error,S=Recursive steps taken\n\n')
    for i in range(len(funcs)):
        print('f(x)={}, a=0, b=1'.format(desc[i]))
        Q, err, steps = integ_rec(funcs[i],0,1,acc=1e-7,eps=1e-7)
        print('Q={} , E={}, S={}\n\n'.format(Q,err,steps))

def probB():
    print('Problem B:\n')
    print('Testing recursive adaptive integration with infinite limits')
    print('Q=Integral,E=Error,S=Recursive steps taken\n')
    print('f(x)=exp(-x^2), a=-inf, b=inf')
    Q, err, steps = integ_rec(lambda x: np.exp(-(x*x)),-math.inf,math.inf,acc=1e-7,eps=1e-7)
    print('Q={} , E={}, S={}\n'.format(Q,err,steps))
    print('f(x)=exp(-3x), a=1, b=inf')
    Q, err, steps = integ_rec(lambda x: np.exp(-3*x),1,math.inf,acc=1e-7,eps=1e-7)
    print('Q={} , E={}, S={}\n'.format(Q,err,steps))
    print('f(x)=exp(3x), a=-inf, b=-1')
    Q, err, steps = integ_rec(lambda x: np.exp(3*x),-math.inf,-1,acc=1e-7,eps=1e-7)
    print('Q={} , E={}, S={}\n\n'.format(Q,err,steps))
