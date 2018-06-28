import numpy as np
from integ_mc import *
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_palette('colorblind')
sns.set_color_codes(palette='colorblind')
plt.style.use('seaborn-poster')


def probAB():
    """
    Both problem A and B
    Output in out.txt and plot.pdf
    """
    # Interesting test functions
    w = 'Trying plain Monte Carlo integration with N=10^6 and following functions:\n'
    w += 'Unit sphere in radial coordinates:\nf(t,p,r)=sin(p)*r^2\n'
    sphere = lambda x: np.sin(x[1])*x[2]*x[2] # Unit sphere in radial coordinates
    a = np.array([0,0,0])
    b = np.array([2*np.pi,np.pi,1])
    res,err = plainmc(sphere,a,b,1e6)
    w += 'Actual value: 4*pi/3={}\nQ={}, E={}\n\n'.format(4*np.pi/3,res,err)
    w += 'Rectangle, f(x,y)=x^2+4y\n'
    rect = lambda x: x[0]*x[0]+4*x[1]
    a = np.array([11,14])
    b = np.array([7,10])
    w += 'a=[{},{}], b=[{},{}]\n'.format(a[0],a[1],b[0],b[1])
    res,err = plainmc(rect,a,b,1e6)
    w += 'Actual value: 1719\nQ={}, E={}\n\n'.format(res,err)
    w += 'For result from integral in exercise, see plot.pdf'

    # Test function and integration range
    f = lambda x: 1/((1-np.cos(x[0])*np.cos(x[1])*np.cos(x[2]))*np.pi**3)
    a = np.array([0,0,0])
    b = np.array([np.pi,np.pi,np.pi])
    # Arrays for appending results, and run for varying N
    result = []; error = []; N = []
    for i in range(1,9):
        res, err = plainmc(f,a,b,10**i)
        result.append(res); error.append(err); N.append(10**i)
    # Plot making and wirting out.txt
    fig,ax = plt.subplots(2,1,sharex=True)
    ax[0].semilogx(N,result,'.r',label='Found value')
    ax[0].plot([1,N[-1]],[1.393203929685,1.393203929685],'--k',alpha=0.5,label='True value')
    ax[0].set_ylabel('Result(N)')
    ax[0].legend(numpoints=1)
    ax[1].loglog(N,error,'-r',label='Estimated error')
    ax[1].loglog(N,1/np.sqrt(np.array(N)),'--k',alpha=0.5,label=r'$1/\sqrt{N}$')
    ax[1].legend()
    ax[1].set_ylabel('Error(N)')
    ax[1].set_xlabel('N')
    plt.savefig('plot.pdf')
    f = open('out.txt','w')
    f.write(w)
probAB()
