import numpy as np
import matplotlib.pyplot as plt
import array
import random


class matrix(object):
    " Class for matrix objects "
    def __init__ (self,n:int,m:int,t:type='d'):
        """ 
        Initialize matrix object 
            - n: Number of rows
            - m: Number of columns
            - t: Data type
        """
        self.size1=n; self.size2=m
        self.data=array.array(t,[0.0]*(n*m))

    def set(self,i:int,j:int,x):
        " Set matrix element i,j "
        self.data[i+self.size1*j]=x

    def get(self,i:int,j:int):
        " Get matrix element i,j "
        return self.data[i+self.size1*j]

    def row(self,i):
        " Get row i "
        return [self.data[i+self.size1*j] for j in range(self.size2)]

    def col(self,j):
        " Get column j "
        return [self.data[i+self.size1*j] for i in range(self.size1)]

    def view(self,M):
        " Set all matrix elements with nested list "
        for i in range(self.size1):
            for j in range(self.size2):
                self.data[i+self.size1*j] = M[i][j]

    def show(self):
        " Print matrix to stdout "
        main = ''
        for i in range(self.size1):
            for j in range(self.size2):
                main += '{:.3f}'.format(self.data[i+self.size1*j]) + '\t'
            main += '\n'
        print(main)

    def __getitem__ (self,ij):
        " Return element i,j "
        i,j=ij; return self.get(i,j)

    def __setitem__(self,ij,x):
        " Set element i,j "
        i,j=ij; self.set(i,j,x)

def copy(A):
    " Copy matrix A "
    B = matrix(A.size1,A.size2)
    for i in range(A.size1):
        for j in range(A.size2):
            B[i,j] = A[i,j]
    return B

def multiply(A:matrix,B:matrix):
    " Multiply two matrixes "
    C = matrix(A.size1,B.size2)
    for i in range(C.size1):
        for j in range(C.size2):
            C[i,j] = sum([A[i,l]*B[l,j] for l in range(A.size2)])
    return C

def multiplyv(A:matrix,v:list):
    " Multiply matrix and vector "
    assert(A.size2==len(v))
    b = []
    for i in range(len(v)):
        b.append(sum([A[i,j]*v[j] for j in range(len(v))]))
    return b


def trans(A:matrix):
    " Transpose matrix "
    B = matrix(A.size2,A.size1)
    for i in range(A.size1):
        for j in range(A.size2):
            B[j,i] = A[i,j]
    return B

def dot(A:array,B:array):
    " Find dot product of two vectors/arrays "
    S = 0
    for i in range(len(A)):
        S += A[i]*B[i]
    return S

def inner_v(A:array):
    " Inner product of vector "
    return np.sqrt(dot(A,A))

def qr_gs_decomp(A:matrix):
    " QR decomposition of matrix "
    R = matrix(A.size2,A.size2)
    Q = matrix(A.size1,A.size2)
    Aj = copy(A)
    
    for i in range(A.size2):
        R[i,i] = dot(Aj.col(i),Aj.col(i))**(1./2)
        for l in range(A.size1):
            Q[l,i] = Aj[l,i]/R[i,i]
        
        for j in range(i+1,A.size2):
            R[i,j] = dot(Q.col(i),Aj.col(j))
            for l in range(A.size1):
                Aj[l,j] = Aj[l,j]-Q[l,i]*R[i,j]
    
    return Q,R

def qr_gs_solve(Q:matrix,R:matrix,b:list,check=0):
    " Solve linear system from QR decomposition "
    x = [0 for i in range(Q.size2)]
    for i in range(Q.size2):
        x[i] = dot(Q.col(i),b)
    for i in range(Q.size2-1,-1,-1):
        x[i] /= R[i,i]
        for j in range(i-1,-1,-1):
            x[j] -= x[i]*R[j,i]

    return x

def qr_gs_inverse(Q:matrix,R:matrix):
    " Find inverse matrix from QR decomposition "
    Rin = matrix(R.size1,R.size2)
    for i in range(R.size2-1,-1,-1):
        Rin[i,i] = 1/R[i,i]
        for l in range(i+1,R.size2):
            Rin[i,l] /= R[i,i]
        for j in range(i-1,-1,-1):
            for l in range(i,R.size2):
                Rin[j,l] -= R[j,i]*Rin[i,l]
    B = multiply(Rin,trans(Q))
    
    return B
