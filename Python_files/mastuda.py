# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\mastuda_func.m
import numpy
from numpy import * 
from math import * 

from adding import addpoly
    
def mastuda_func(F=None,alp=None,fl=None,fu=None,N=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    wl=dot(dot(2,pi),fl)
# ..\MATLAB_files\mastuda_func.m:3
    #wl=fl;
    wu=dot(dot(2,pi),fu)
# ..\MATLAB_files\mastuda_func.m:5
    #wu=fu;
    K=dot(2,N) + 1
# ..\MATLAB_files\mastuda_func.m:7
    
    p=logspace(log10(wl),log10(wu),K)
# ..\MATLAB_files\mastuda_func.m:8
    
    d=numpy.zeros([K,1])
# ..\MATLAB_files\mastuda_func.m:9
    d[0]=p[0] ** alp
# ..\MATLAB_files\mastuda_func.m:11
    
    d[1]=(p[1] - p[0]) / ((p[1] ** alp) - (p[0] ** alp))
# ..\MATLAB_files\mastuda_func.m:12
    for i in range(2,K):
        d[i]=(p[i] - p[0]) / (- d[0] + p[i] ** alp)
# ..\MATLAB_files\mastuda_func.m:14
        for j in range(1,i):
            d[i]=(p[i] - p[j]) / (- d[j] + d[i])
# ..\MATLAB_files\mastuda_func.m:16
    
 #   a_neg1=1
# ..\MATLAB_files\mastuda_func.m:20
    
    a_0=d[0]
# ..\MATLAB_files\mastuda_func.m:21
    b_0=1
# ..\MATLAB_files\mastuda_func.m:22
#    x=concat([0])
# ..\MATLAB_files\mastuda_func.m:23
#    po=concat([0])
# ..\MATLAB_files\mastuda_func.m:24
    an=numpy.zeros([2*N,2*N])
# ..\MATLAB_files\mastuda_func.m:25
    bn=numpy.zeros([2*N,2*N])
# ..\MATLAB_files\mastuda_func.m:26
    for j in range(0,2*N):
        if (j == 0):
            an[j,0:2]               = addpoly(d[j+1]*a_0,[1,- p[j]])
            bn[j,0]                 = d[j + 1]*b_0
        elif (j == 1):
            an[j,0:2]               = addpoly((d[j + 1]*an[j-1, 0:2]),convolve([1,- p[j]],a_0))
            bn[j,0:2]               = addpoly((d[j + 1]*bn[j-1, 0]),convolve([1,- p[j]],b_0))
        elif (j == 2):
            an[j,0:j+1]             = addpoly((d[j + 1]*an[j-1, 0:j]),convolve([1,- p[j]],an[j-2,0:2]))
            bn[j,0:j]               = addpoly((d[j + 1]*bn[j-1, 0:j]),convolve([1,- p[j]],bn[j-2,0]))
        elif (remainder(j+1,2) == 0):
            x                       = convolve([1,- p[j]],an[j-2, 0:j-1])
            po                      = convolve([1,- p[j]],bn[j-2, 0:j])
            an[j,0:j]               = addpoly(x, (d[j + 1]*an[j-1,0:j]))
            bn[j,0:j+1]             = addpoly(po,(d[j + 1]*bn[j-1,0:j]))
        else:
            x                       = convolve([1,- p[j]],an[j-2,0:j])
            po                      = convolve([1,- p[j]],bn[j-2,0:j-1])
            an[j,0:j+1]             = addpoly(x, (d[j + 1]*an[j-1,0:j]))
            bn[j,0:j]               = addpoly(po,(d[j + 1]*bn[j-1,0:j]))
    
    num=an[2*N-1,0:N+1] / an[2*N-1,0]
# ..\MATLAB_files\mastuda_func.m:50
    den=bn[2*N-1,0:N+1] / an[2*N-1,0]
# ..\MATLAB_files\mastuda_func.m:51
    num=multiply(F,num)
# ..\MATLAB_files\mastuda_func.m:53
    print(num,den)
    return num,den