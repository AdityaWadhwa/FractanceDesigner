# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\charef_func_TS.m

# charef's method, more realistic for higher frequencies
import copy
    
def charef_func_TS(F=None,alp=None,fl=None,fu=None,derr=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    err=1e-05
# ..\MATLAB_files\charef_func_TS.m:4
    
    wl=copy.copy(fl)
# ..\MATLAB_files\charef_func_TS.m:5
    #wl = 2*pi*fl;
    wu=copy.copy(fu)
# ..\MATLAB_files\charef_func_TS.m:7
    #wu = 2*pi*fu;
    
    alpha=abs(alp)
# ..\MATLAB_files\charef_func_TS.m:10
    
    
    div=10 ** (err / (dot(10,alpha))) - 1
# ..\MATLAB_files\charef_func_TS.m:12
    wc=abs(dot(wl,(sqrt(div))))
# ..\MATLAB_files\charef_func_TS.m:13
    num=concat([1])
# ..\MATLAB_files\charef_func_TS.m:15
    den=concat([1])
# ..\MATLAB_files\charef_func_TS.m:16
    powa=derr / (dot(10,(1 - alpha)))
# ..\MATLAB_files\charef_func_TS.m:18
    powb=derr / (dot(10,alpha))
# ..\MATLAB_files\charef_func_TS.m:19
    powz0=derr / (dot(20,alpha))
# ..\MATLAB_files\charef_func_TS.m:20
    z0=dot(wc,(10 ** powz0))
# ..\MATLAB_files\charef_func_TS.m:21
    a=10 ** powa
# ..\MATLAB_files\charef_func_TS.m:22
    b=10 ** powb
# ..\MATLAB_files\charef_func_TS.m:23
    p0=dot(a,z0)
# ..\MATLAB_files\charef_func_TS.m:24
    wmax=dot(100,wu)
# ..\MATLAB_files\charef_func_TS.m:25
    Kd=wc ** alpha
# ..\MATLAB_files\charef_func_TS.m:27
    nu=log10(wmax / z0)
# ..\MATLAB_files\charef_func_TS.m:28
    d=log10(dot(a,b))
# ..\MATLAB_files\charef_func_TS.m:29
    x=1
# ..\MATLAB_files\charef_func_TS.m:30
    N=floor(nu / d) + 1
# ..\MATLAB_files\charef_func_TS.m:32
    for i in arange(0,N,1).reshape(-1):
        x=(dot(a,b)) ** i
# ..\MATLAB_files\charef_func_TS.m:34
        num=conv(num,concat([1 / (dot(z0,x)),1]))
# ..\MATLAB_files\charef_func_TS.m:35
        den=conv(den,concat([1 / (dot(p0,x)),1]))
# ..\MATLAB_files\charef_func_TS.m:36
    
    x=dot(Kd,F)
# ..\MATLAB_files\charef_func_TS.m:38
    num=multiply(x,num)
# ..\MATLAB_files\charef_func_TS.m:39
    if alp < 0:
        num,den=deal(den,num,nargout=2)
# ..\MATLAB_files\charef_func_TS.m:42
    
    normalizer=den(1)
# ..\MATLAB_files\charef_func_TS.m:45
    num=num / normalizer
# ..\MATLAB_files\charef_func_TS.m:46
    den=den / normalizer
# ..\MATLAB_files\charef_func_TS.m:47
    return num,den
    
if __name__ == '__main__':
    pass
    