from eigen_func import *
import random
from timeit import Timer

def Simpletest():

    dat =  [[3, 2, 4],
            [2, 0, 2],
            [4, 2, 3]]
    A = matrix(3,3)
    A.view(dat)
    V,D = Jac_eig(A)

    print('Is V^TAV==D?\nD=')
    D.show()
    print('V^TAV=')
    multiply(trans(V),multiply(A,V)).show()

def ntest(n,prob='A',l=None):
    A = matrix(n,n)
    for i in range(n):
        A[i,i] = random.uniform(-10,10)
        for j in range(i,n):
            c = random.uniform(-10,10)
            A[i,j] = c
            A[j,i] = c
    if prob == 'A':
        V,D = Jac_eig(A)
    elif prob == 'B':
        V,D = Jac_eig_n(A,n=l)
    
def probA():
    time = []
    size = []
    for n in range(2,20):
        size.append(n)
        print(n)
        t = Timer(lambda: ntest(n))
        time.append(t.timeit(number=3))

    a = np.array([size,time])
    a = a.T
    np.savetxt('time.txt',a,fmt=['%d','%.3e'])

def probB():
    # Simple matrix for testing
    dat = [[3, 2, 4],
           [2, 0, 2],
           [4, 2, 3]]
    B = matrix(3,3)
    B.view(dat)
    
    # Random matrox for final testing
    l = 6
    A = matrix(l,l)
    for i in range(l):
        A[i,i] = random.uniform(0,10)
        for j in range(i,l):
            c = random.uniform(0,10)
            A[i,j] = c
            A[j,i] = c
    """
    print('First {} eigenvalues:'.format(3))
    V,D = Jac_eig_n(A,n=3)
    D.show()
    print('Lowest first')
    V,D = Jac_eig_n(A)
    D.show()
    print('Highest first')
    V,D = Jac_eig_n(A)
    D.show()
    """
    tA = []
    tB1 = []
    tB2 = []
    size = []
    for n in range(2,20):
        size.append(n)
        print(n)
        t1 = Timer(lambda: ntest(n,prob='A'))
        tA.append(t1.timeit(number=3))
        t2 = Timer(lambda: ntest(n,prob='B',l=1))
        tB1.append(t2.timeit(number=3))
        t3 = Timer(lambda: ntest(n,prob='B'))
        tB2.append(t3.timeit(number=3))
    a = np.array([size,tA,tB1,tB2])
    a = a.T
    header = 'Size\tcyclic\t1_value\tall_value'
    np.savetxt('timeB.txt',a,header=header,fmt=['%d','%.3e','%.3e','%.3e'])


probB()
