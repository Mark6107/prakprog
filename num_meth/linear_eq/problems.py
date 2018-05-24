import numpy as np
from lin_eq import *

def probA1():

    dat = [[1, 1, 1],
            [0, 2, 5],
            [2, 5,-1],
            [-2,3, 4]]
    A = matrix(4,3)
    A.view(dat)
    Q,R = qr_gs_decomp(A)
    print('Is R upper triangular?')
    R.show()
    print('\nIs QTQ=1?')
    multiply(trans(Q),Q).show()
    print('\nIs QR=A?\nA=')
    A1.show()
    print('\nQR=')
    multiply(Q,R).show()


def probA2():
    
    A = matrix(3,3)
    dat =   ([[2, 1, 3],
              [2, 6, 8],
              [6, 8, 18]])
    A.view(dat)
    b = [1,3,5]
    Q,R = qr_gs_decomp(A)
    x = qr_gs_solve(Q,R,b)
    print(x)

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

probB()
