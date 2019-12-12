# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\TheileSecondCFE_func.m
import copy
import numpy
from numpy import * 
from math import * 
    
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
    c_0=phik(0,w_0,alp)
# ..\MATLAB_files\TheileSecondCFE_func.m:8
    c=numpy.zeros([dot(2,N),1])
# ..\MATLAB_files\TheileSecondCFE_func.m:9
    for i in arange(1,dot(2,N),1).reshape(-1):
        if (i == 1):
            c[i]=phik(i,w_0,alp)
# ..\MATLAB_files\TheileSecondCFE_func.m:13
        else:
            c[i]=phik(i,w_0,alp) - phik(i - 2,w_0,alp)
# ..\MATLAB_files\TheileSecondCFE_func.m:15
    
    #a_neg1 = 1; #a-1
    a_0=copy.copy(c_0)
# ..\MATLAB_files\TheileSecondCFE_func.m:20
    b_0=1
# ..\MATLAB_files\TheileSecondCFE_func.m:21
    x=concat([0])
# ..\MATLAB_files\TheileSecondCFE_func.m:22
    po=concat([0])
# ..\MATLAB_files\TheileSecondCFE_func.m:23
    an=numpy.zeros(dot(2,N))
# ..\MATLAB_files\TheileSecondCFE_func.m:24
    bn=numpy.zeros(dot(2,N))
# ..\MATLAB_files\TheileSecondCFE_func.m:25
    for j in arange(1,dot(2,N),1).reshape(-1):
        if (j == 1):
            an[j,arange(1,2)]=addpoly(dot(c(j),a_0),concat([1,- w_0]))
# ..\MATLAB_files\TheileSecondCFE_func.m:29
            bn[j,1]=dot(c(j),b_0)
# ..\MATLAB_files\TheileSecondCFE_func.m:30
        else:
            if (j == 2):
                an[j,arange(1,2)]=addpoly(dot(c(j),an(j - 1,arange(1,2))),conv(concat([1,- w_0]),a_0))
# ..\MATLAB_files\TheileSecondCFE_func.m:32
                bn[j,arange(1,2)]=addpoly(dot(c(j),bn(j - 1,1)),conv(concat([1,- w_0]),b_0))
# ..\MATLAB_files\TheileSecondCFE_func.m:33
                #     elseif(j==3)
#         an(j,1:j) = addpoly(c(j)*an(j-1,1:j-1), conv([1 -w_0], an(j-2,1:2)));
#         #bn(j,1:j-1) = addpoly(d(j+1)*bn(j-1,1:j-1), conv([1 -p(j)], bn(j-2,1)));
            else:
                if (mod(j,2) == 0):
                    x=conv(concat([1,- w_0]),an(j - 2,arange(1,j - 2)))
# ..\MATLAB_files\TheileSecondCFE_func.m:38
                    po=conv(concat([1,- w_0]),bn(j - 2,arange(1,j - 1)))
# ..\MATLAB_files\TheileSecondCFE_func.m:39
                    an[j,arange(1,j - 1)]=addpoly(x,dot(c(j),an(j - 1,arange(1,j - 1))))
# ..\MATLAB_files\TheileSecondCFE_func.m:40
                    bn[j,arange(1,j)]=addpoly(po,dot(c(j),bn(j - 1,arange(1,j - 1))))
# ..\MATLAB_files\TheileSecondCFE_func.m:41
                else:
                    x=conv(concat([1,- w_0]),an(j - 2,arange(1,j - 1)))
# ..\MATLAB_files\TheileSecondCFE_func.m:43
                    po=conv(concat([1,- w_0]),bn(j - 2,arange(1,j - 2)))
# ..\MATLAB_files\TheileSecondCFE_func.m:44
                    an[j,arange(1,j)]=addpoly(x,dot(c(j),an(j - 1,arange(1,j - 1))))
# ..\MATLAB_files\TheileSecondCFE_func.m:45
                    bn[j,arange(1,j - 1)]=addpoly(po,dot(c(j),bn(j - 1,arange(1,j - 1))))
# ..\MATLAB_files\TheileSecondCFE_func.m:46
    
    Num=an(dot(2,N),arange(1,N + 1)) / an(dot(2,N),1)
# ..\MATLAB_files\TheileSecondCFE_func.m:50
    Den=bn(dot(2,N),arange(1,N + 1)) / an(dot(2,N),1)
# ..\MATLAB_files\TheileSecondCFE_func.m:51
    Num=multiply(F,Num)
# ..\MATLAB_files\TheileSecondCFE_func.m:52
    return Num,Den