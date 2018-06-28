import numpy as np

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

