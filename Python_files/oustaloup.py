# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\coeffoustaloup.m
from copy import copy
from numpy import * 
from math import * 
    
def coeffoustaloup(F=None,alp=None,fl=None,fh=None,N=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    Num=1
# ..\MATLAB_files\coeffoustaloup.m:3
    Den=1
# ..\MATLAB_files\coeffoustaloup.m:4
    wl=copy(fl)
# ..\MATLAB_files\coeffoustaloup.m:6
    
    wh=copy(fh)
# ..\MATLAB_files\coeffoustaloup.m:7
    wu=sqrt(wl*wh)
# ..\MATLAB_files\coeffoustaloup.m:9
    C0=wu / wh
# ..\MATLAB_files\coeffoustaloup.m:11
    N = N//2
# ..\MATLAB_files\coeffoustaloup.m:13
    for k in range(-N,N+1):
        w_k=(wl*(wh / wl) ** ((k + N + 1/2 - alp/2) / (2*N+1)))
# ..\MATLAB_files\coeffoustaloup.m:16
        wk=(wl*(wh / wl) ** ((k + N + 1/2 + alp/2) / (2*N+1)))
# ..\MATLAB_files\coeffoustaloup.m:17
        Num=convolve(Num,[wk,wk*w_k])
# ..\MATLAB_files\coeffoustaloup.m:18
        Den=convolve(Den,[w_k,w_k*wk])
# ..\MATLAB_files\coeffoustaloup.m:19
    
    Num=multiply((C0 ** alp),Num)
# ..\MATLAB_files\coeffoustaloup.m:21
    normalizer=Den[1]
# ..\MATLAB_files\coeffoustaloup.m:23
    Num=Num / normalizer
# ..\MATLAB_files\coeffoustaloup.m:24
    Den=Den / normalizer
# ..\MATLAB_files\coeffoustaloup.m:25
    Num=multiply(F,Num)
# ..\MATLAB_files\coeffoustaloup.m:26
    return Num,Den
    
if __name__ == '__main__':
    pass