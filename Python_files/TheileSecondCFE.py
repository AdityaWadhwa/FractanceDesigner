# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\TheileSecondCFE_func.m
import copy
import numpy
from numpy import * 
from math import * 

from phik import phik_func
from adding import addpoly
    
    
def TheileSecondCFE_func(F=None,alp=None,fl=None,fu=None,N=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    K=dot(2,N) + 1
# ..\MATLAB_files\TheileSecondCFE_func.m:3
    wl=dot(dot(2,pi),fl)
# ..\MATLAB_files\TheileSecondCFE_func.m:4
    wu=dot(dot(2,pi),fu)
# ..\MATLAB_files\TheileSecondCFE_func.m:5
    p=logspace(log10(wl),log10(wu),K)
# ..\MATLAB_files\TheileSecondCFE_func.m:6
    
    w_0=median(p)
# ..\MATLAB_files\TheileSecondCFE_func.m:7
    c_0=phik_func(0,w_0,alp)
# ..\MATLAB_files\TheileSecondCFE_func.m:8
    c=zeros(2*N)
# ..\MATLAB_files\TheileSecondCFE_func.m:9
    for i in range(0,2*N):
        if (i == 0):
            c[i]=phik_func(i+1,w_0,alp)
# ..\MATLAB_files\TheileSecondCFE_func.m:13
        else:
            c[i]=phik_func(i+1,w_0,alp) - phik_func(i-1,w_0,alp)
# ..\MATLAB_files\TheileSecondCFE_func.m:15
    
    #a_neg1 = 1; #a-1
    a_0=copy(c_0)
# ..\MATLAB_files\TheileSecondCFE_func.m:20
    b_0=1
# ..\MATLAB_files\TheileSecondCFE_func.m:21
    x=0
# ..\MATLAB_files\TheileSecondCFE_func.m:22
    po=0
# ..\MATLAB_files\TheileSecondCFE_func.m:23
    an=zeros([2*N,2*N])
# ..\MATLAB_files\TheileSecondCFE_func.m:24
    bn=zeros([2*N,2*N])
# ..\MATLAB_files\TheileSecondCFE_func.m:25
    for j in range(0,2*N):
        if (j == 0):
            an[j,0:2]   = addpoly([c[j]*a_0],[1,-w_0])
            bn[j,0]     = c[j]*b_0
        elif (j == 1):
            an[j,0:2]   = addpoly(c[j]*an[j-1,0:2],convolve([1,-w_0],a_0))
            bn[j,0:2]   = addpoly([c[j]*bn[j-1,0]],convolve([1,-w_0],b_0))
        elif (remainder(j+1,2) == 0):
            x           = convolve([1,-w_0],an[j-2,0:j-1])
            po          = convolve([1,-w_0],bn[j-2,0:j])
            an[j,0:j]   = addpoly(x, (c[j]*an[j-1,0:j]))
            bn[j,0:j+1] = addpoly([po],(c[j]*bn[j-1,0:j]))
        else:
            x           = convolve([1,-w_0],an[j-2,0:j])
            po          = convolve([1,-w_0],bn[j-2,0:j-1])
            an[j,0:j+1] = addpoly(x, (c[j]*an[j-1,0:j]))
            bn[j,0:j]   = addpoly([po],(c[j]*bn[j-1,0:j]))
    
#    Num=an(dot(2,N),arange(1,N + 1)) / an(dot(2,N),1)
    Num=an[2*N-1,0:N+1] / an[2*N-1,0]
# ..\MATLAB_files\TheileSecondCFE_func.m:50
#    Den=bn(dot(2,N),arange(1,N + 1)) / an(dot(2,N),1)
    Den=bn[2*N-1,0:N+1] / an[2*N-1,0]
# ..\MATLAB_files\TheileSecondCFE_func.m:51
    Num=multiply(F,Num)
# ..\MATLAB_files\TheileSecondCFE_func.m:52
    print(Num)
    print(Den)
    return Num,Den