# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\coeffmodoustaloup.m
import copy
    
def coeffmodoustaloup(F=None,alp=None,fl=None,fh=None,N=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    Num=concat([1])
# ..\MATLAB_files\coeffmodoustaloup.m:3
    Den=concat([1])
# ..\MATLAB_files\coeffmodoustaloup.m:4
    alpha=abs(alp)
# ..\MATLAB_files\coeffmodoustaloup.m:5
    wb=copy.copy(fl)
# ..\MATLAB_files\coeffmodoustaloup.m:7
    
    wh=copy.copy(fh)
# ..\MATLAB_files\coeffmodoustaloup.m:8
    d=9
# ..\MATLAB_files\coeffmodoustaloup.m:10
    b=10
# ..\MATLAB_files\coeffmodoustaloup.m:11
    N=floor(N / 2)
# ..\MATLAB_files\coeffmodoustaloup.m:12
    K=((dot(d,wb) / b) ** alpha)
# ..\MATLAB_files\coeffmodoustaloup.m:14
    for k in arange(- N,N,1).reshape(-1):
        w_k=(dot(d,wb) / b) ** ((alpha - dot(2,k)) / (dot(2,N) + 1))
# ..\MATLAB_files\coeffmodoustaloup.m:16
        wk=(dot(b,wh) / d) ** ((alpha + dot(2,k)) / (dot(2,N) + 1))
# ..\MATLAB_files\coeffmodoustaloup.m:17
        Num=conv(Num,concat([wk,dot(wk,w_k)]))
# ..\MATLAB_files\coeffmodoustaloup.m:18
        Den=conv(Den,concat([w_k,dot(wk,w_k)]))
# ..\MATLAB_files\coeffmodoustaloup.m:19
    
    Num=conv(Num,concat([d,dot(b,wh),0]))
# ..\MATLAB_files\coeffmodoustaloup.m:22
    Den=conv(Den,concat([dot(d,(1 - alpha)),dot(b,wh),dot(d,alpha)]))
# ..\MATLAB_files\coeffmodoustaloup.m:23
    Num=multiply(K,Num)
# ..\MATLAB_files\coeffmodoustaloup.m:24
    if alp < 0:
        Den,Num=deal(Num,Den,nargout=2)
# ..\MATLAB_files\coeffmodoustaloup.m:27
    
    normalizer=Den(1)
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
    