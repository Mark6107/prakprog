import numpy as np
from lin_eq import *

def probA1():
    print('Task A.1:\n ')
    dat = [[1, 1, 1],
            [0, 2, 5],
            [2, 5,-1],
            [-2,3, 4]]
    A = matrix(4,3)
    A.view(dat)
    print('Starting matrix')
    A.show()
    Q,R = qr_gs_decomp(A)
    print('Is R upper triangular?')
    R.show()
    print('Is QTQ=1?')
    multiply(trans(Q),Q).show()
    print('Is QR=A?\nA=')
    A.show()
    print('QR=')
    multiply(Q,R).show()


def probA2():
    print('\nTask A.2:\n')
    A = matrix(3,3)
    dat =   np.random.rand(3,3)*4
    A.view(dat)
    print('Starting matrix A:')
    A.show()
    b = np.random.rand(3,1)*3
    print('Vector b:')
    for i in range(len(b)):
        print(float(b[i]))
    Q,R = qr_gs_decomp(A)
    print('\nQ=')
    Q.show()
    print('R=')
    R.show()
    x = qr_gs_solve(Q,R,b)
    print('x=')
    for i in range(len(x)):
        print(float(x[i]))
    print('\nAx=')
    b2 = multiplyv(A,x)
    for i in range(len(b2)):
        print(float(b2[i]))
    

def probB():
    dat = [[3,0,2],
           [2,0,-2],
           [0,1,1]]
    A = matrix(3,3)
    A.view(dat)
    
    Q,R = qr_gs_decomp(A)
    B = qr_gs_inverse(Q,R)
    print('Is AB=I?')
    multiply(A,B).show()
    multiply(B,A).show()

