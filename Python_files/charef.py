# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\charef_func_TS.m

# charef's method, more realistic for higher frequencies
from copy import copy
from numpy import * 
from math import * 
    
def charef_func_TS(F=None,alp=None,fl=None,fu=None,derr=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    err=1e-05
# ..\MATLAB_files\charef_func_TS.m:4
    
    wl=copy(2*pi*fl)
# ..\MATLAB_files\charef_func_TS.m:5
    #wl = 2*pi*fl;
    wu=copy(2*pi*fu)
# ..\MATLAB_files\charef_func_TS.m:7
    #wu = 2*pi*fu;
    
    alpha=abs(alp)
# ..\MATLAB_files\charef_func_TS.m:10
    
    
    div=10 ** (err / ((10*alpha))) - 1
# ..\MATLAB_files\charef_func_TS.m:12
    wc=abs((wl*(sqrt(div))))
# ..\MATLAB_files\charef_func_TS.m:13
    num=1
# ..\MATLAB_files\charef_func_TS.m:15
    den=1
# ..\MATLAB_files\charef_func_TS.m:16
    powa=derr / (10*(1 - alpha))
# ..\MATLAB_files\charef_func_TS.m:18
    powb=derr / (10*alpha)
# ..\MATLAB_files\charef_func_TS.m:19
    powz0=derr / (20*alpha)
# ..\MATLAB_files\charef_func_TS.m:20
    z0=(wc*(10 ** powz0))
# ..\MATLAB_files\charef_func_TS.m:21
    a=10 ** powa
# ..\MATLAB_files\charef_func_TS.m:22
    b=10 ** powb
# ..\MATLAB_files\charef_func_TS.m:23
    p0=(a*z0)
# ..\MATLAB_files\charef_func_TS.m:24
    wmax=(100*wu)
# ..\MATLAB_files\charef_func_TS.m:25
    Kd=wc ** alpha
# ..\MATLAB_files\charef_func_TS.m:27
    nu=log10(wmax / z0)
# ..\MATLAB_files\charef_func_TS.m:28
    d=log10(a*b)
# ..\MATLAB_files\charef_func_TS.m:29
    x=1
# ..\MATLAB_files\charef_func_TS.m:30
    N = int(nu//d + 1)
# ..\MATLAB_files\charef_func_TS.m:32
    for i in range(0,N+1):
        x=(a*b) ** i
# ..\MATLAB_files\charef_func_TS.m:34
        num=convolve(num,[1/(z0*x),1])
# ..\MATLAB_files\charef_func_TS.m:35
        den=convolve(den,[1/(p0*x),1])
# ..\MATLAB_files\charef_func_TS.m:36
    
    x=(Kd*F)
# ..\MATLAB_files\charef_func_TS.m:38
    num=multiply(x,num)
# ..\MATLAB_files\charef_func_TS.m:39
    if alp < 0:
        num,den=den,num
# ..\MATLAB_files\charef_func_TS.m:42
    
    normalizer=den[1]
# ..\MATLAB_files\charef_func_TS.m:45
    num=num / normalizer
# ..\MATLAB_files\charef_func_TS.m:46
    den=den / normalizer
# ..\MATLAB_files\charef_func_TS.m:47
    return num,den
    
if __name__ == '__main__':
    pass
    