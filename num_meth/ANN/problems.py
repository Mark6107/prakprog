import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from ann import *


def fit2D(x,y):
    z = np.exp(-2*(x-0.5)**2-2*(y-0.5)**2)-np.exp(-(x-1)**2-(y-0.3)**2)
    #z = 0.75*np.exp(-(9*x-2)**2/4-(9*y-2)**2/4)+0.75*np.exp(-(9*x+1)**2/49-(9*y+1)/10)+0.50*np.exp(-(9*x-7)**2/4-(9*y-3)**2/4)-0.20*np.exp(-(9*x-4)**2-(9*y-7)**2)
    return z
def f2D(x,y):
    return x*np.exp(-x*x)*y*np.exp(-y*y)

def probA():
    f = lambda x: x*np.exp(-x*x)
    fit = lambda x: np.cos(x)*np.exp(-x/5)
    a = -5.; b = 5.
    xx = np.linspace(a,b,30); yy = fit(xx)
    dat = np.ones((15,3)); x0 = np.linspace(a,b,15)
    for i in range(15):
        dat[i][0] = x0[i]
    n = 15
    inter = interpol_1D(n,f)
    inter.train(xx,yy)
    xfit = np.linspace(a,b,6)
    yfit = inter.interpolate(xfit)
    
    fig,ax = plt.subplots(1,1)
    ax.plot(xx,yy,'--r',alpha=0.5,zorder=1,label='Function to fit')
    ax.plot(xfit,yfit,'ob',zorder=2,label='Fitted points')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.legend(numpoints=1,loc=4)
    plt.savefig('plotA.pdf')
    print('Problem A:\n')
    print('Interpolating in 1D')
    print('Using activation function:')
    print('f(x) = x*exp(-x*x)\n')
    print('Number of hidden neurons: {}'.format(n))
    print('Training with {} points, and interpolating {} points.\n'.format(len(xx),len(xfit)))
    print('Graphical result shown in plotA.pdf')

def probB():
    xx = np.random.random(50); yy = np.random.random(50)
    zz = fit2D(xx,yy)
    n = 15
    dat = np.ones((n,5)); x0 = np.linspace(0,1,n); y0 = np.linspace(0,1,n)
    for i in range(n):
        dat[i][0] = x0[i]
        dat[i][2] = y0[i]

    inter = interpol_2D(n,f2D)
    inter.train(xx,yy,zz)
    xfit = np.random.random(10); yfit = np.random.random(10)
    zfit = inter.interpolate(xfit,yfit)

    xp = np.linspace(0,1,30); yp = np.linspace(0,1,30)
    xp, yp = np.meshgrid(xp,yp)
    zp = fit2D(xp,yp)
    fig = plt.figure(figsize=(10,15))
    ax2 = fig.add_subplot(212)
    ax2.plot([i+1 for i in range(len(zfit))],(zfit-fit2D(xfit,yfit)),'.r')
    ax2.set_xlabel('# of interpolated point')
    ax2.set_ylabel(r'$z_{int}-f(x,y)$')
    ax2.set_xlim([0,11])
    ax1 = fig.add_subplot(211,projection='3d')
    ax1.plot_wireframe(xp,yp,zp,cmap=cm.coolwarm,zorder=1,alpha=0.5,label=r'$f(x,y)$')
    ax1.scatter(xfit,yfit,zfit,c='k',marker='.',s=500,zorder=5,label=r'$z_{int}$')
    ax1.legend(numpoints=1)
    plt.tight_layout()
    plt.savefig('plotB.pdf')
    
    print('Problem B:\n')
    print('Interpolating in 2D.')
    print('Using activation function:')
    print('f(x) = x*exp(-x*x)*y*exp(-y*y)\n')
    print('Number of hidden neurons: {}'.format(n))
    print('Training with {} points, and interpolating {} points.\n'.format(len(xx),len(xfit)))
    print('Graphical result shown in plotB.pdf')
