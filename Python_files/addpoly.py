# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\addpoly.m
import copy
    
def addpoly(x1=None,x2=None,*args,**kwargs):
    varargin = args
    nargin = 2 + len(varargin)

    x1_order=length(x1)
# ..\MATLAB_files\addpoly.m:2
    x2_order=length(x2)
# ..\MATLAB_files\addpoly.m:3
    if x1_order > x2_order:
        max_order=size(x1)
# ..\MATLAB_files\addpoly.m:5
        new_x2=padarray(x2,max_order - size(x2),0,'pre')
# ..\MATLAB_files\addpoly.m:6
        new_x1=copy(x1)
# ..\MATLAB_files\addpoly.m:7
    else:
        max_order=size(x2)
# ..\MATLAB_files\addpoly.m:9
        new_x1=padarray(x1,max_order - size(x1),0,'pre')
# ..\MATLAB_files\addpoly.m:10
        new_x2=copy.copy(x2)
# ..\MATLAB_files\addpoly.m:11
    
    coeff_sum=new_x1 + new_x2
# ..\MATLAB_files\addpoly.m:13
    return coeff_sum