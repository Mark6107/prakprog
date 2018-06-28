import numpy as np
import sys
import math
sys.setrecursionlimit(10000)

def points(a,b):
    x = np.array([1./6, 2./6, 4./6, 5./6]) # Points in scalar
    return a+(b-a)*x

def integ_rec(f,a:float,b:float,acc=1e-3,eps=1e-3):
    """
    Routine for computing integral
    of f from a to b via
    revursive adaptive integration using open
    QUADrates. For higher orders, the trapezium rule is used,
    with the rectangular rule for error estimation
    """
    F = f
    if math.isinf(a):
        if math.isinf(b):
            F = lambda t: f(t/(1-t*t))*(1+t*t)/((1-t*t)**2)
            a = -1
            b = 1
        else:
            F = lambda t: f(b-(1-t)/t)*t**(-2)
            a = 0
            b = 1
    elif math.isinf(b):
        F = lambda t: f(a+(1-t)/t)/(t*t)
        a = 0
        b = 1
    f1 = F(points(a,b)[1])
    f2 = F(points(a,b)[2])
    Q, err, steps = quad_integrate(F,a,b,f1,f2,acc,eps,steps=0)
    return Q, err, steps

def quad_integrate(f,a,b,f1,f2,acc,eps,steps):
    f0 = f(points(a,b)[0])
    f3 = f(points(a,b)[3])
    fs = np.array([f0,f1,f2,f3])

    w = np.array([2./6, 1./6, 1./6, 2./6])
    v = np.array([1./4, 1./4, 1./4, 1./4])
    
    Q = (b-a)*(w[0]*f0+w[1]*f1+w[2]*f2+w[3]*f3)
    q = (b-a)*(v[0]*f0+v[1]*f1+v[2]*f2+v[3]*f3)
    err = abs(Q-q)
    tol = acc + eps*abs(Q)

    if err<tol:
        return Q, err, steps

    else:
        ac2 = acc/np.sqrt(2)
        half = (a+b)/2.
        Q1, err1, steps1 = quad_integrate(f,a,half,f0,f1,ac2,eps,steps=steps+1)
        Q2, err2, steps2 = quad_integrate(f,half,b,f2,f3,ac2,eps,steps=steps+1)
        Q = Q1+Q2
        err = np.sqrt(err1**2+err2**2)
        steps = max(steps1,steps2)
        return Q, err, steps
