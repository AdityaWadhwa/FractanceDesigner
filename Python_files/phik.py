# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\phik.m
from numpy import * 
from math import * 

    
def phik(k=None,w=None,alp=None,*args,**kwargs):
    varargin = args
    nargin = 3 + len(varargin)

    prod=1
# ..\MATLAB_files\phik.m:3
    phi_0=w ** alp
# ..\MATLAB_files\phik.m:4
    phi_1=(w ** (1 - alp)) / alp
# ..\MATLAB_files\phik.m:5
    m=1
# ..\MATLAB_files\phik.m:6
    if (k == 0):
        phik_val=copy(phi_0)
# ..\MATLAB_files\phik.m:8
    else:
        if (k == 1):
            phik_val=copy(phi_1)
# ..\MATLAB_files\phik.m:10
        else:
            if (mod(k,2) == 0):
                m=k / 2
# ..\MATLAB_files\phik.m:12
                for i in arange(1,m,1).reshape(-1):
                    prod=dot(prod,(i + alp)) / (i - alp)
# ..\MATLAB_files\phik.m:14
                phik_val=dot(prod,phi_0)
# ..\MATLAB_files\phik.m:16
            else:
                m=(k - 1) / 2
# ..\MATLAB_files\phik.m:18
                for i in arange(1,m,1).reshape(-1):
                    prod=dot(prod,(i - alp + 1)) / (i + alp)
# ..\MATLAB_files\phik.m:20
                phik_val=dot(dot(prod,phi_1),(m + 1))
# ..\MATLAB_files\phik.m:22
    
    return phik_val