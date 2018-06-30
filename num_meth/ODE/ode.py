import numpy as np

def driver(a,b,h,yt,f,stepper,acc=1e-3,eps=1e-3,n=0):
    """
    Driver for Runge-Kutta solver
        - a: float, starting point
        - b: float, ending point
        - h: float, guessed step-size
        - yt: list, staring parameters
        - f: list, set of differential equations
        - stepper: Which stepper to use, rkstep12 or rkstep 34
        - acc: float, absolute accuracy
        - eps: float, relatice accuracy
        - n: int, current step
    """

    " Array for t values along path "
    t = np.array([a])
    " Nested array for all y(t) values "
    y_run = np.array([yt])

    " Main body "
    while b-t[-1]>1e-6:
        " Count of steps, succesful and unsuccesful " 
        n += 1; assert(n<2000)
        " Check that it doesn't go further than b "
        if t[-1]+h>b:
            h = b-t[-1]
        " Call stepper and calculate error and tolerance "
        yi,syi = stepper(t[-1],h,yt,f)
        ei = np.sqrt(np.inner(syi,syi))
        toli = (eps*np.sqrt(np.inner(yi,yi))+acc)*np.sqrt(h/(b-a))
        " Criterion for update "
        if ei<toli:
            t = np.append(t,t[-1] + h)
            yt = yi
            y_run = np.vstack((y_run,np.array([yi])))
        " Adjust h "
        h *= (toli/ei)**0.25*0.95
    return y_run,t,n

def rkstep12(t:float,h:float,yt,f):
    " Two point method calculation "
    k0 = f(t,yt)
    k1 = f(t+h,yt+h*k0)
    k = (k0+k1)/2
    
    " Updated step "
    y1 = yt + h*k
    sy1 = h*(k-k0)
    return y1,sy1

def rkstep34(t:float,h:float,yt,f):
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
