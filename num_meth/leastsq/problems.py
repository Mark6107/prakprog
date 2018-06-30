import numpy as np
import math
import matplotlib.pyplot as plt
from lmfit import Model
from least_sq import *


def one(x):
    return 1

def con(x):
    return x

def sqa(x):
    return x*x



def probA():
    print('Problem A:\nFitting dataset with linear combination of functions\n')
    x = [0.1, 1.33, 2.55, 3.78, 5, 6.22, 7.45, 8.68, 9.9]
    y = [-15.3, 0.32, 2.45, 2.75, 2.27, 1.35, 0.157, -1.23, -2.75]
    dy = [1.04, 0.594, 0.983, 0.998, 1.11, 0.398, 0.535, 0.968, 0.478]
    print('Functions:\n[log(x),1,x]\n')
    f = [math.log,one,con]
    res, dres = lqfit(x,y,dy,f)
    print('Fitted c parameters:')
    print(res)
    print('\nUnceartainties of c parameters:')
    print(dres)

def probB():
    x = [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
    y = [30, 9, 0, -15, -16.3, -11, 0.3, 18, 48]
    dy = [1, 4, 8, 2, 6, 5, 3, 3, 10]
    print('Problem B:\n\nFitting own dataset with functions:\n[x*x,x,1]\n') 
    f = [sqa,con,one]
    res, dres = lqfit(x,y,dy,f)
    print('Fitted c parameters:')
    print(res)
    print('\nUnceartainties of c parameters:')
    print(dres)
    print('\nFit can be seen in plotB.pdf')

    xx = np.linspace(-2,2,100)
    yy = res[0]*sqa(xx)+res[1]*con(xx)+res[2]*one(xx)
    yl = (res[0]-dres[0])*sqa(xx)+(res[1]-dres[1])*con(xx)+(res[2]-dres[2])*one(xx)
    yu = (res[0]+dres[0])*sqa(xx)+(res[1]+dres[1])*con(xx)+(res[2]+dres[2])*one(xx)
    
    figure,ax = plt.subplots(1,1)
    ax.errorbar(x,y,yerr=dy,fmt='.b',label='Dataset',zorder=5)
    ax.plot(xx,yy,'-r',label=r'Fit($c_k$)')
    ax.plot(xx,yl,'--k',label=r'Fit($c_k \pm \delta c_k$)')
    ax.plot(xx,yu,'--k')
    ax.grid()
    ax.set_axisbelow(True)
    plt.legend(numpoints=1)
    plt.savefig('plotB.pdf')

