import numpy as np
from scipy.optimize import minimize

class interpol_1D:
    def __init__(self,n,f,data=None):
        if data==None:    
            self.data = np.random.rand(n,3)
        else:
            self.data = data
        self.n = n
        self.func = f
    def interpolate(self,x):
        y = []
        for i in range(len(x)):
            y.append(self.feed_forward(x[i]))
        return y
    def feed_forward(self,x):
        F = 0
        for i in range(self.n):
            F+= self.func((x-self.data[i][0])/self.data[i][1])*self.data[i][2]
        return F
    def trainf(self,x,vx,vy):
        F = 0
        self.data = np.reshape(x,(int(len(x)/3),3))
        for i in range(len(vx)):
            F += (self.feed_forward(vx[i])-vy[i])**2
        return F
    def train(self,vx,vy):
        x0 = [self.data[i][j] for i in range(len(self.data)) for j in range(3)]
        res = minimize(lambda x:self.trainf(x,vx,vy), x0)
        self.data = np.reshape(res.x,(int(len(res.x)/3),3))


class interpol_2D:
    def __init__(self,n,f,data=None):
        if data==None:    
            self.data = np.random.rand(n,5)
        else:
            self.data = data
        self.n = n
        self.func = f
    def interpolate(self,x,y):
        z = []
        for i in range(len(x)):
            z.append(self.feed_forward(x[i],y[i]))
        return z
    def feed_forward(self,x,y):
        F = 0
        for i in range(self.n):
            F+= self.func((x-self.data[i][0])/self.data[i][1],
                          (y-self.data[i][2])/self.data[i][3])*self.data[i][4]
        return F
    def trainf(self,x,vx,vy,vz):
        F = 0
        self.data = np.reshape(x,(int(len(x)/5),5))
        for i in range(len(vx)):
            F += (self.feed_forward(vx[i],vy[i])-vz[i])**2
        return F
    def train(self,vx,vy,vz):
        x0 = [self.data[i][j] for i in range(len(self.data)) for j in range(5)]
        res = minimize(lambda x:self.trainf(x,vx,vy,vz), x0)
        self.data = np.reshape(res.x,(int(len(res.x)/5),5))




