from lin_eq import *

def newton(f,df,Hf,x0,eps=1e-6,alpha=1e-2,n=0):
    x = np.copy(np.array(x0))
    H = matrix(len(Hf(x)),len(Hf(x)[0]))
    while inner_v(df(x))>eps:
        n += 1; assert(n<1e6)
        H.view(Hf(x))
        Q,R = qr_gs_decomp(H)
        dx = np.array(qr_gs_solve(Q,R,[-i for i in df(x)]))
        lam = 1.
        while f(x+lam*dx)>f(x)+alpha*lam*dot(dx,df(x)) and lam>1/64.:
            lam /= 2.
            n+= 1
        x = x + lam*dx

    return x,n

def q_newton_broyden(f,df,x0,eps=1e-6,alpha=1e-4,n=0):
    """
    Minimum of function by Quasi-Newton method
    Gradient supplied by user.
    """
    x = np.copy(np.array(x0))
    B = matrix(len(x),len(x))
    dB = matrix(len(x),len(x))
    for i in range(len(x)):
        B[i,i] = 1
    
    while inner_v(df(x))>eps:
        assert(n<5e3)
        n += 1
        dx = np.array(multiplyv(B,-np.array(df(x))))
        lam = 1.
        dxdf = dot(dx,df(x))
        while True:
            n += 1
            lam /= 2.
            if f(x+lam*dx)<f(x)+alpha*lam*dxdf:
                break
            if lam < 1/64:
                B = matrix(len(x),len(x))
                for i in range(len(x)):
                    B[i,i] = 1
                break
        y = np.array(df(x+lam*dx))-np.array(df(x))
        u = lam*dx-np.array(multiplyv(B,y))
        c = u/dot(lam*dx,y)
        for i in range(len(c)):
            for j in range(len(dx)):
                dB[i,j] = c[i]*lam*dx[j]
        B.add(dB)
        x = x + lam*dx
    return x,n

    
