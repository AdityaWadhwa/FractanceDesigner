# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\coeffmodoustaloup.m
from copy import copy
from numpy import * 
from math import * 
    
def coeffmodoustaloup(F=None,alp=None,fl=None,fh=None,N=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    Num=1
# ..\MATLAB_files\coeffmodoustaloup.m:3
    Den=1
# ..\MATLAB_files\coeffmodoustaloup.m:4
    alpha=abs(alp)
# ..\MATLAB_files\coeffmodoustaloup.m:5
    wb=copy(fl)
# ..\MATLAB_files\coeffmodoustaloup.m:7
    
    wh=copy(fh)
# ..\MATLAB_files\coeffmodoustaloup.m:8
    d=9
# ..\MATLAB_files\coeffmodoustaloup.m:10
    b=10
# ..\MATLAB_files\coeffmodoustaloup.m:11
    N=N//2
# ..\MATLAB_files\coeffmodoustaloup.m:12
    K=(((d*wb) / b) ** alpha)
# ..\MATLAB_files\coeffmodoustaloup.m:14
    for k in range(-N,N+1):
        w_k=((d*wb) / b) ** ((alpha - (2*k)) / (2*N+1))
# ..\MATLAB_files\coeffmodoustaloup.m:16
        wk=((b*wh) / d) ** ((alpha + (2*k)) / (2*N+1))
# ..\MATLAB_files\coeffmodoustaloup.m:17
        Num=convolve(Num,[wk,(wk*w_k)])
# ..\MATLAB_files\coeffmodoustaloup.m:18
        Den=convolve(Den,[w_k,(wk*w_k)])
# ..\MATLAB_files\coeffmodoustaloup.m:19
    
    Num=convolve(Num,[d,(b*wh),0])
# ..\MATLAB_files\coeffmodoustaloup.m:22
    Den=convolve(Den,[(d*(1 - alpha)),(b*wh),(d*alpha)])
# ..\MATLAB_files\coeffmodoustaloup.m:23
    Num=multiply(K,Num)
# ..\MATLAB_files\coeffmodoustaloup.m:24
    if alp < 0:
        Den,Num = Num,Den
# ..\MATLAB_files\coeffmodoustaloup.m:27
    
    normalizer=Den[1]
# ..\MATLAB_files\coeffmodoustaloup.m:30
    Num=Num / normalizer
# ..\MATLAB_files\coeffmodoustaloup.m:31
    Den=Den / normalizer
# ..\MATLAB_files\coeffmodoustaloup.m:32
    Num=multiply(F,Num)
# ..\MATLAB_files\coeffmodoustaloup.m:33
    return Num,Den
    
if __name__ == '__main__':
    pass
    