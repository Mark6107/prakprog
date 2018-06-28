import numpy as np
import sys
from multiprocessing import Process,Pool

def plainmc(f,a,b,N:int):
    """
    Function for plain Monte Carlo multi-dimensional integration.
    - f: function of singular vector
    - a: lower integral interval vector
    - b: upper integral interval vector
    - N: Integer, resolution of integral
    """
    # Volume of integral
    V = 1.
    for i in range(len(a)):
        V *= b[i]-a[i]
    # Sums of function
    sum1 = 0; sum2 = 0
    for i in range(int(N)):
        fx = f(np.random.uniform(a,b,len(a)))
        sum1 += fx
        sum2 += fx*fx
    # Average of the function and its variance
    avr = sum1/N; var = sum2/N-avr*avr
    # Return integrated value and the estimated error
    return avr*V, np.sqrt(var/N)*V


def integ_ex(N):
    print('Initializing MC-integration of\ntest-function with N=10^{}\n'.format(N))
    sys.stderr.write('Initializing for N=10^{}\n'.format(N))
    f = lambda x: 1/((1-np.cos(x[0])*np.cos(x[1])*np.cos(x[2]))*np.pi**3)
    a = np.array([0,0,0])
    b = np.array([np.pi,np.pi,np.pi])
    res,err = plainmc(f,a,b,10**N)
    print('Finalized integration with N=10^{}!\nQ={}, E={}\n'.format(N,res,err))
    sys.stderr.write('Finalized with N=10^{}!\n'.format(N))


if __name__ == '__main__':
    rang = range(3,8)
    print('Starting multiprocessing of MC-integration\nwith N=10^[{}:{}]\n'.format(rang[0],rang[-1]))
    print('This output is not real-time based, which is why the multiprocessing\ncan\'t be seen from this. To see it, run make and look at the stderr output.\n')
    with Pool(5) as p:
        p.map(integ_ex,rang)
