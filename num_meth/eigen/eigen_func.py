import numpy as np
import copy 
from lin_eq import *
from math import *


def Jac_eig(A:matrix,eps=1e-6):
    assert(A.size1==A.size2)
    V = matrix(A.size1,A.size2)
    J = matrix(A.size1,A.size2)
    for i in range(A.size1):
        V[i,i] = 1
        J[i,i] = 1
    while sum([sum([abs(A[i,j]) for j in range(i)]) for i in range(1,A.size1)])>eps:
        for q in range(1,A.size1):
            for p in range(q):
                t = 0.5*np.arctan2(2.*A[p,q],A[q,q]-A[p,p])
                J[p,p] = cos(t); J[q,q] = cos(t)
                J[p,q] = sin(t); J[q,p] = -sin(t)
                A = multiply(trans(J),multiply(A,J))
                V = multiply(V,J)
                J[p,p] = 1; J[q,q] = 1
                J[p,q] = 0; J[q,p] = 0
    
    return V,A

def Jac_eig_n(A:matrix,n:int=None,t=False,eps=1e-10):
    if not n:
        n = A.size1
    else:
        assert(n<=A.size1)
        n += 1
    V = matrix(A.size1,A.size2)
    Vd = matrix(A.size1,A.size2)
    Ad = copy(A)
    for i in range(A.size1):
        V[i,i] = 1
        Vd[i,i] = 1
    for p in range(n-1):
        while sum([abs(A[p,j]) for j in range(p+1,A.size2)])>eps:
            for q in range(p+1,A.size1):
                if not t:
                    t = 0.5*np.arctan2(2.0*A[p,q],A[q,q]-A[p,p])
                elif t:
                    t = 0.5*(np.pi+np.arctan2(2.0*A[p,q],A[q,q]-A[p,p]))
                s = np.sin(t)
                c = np.cos(t)
                for i in range(A.size1):
                    
                    if not (i==p or i==q):
                        Ad[p,i] = c*A[p,i]-s*A[q,i]
                        Ad[i,p] = c*A[p,i]-s*A[q,i]
                        Ad[q,i] = s*A[p,i]+c*A[q,i]
                        Ad[i,q] = s*A[p,i]+c*A[q,i]
                    
                    Vd[i,p] = c*V[i,p]-s*V[i,q]
                    Vd[i,q] = s*V[i,p]+c*V[i,q]

                Ad[p,p] = c*c*A[p,p]-2.*s*c*A[p,q]+s*s*A[q,q]
                Ad[q,q] = s*s*A[p,p]+2.*s*c*A[p,q]+c*c*A[q,q]
                Ad[p,q] = s*c*(A[p,p]-A[q,q])+(c*c-s*s)*A[p,q]
                Ad[q,p] = s*c*(A[p,p]-A[q,q])+(c*c-s*s)*A[p,q]
                A = copy(Ad)
                V = copy(Vd)
    return V,A
