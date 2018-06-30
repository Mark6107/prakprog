import numpy as np
import matplotlib.pyplot as plt
from ode import *

def osc(t,y,m,k):
    " Diff. eq. for harmonic oscillation "
    df = np.array([y[1],-k/m*y[0]])
    return df

def osc_fric(t,y,m,k,c):
    """ 
    Diff. eq. for harmonic oscillation with dampening.
    m = mass
    k = force constant
    c = friction constant
    """

    df = np.array([y[1],-c/m*y[1]-k/m*y[0]])   
    return df

def probAB():
    " Main body for calling the ODE-solver, which plots while varying inpu parameters "
    fig, ax = plt.subplots(2,1,sharex=True)
    " Initial conditions "
    a = 0.
    b = 10.
    h = 0.2
    yt = np.array([1,0])
    print( 'Solving oscillation with damping force:\nm x\'\' + l x\' + k x = 0,\nwith k=m=1 and varied l,\nin the interval t=[{},{}]\n\n'.format(a,b))
    
    " Loop over varied l "
    for l in np.array(range(5))/4.:
        print('Solving for l={}\n'.format(l))
        " Make the diff. eq. only a function of t and y "
        f = lambda t,y: osc_fric(t,y,1,1,l)
        y,t,n = driver(a,b,h,yt,f,rkstep34)
        print('Endpoint found after {} steps.\n\n'.format(n))
        
        " Rest is plotting "
        ax[0].plot(t,[y[i][0] for i in range(len(y))],'--',label='l={}'.format(l))
        ax[1].plot(t,[y[i][1] for i in range(len(y))],'--',label='l={}'.format(l))
    ax[0].legend(loc=3)
    ax[0].set_ylabel(r'$x(t)$')
    ax[1].set_ylabel(r'$\dot{x}(t)$')
    ax[1].set_xlabel(r'$t$')
    ax[0].grid()
    ax[0].set_axisbelow(True)
    ax[1].grid()
    ax[1].set_axisbelow(True)
    ax[0].set_title('Dampened harmonic oscillation')
    plt.subplots_adjust(hspace=0.1)
    plt.savefig('plot.pdf')
    print('Output from solutions can be seen in plot.pdf')
    print('Problem B is solved, as the saved path is used for plotting')
