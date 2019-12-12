# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\mastuda_func.m
import numpy
from numpy import * 
from math import * 
    
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
    d[1]=p(1) ** alp
# ..\MATLAB_files\mastuda_func.m:11
    
    d[2]=(p(2) - p(1)) / ((p(2) ** alp) - (p(1) ** alp))
# ..\MATLAB_files\mastuda_func.m:12
    for i in arange(3,K,1).reshape(-1):
        d[i]=(p(i) - p(1)) / (- d(1) + p(i) ** alp)
# ..\MATLAB_files\mastuda_func.m:14
        for j in arange(2,i - 1,1).reshape(-1):
            d[i]=(p(i) - p(j)) / (- d(j) + d(i))
# ..\MATLAB_files\mastuda_func.m:16
    
    a_neg1=1
# ..\MATLAB_files\mastuda_func.m:20
    
    a_0=d(1)
# ..\MATLAB_files\mastuda_func.m:21
    b_0=1
# ..\MATLAB_files\mastuda_func.m:22
    x=concat([0])
# ..\MATLAB_files\mastuda_func.m:23
    po=concat([0])
# ..\MATLAB_files\mastuda_func.m:24
    an=numpy.zeros(dot(2,N))
# ..\MATLAB_files\mastuda_func.m:25
    bn=numpy.zeros(dot(2,N))
# ..\MATLAB_files\mastuda_func.m:26
    for j in arange(1,dot(2,N),1).reshape(-1):
        if (j == 1):
            an[j,arange(1,2)]=addpoly(dot(d(j + 1),a_0),concat([1,- p(j)]))
# ..\MATLAB_files\mastuda_func.m:29
            bn[j,1]=dot(d(j + 1),b_0)
# ..\MATLAB_files\mastuda_func.m:30
        else:
            if (j == 2):
                an[j,arange(1,2)]=addpoly(dot(d(j + 1),an(j - 1,arange(1,2))),conv(concat([1,- p(j)]),a_0))
# ..\MATLAB_files\mastuda_func.m:32
                bn[j,arange(1,2)]=addpoly(dot(d(j + 1),bn(j - 1,1)),conv(concat([1,- p(j)]),b_0))
# ..\MATLAB_files\mastuda_func.m:33
            else:
                if (j == 3):
                    an[j,arange(1,j)]=addpoly(dot(d(j + 1),an(j - 1,arange(1,j - 1))),conv(concat([1,- p(j)]),an(j - 2,arange(1,2))))
# ..\MATLAB_files\mastuda_func.m:35
                    bn[j,arange(1,j - 1)]=addpoly(dot(d(j + 1),bn(j - 1,arange(1,j - 1))),conv(concat([1,- p(j)]),bn(j - 2,1)))
# ..\MATLAB_files\mastuda_func.m:36
                else:
                    if (mod(j,2) == 0):
                        x=conv(concat([1,- p(j)]),an(j - 2,arange(1,j - 2)))
# ..\MATLAB_files\mastuda_func.m:38
                        po=conv(concat([1,- p(j)]),bn(j - 2,arange(1,j - 1)))
# ..\MATLAB_files\mastuda_func.m:39
                        an[j,arange(1,j - 1)]=addpoly(x,dot(d(j + 1),an(j - 1,arange(1,j - 1))))
# ..\MATLAB_files\mastuda_func.m:40
                        bn[j,arange(1,j)]=addpoly(po,dot(d(j + 1),bn(j - 1,arange(1,j - 1))))
# ..\MATLAB_files\mastuda_func.m:41
                    else:
                        x=conv(concat([1,- p(j)]),an(j - 2,arange(1,j - 1)))
# ..\MATLAB_files\mastuda_func.m:43
                        po=conv(concat([1,- p(j)]),bn(j - 2,arange(1,j - 2)))
# ..\MATLAB_files\mastuda_func.m:44
                        an[j,arange(1,j)]=addpoly(x,dot(d(j + 1),an(j - 1,arange(1,j - 1))))
# ..\MATLAB_files\mastuda_func.m:45
                        bn[j,arange(1,j - 1)]=addpoly(po,dot(d(j + 1),bn(j - 1,arange(1,j - 1))))
# ..\MATLAB_files\mastuda_func.m:46
    
    num=an(dot(2,N),arange(1,N + 1)) / an(dot(2,N),1)
# ..\MATLAB_files\mastuda_func.m:50
    den=bn(dot(2,N),arange(1,N + 1)) / an(dot(2,N),1)
# ..\MATLAB_files\mastuda_func.m:51
    num=multiply(F,num)
# ..\MATLAB_files\mastuda_func.m:53
    return num,den