import numpy as np
import matplotlib.pyplot as plt
from ode import *

def rv(x1,y1,x2,y2):
    " Gives the normalized r-vector divided by its size squared "
    l = ((x2-x1)**2.+(y2-y1)**2.)**(3./2)
    x = (x2-x1)/l
    y = (y2-y1)/l
    return np.array([x,y])

def orbn(t,y,m):
    " Gives the sets of coupled 1. order differential equations for n objects "
    h = np.zeros(len(m)*2)
    " Calculating object i's acceleration towards j, and vise versa "
    for i in range(len(m)):
        for j in range(i+1,len(m)):
            h1 = m[j]*rv(y[i*4],y[i*4+1],y[j*4],y[j*4+1])
            h2 = -h1*m[i]/m[j]
            h[i*2]   += h1[0]
            h[i*2+1] += h1[1]
            h[j*2]   += h2[0]
            h[j*2+1] += h2[1]
    " Collecting the output of all the differential equations "
    y1 = []
    for i in range(len(m)):
        y1.append(y[i*4+2])
        y1.append(y[i*4+3])
        y1.append(h[i*2])
        y1.append(h[i*2+1])
    return np.array(y1)

def make_y0(x,y,vx,vy):
    " Gives the ordered set of initial parameters for the differential equations "
    assert(len(x)==len(y) and len(x)==len(vx) and len(x)==len(vy))
    p = []
    for i in range(len(x)):
        p.append(x[i])
        p.append(y[i])
        p.append(vx[i])
        p.append(vy[i])
    return np.array(p)

def main():
    " Solves a system of n objects, whose only interaction is gravitation "
    " Example starts with 3 objects, but can be expanded by adding sets of initial conditions "
    " The example system is a binary system within a binary system "

    " Time interval and guessed step size "
    a = 0.
    b = 5.
    h = 0.2
    " Initial conditions for n objects"
    " x-position, y-position, x-velocity, y-velocity, mass "
    " To add an object, simply make another set of entries in these lists "
    px = [-1.55,-1.45, 0   ]
    py = [ 0   , 0   , 0   ]
    vx = [ 0   , 0   , 0   ]
    vy = [ 5/3+8 ,-5+8, -0.32   ]
    m  = [ 3   , 1   ,100  ]
    " Make single array with initial conditions "
    y0 = make_y0(px,py,vx,vy)
    print('Initializing gravitational numerical simulation of {} objects\nin the time interval t=[{}:{}].'.format(len(m),a,b))
    " Make the diff. eq. only a function of t and y "
    f = lambda t,y: orbn(t,y,m)
    " Run the 2 step solver "
    y,t,n = driver2step(a,b,h,y0,f)
    print('Simulation finished after {} steps!\nSee solution in plot.pdf!'.format(n))
    " Generating plot "
    c = ['r','b','g']; t = ''
    fig,ax = plt.subplots(1,1)
    for j in range(len(m)):
        ax.plot(y[0][j*4],y[0][j*4+1],'o'+c[j],label='Start {}'.format(j+1))
        ax.plot([y[i][j*4] for i in range(len(y))],
                [y[i][j*4+1] for i in range(len(y))],
                '-'+c[j],lw=2,alpha=0.8,label='Object {}'.format(j+1))
        t += 'm{} = {}, '.format(j+1,m[j])
    t = t[:-2]
    ax.axis('equal')
    ax.grid()
    ax.set_title(t)
    ax.set_axisbelow(True)
    ax.legend(numpoints=1)
    plt.savefig('plot.pdf')


main()
