import numpy as np
from lin_eq import *

def lqfit(x:list,y:list,dy:list,f:list):
    A = matrix(len(x),len(f))
    l = [y[i]/dy[i] for i in range(A.size1)]
    b = matrix(len(l),1); 
    for i in range(A.size1):
        b[i,0] = l[i]
        for k in range(A.size2):
            A[i,k] = f[k](x[i])/dy[i]


    Q,R = qr_gs_decomp(A)
    Rin = matrix(R.size1,R.size2)
    for i in range(R.size2-1,-1,-1):
        Rin[i,i] = 1/R[i,i]
        for l in range(i+1,R.size2):
            Rin[i,l] /= R[i,i]
        for j in range(i-1,-1,-1):
            for l in range(i,R.size2):
                Rin[j,i] -= R[j,i]*Rin[i,l]
    
    c = multiply(multiply(Rin,trans(Q)),b)
    sig = multiply(Rin,trans(Rin))
    c = [c[i,0] for i in range(c.size1)]
    dc = [sig[i,i] for i in range(sig.size1)]
    return  c, dc
