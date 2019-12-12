# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\coeffcarlson.m
from copy import copy
from numpy import * 
from math import * 
    
def coeffcarlson(F=None,alp=None,fl=None,fh=None,N=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    Num0=1
# ..\MATLAB_files\coeffcarlson.m:3
    Den0=1
# ..\MATLAB_files\coeffcarlson.m:4
    alpha=abs(alp)
# ..\MATLAB_files\coeffcarlson.m:6
    alpha=round(dot(alpha,10),0)
# ..\MATLAB_files\coeffcarlson.m:7
    i_5=int(alpha//5)
# ..\MATLAB_files\coeffcarlson.m:8
    alpha=alpha%5
# ..\MATLAB_files\coeffcarlson.m:9
    i_2=int(alpha//2)
# ..\MATLAB_files\coeffcarlson.m:10
    alpha=alpha%2
# ..\MATLAB_files\coeffcarlson.m:11
    i_1=int(copy(alpha))
# ..\MATLAB_files\coeffcarlson.m:12
    for i in range(0,N):
        Numpower=copy(Num0)
# ..\MATLAB_files\coeffcarlson.m:16
        Denpower=copy(Den0)
# ..\MATLAB_files\coeffcarlson.m:17
        for j in range(1,2):
            Numpower=convolve(Numpower,Num0)
# ..\MATLAB_files\coeffcarlson.m:19
            Denpower=convolve(Denpower,Den0)
# ..\MATLAB_files\coeffcarlson.m:20
        Num1=convolve(Num0,multiply((2 - 1),convolve(([0,1]),Numpower)) + multiply((2 + 1),convolve(([1,0]),Denpower)))
# ..\MATLAB_files\coeffcarlson.m:23
        Den1=convolve(Den0,multiply((2 + 1),convolve(([0,1]),Numpower)) + multiply((2 - 1),convolve(([1,0]),Denpower)))
# ..\MATLAB_files\coeffcarlson.m:24
        Num0=copy(Num1)
# ..\MATLAB_files\coeffcarlson.m:26
        Den0=copy(Den1)
# ..\MATLAB_files\coeffcarlson.m:27
    
    Num5=copy(Num1)
# ..\MATLAB_files\coeffcarlson.m:31
    Den5=copy(Den1)
# ..\MATLAB_files\coeffcarlson.m:32
    Num0=1
# ..\MATLAB_files\coeffcarlson.m:34
    Den0=1
# ..\MATLAB_files\coeffcarlson.m:35
    for i in range(0,N):
        Numpower=copy(Num0)
# ..\MATLAB_files\coeffcarlson.m:39
        Denpower=copy(Den0)
# ..\MATLAB_files\coeffcarlson.m:40
        for j in range(1,5):
            Numpower=convolve(Numpower,Num0)
# ..\MATLAB_files\coeffcarlson.m:42
            Denpower=convolve(Denpower,Den0)
# ..\MATLAB_files\coeffcarlson.m:43
        Num1=convolve(Num0,multiply((5 - 1),convolve(([0,1]),Numpower)) + multiply((5 + 1),convolve(([1,0]),Denpower)))
# ..\MATLAB_files\coeffcarlson.m:46
        Den1=convolve(Den0,multiply((5 + 1),convolve(([0,1]),Numpower)) + multiply((5 - 1),convolve(([1,0]),Denpower)))
# ..\MATLAB_files\coeffcarlson.m:47
        Num0=copy(Num1)
# ..\MATLAB_files\coeffcarlson.m:49
        Den0=copy(Den1)
# ..\MATLAB_files\coeffcarlson.m:50
    
    Num2=copy(Num1)
# ..\MATLAB_files\coeffcarlson.m:54
    Den2=copy(Den1)
# ..\MATLAB_files\coeffcarlson.m:55
    Num0=1
# ..\MATLAB_files\coeffcarlson.m:57
    Den0=1
# ..\MATLAB_files\coeffcarlson.m:58
    for i in range(0,N):
        Numpower=copy(Num0)
# ..\MATLAB_files\coeffcarlson.m:62
        Denpower=copy(Den0)
# ..\MATLAB_files\coeffcarlson.m:63
        for j in range(1,10):
            Numpower=convolve(Numpower,Num0)
# ..\MATLAB_files\coeffcarlson.m:65
            Denpower=convolve(Denpower,Den0)
# ..\MATLAB_files\coeffcarlson.m:66
        Num1=convolve(Num0,multiply((10 - 1),convolve(([0,1]),Numpower)) + multiply((10 + 1),convolve(([1,0]),Denpower)))
# ..\MATLAB_files\coeffcarlson.m:69
        Den1=convolve(Den0,multiply((10 + 1),convolve(([0,1]),Numpower)) + multiply((10 - 1),convolve(([1,0]),Denpower)))
# ..\MATLAB_files\coeffcarlson.m:70
        Num0=copy(Num1)
# ..\MATLAB_files\coeffcarlson.m:72
        Den0=copy(Den1)
# ..\MATLAB_files\coeffcarlson.m:73
    
    Num=1
# ..\MATLAB_files\coeffcarlson.m:77
    Den=1
# ..\MATLAB_files\coeffcarlson.m:78
    for j in range(0,i_5):
        Num=convolve(Num,Num5)
# ..\MATLAB_files\coeffcarlson.m:80
        Den=convolve(Den,Den5)
# ..\MATLAB_files\coeffcarlson.m:81
    
    for j in range(0,i_2):
        Num=convolve(Num,Num2)
# ..\MATLAB_files\coeffcarlson.m:84
        Den=convolve(Den,Den2)
# ..\MATLAB_files\coeffcarlson.m:85
    
    for j in range(0,i_1):
        Num=convolve(Num,Num1)
# ..\MATLAB_files\coeffcarlson.m:88
        Den=convolve(Den,Den1)
# ..\MATLAB_files\coeffcarlson.m:89
    
    if alp < 0:
        Den,Num=Num,Den
# ..\MATLAB_files\coeffcarlson.m:93
    
    normalizer=Num[1]
# ..\MATLAB_files\coeffcarlson.m:96
    Num=Num / normalizer
# ..\MATLAB_files\coeffcarlson.m:97
    Den=Den / normalizer
# ..\MATLAB_files\coeffcarlson.m:98
    Num=multiply(F,Num)
# ..\MATLAB_files\coeffcarlson.m:99
    return Num,Den
    
if __name__ == '__main__':
    pass
    