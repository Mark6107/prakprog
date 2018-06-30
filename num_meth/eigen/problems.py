from eigen_func import *
import random
import sys
from timeit import Timer

def ntest(n,prob='A1',l=None):
    A = matrix(n,n)
    for i in range(n):
        A[i,i] = random.uniform(-10,10)
        for j in range(i,n):
            c = random.uniform(-10,10)
            A[i,j] = c
            A[j,i] = c
    if prob == 'A1':
        print('A=')
        A.show()
        V,D = Jac_eig(A)
        print('V=')
        V.show()
        print('D=')
        D.show()
        print('V^TAV=')
        multiply(trans(V),multiply(A,V)).show()
    elif prob == 'A2':
        V,D = Jac_eig(A)
    elif prob == 'B':
        V,D = Jac_eig_n(A,n=l)
    
def probA():
    print('Task A, testing cyclic sweep diagonalization:\n')
    ntest(5,prob='A1')

    time = []
    size = []
    for n in range(2,10):
        size.append(n)
        t = Timer(lambda: ntest(n,prob='A2'))
        time.append(t.timeit(number=3))
    print('Testing O(n^3):')
    for i in range(len(time)):
        print('n={:2d},\ttime={}'.format(size[i],time[i]))

def probB():
    print('Task B, testing eigenvalue-by-eigenvalue:\n')
    # Simple matrix for testing
    dat = [[3, 2, 5, 4],
           [2, 0, 1, 2],
           [5, 1, 2, 3],
           [4, 2, 3, 1]]
    B = matrix(4,4)
    B.view(dat)
    print('A=')
    B.show()
    print('From lowest eigenvalue:')
    V,D1 = Jac_eig_n(B,trans=False)
    D1.show()
    print('From highest eigenvalue:')
    B.view(dat)
    V,D2 = Jac_eig_n(B,trans=True)
    D2.show()
    print('Testing n-dimension matrix\nt1: Time for cyclic diagonalization\nt2: Time for single eigenvalue\nt3: Time for all eigenvalues')
    for n in range(2,10):
        t1 = Timer(lambda: ntest(n,prob='A2'))
        t2 = Timer(lambda: ntest(n,prob='B',l=1))
        t3 = Timer(lambda: ntest(n,prob='B'))
        print('n={:2d}\tt1={:.10f}\tt2={:.10f}\tt3={:.10f}'.format(n,
               t1.timeit(number=1),t2.timeit(number=1),t3.timeit(number=1)))


