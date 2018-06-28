import numpy as np

def rkstep12(t,h,yt,f):
    " Two point method calculation "
    k0 = f(t,yt)
    k1 = f(t+h,yt+h*k0)
    k = (k0+k1)/2
    
    " Updated step "
    y1 = yt + h*k
    sy1 = h*(k-k0)
    return y1,sy1

def rkstep34(t,h,yt,f):
    " Fourth order "
    k0 = f(t,yt)
    k1 = f(t+0.5*h,yt+0.5*h*k0)
    k2 = f(t+0.5*h,yt+0.5*h*k1)
    k3 = f(t+h,yt+h*k2)
    khigh = k0/6+k1/3+k2/3+k3/6

    " Third order, reusing k0, and k1/2 is the same as fourth orders k1 "
    k4 = f(t+h,yt+h*k0) # k1 in third order, named k4 to avoid name-clash
    klow  = k0/6+4*k1/6+k4/6 

    " Updated step "
    y1 = yt + h*khigh
    sy1 = h*(khigh-klow)
    return y1,sy1

def mstep22(t0,yt0,t1,yt1,h,f):
    """
    Second order two step method.
        - t0: t at i-1
        - yt0: y at i-1
        - t1: t at i
        - yt1: y at i
        - h: Stepsize
        - f: Function
    """
    
    yd = f(t1,yt1)
    c = (yt0-yt1+yd*(t1-t0))*(t1-t0)**(-2)
    " Error estimate and value of next point "
    sy2 = c*h**2
    y2 = yt1 + yd*h + sy2
    return y2,sy2

def driver2step(a,b,h,yt,f,
                step1=rkstep34,step2=mstep22,acc=1e-3,eps=1e-3,n=0):
    """ 
    Driver for two-step method of differential equation solver.
        - a: Starting point
        - b: End point
        - h: Initial step-size
        - yt: Initial y-values
        - f: Function
        - step1: 1 step method for estimating first point
        - step2: 2 step method used
        - acc: Absolute precision
        - eps: Relative precision
        - n: Iteration counter
    """
    
    " Array for t values along path "
    t = np.array([a])
    " Nested array for all y(t) values "
    y_run = np.array([yt])
    
    " Make sure h<(b-a)/20, or else 2step doesn't make sense "
    if h>(b-a)/20:
        h = (b-a)/20
    " First step "
    while True:
        " Count of steps "
        n += 1; assert(n<2e3)
        " Call step1 and calculate error and tolerance "
        yi,syi = step1(t[-1],h,yt,f)
        ei = np.sqrt(np.inner(syi,syi))
        toli = (eps*np.sqrt(np.inner(yi,yi))+acc)*np.sqrt(h/(b-a))
        " Criterion for successful step "
        if ei < toli:
            t = np.append(t,t[-1]+h)
            y_run = np.vstack((y_run,np.array([yi])))
            break
        " Adjust h "
        h *= (toli/ei)**0.25*0.95
    " Main body "
    n1 = 0
    while b-t[-1]>1e-6:
        " Count of steps, n1 makes sure it is not stuck within a single step "
        n += 1; n1 += 1; assert(n1<2e3)
        " Check it doesn't go further than b "
        if t[-1]+h>b:
            h = b-t[-1]
        " Call stepper and calculate error and tolrance "
        yi, syi = step2(t[-2],y_run[-2],t[-1],y_run[-1],h,f)
        ei = np.sqrt(np.inner(syi,syi))
        toli = (eps*np.sqrt(np.inner(yi,yi))+acc)*np.sqrt(h/(b-a))
        " Criterion for successful step "
        if ei < toli:
            t = np.append(t,t[-1]+h)
            y_run = np.vstack((y_run,np.array([yi])))
            n1 = 0
        " Adjust h "
        h *= (toli/ei)**0.25*0.95

    return y_run,t,n

