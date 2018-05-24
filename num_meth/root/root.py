from lin_eq import *
import numpy as np

def Newton_back(f,x0,dx,eps=1e-9,n=0):
    J = matrix(len(f),len(f))
    x = [i for i in x0]
    while sum([abs(f[i](x)) for i in range(len(f))])>eps:
        for i in range(len(f)):
            for k in range(len(x)):
                xv = [i for i in x]; xv[k] += dx
                J[i,k] = (f[i](xv)-f[i](x))/dx
        Q,R = qr_gs_decomp(J)
        Dx = qr_gs_solve(Q,R,[-f[j](x) for j in range(len(f))])
        lam = 2.
        while((inner_v(
            [f[j]([x[l]+lam*Dx[l] for l in range(len(x))]) for j in range(len(f))])>
            (1-lam/2)*inner_v([f[j](x) for j in range(len(f))])) and lam > 1/128.):
            lam /= 2.
            n += 1
        x = [x[k] + lam*Dx[k] for k in range(len(x))]
    return x, n

def Newton_Jacobian(f,x0,Jf,eps=1e-9,n=0):
    J = matrix(len(Jf),len(Jf[0]))
    x = [i for i in x0]
    while sum([abs(f[i](x)) for i in range(len(f))])>eps:
        for i in range(len(Jf)):
            for j in range(len(Jf[0])):
                J[i,j] = Jf[i][j](x)
        Q,R = qr_gs_decomp(J)
        Dx = qr_gs_solve(Q,R,[-f[j](x) for j in range(len(f))])
        lam = 2.
        while((inner_v(
            [f[j]([x[l]+lam*Dx[l] for l in range(len(x))]) for j in range(len(f))])>
            (1-lam/2)*inner_v([f[j](x) for j in range(len(f))])) and lam > 1/128.):
            lam /= 2.
            n += 1
        x = [x[k] + lam*Dx[k] for k in range(len(x))]
    return x, n
