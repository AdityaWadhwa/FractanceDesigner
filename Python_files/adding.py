# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\addpoly.m
import copy
import numpy
    
def addpoly(x1=None,x2=None,*args,**kwargs):
    varargin = args
    nargin = 2 + numpy.size(varargin)

    x1_order=numpy.size(x1)
# ..\MATLAB_files\addpoly.m:2
    x2_order=numpy.size(x2)
# ..\MATLAB_files\addpoly.m:3
    if x1_order > x2_order:
        max_order=numpy.size(x1)
# ..\MATLAB_files\addpoly.m:5
        new_x2=numpy.pad(x2,(max_order - numpy.size(x2),0),'constant', constant_values=(0,0))
# ..\MATLAB_files\addpoly.m:6
        new_x1=copy.copy(x1)
# ..\MATLAB_files\addpoly.m:7
    else:
        max_order=numpy.size(x2)
# ..\MATLAB_files\addpoly.m:9
        new_x1=numpy.pad(x1,(max_order - numpy.size(x1),0),'constant', constant_values=(0,0))
# ..\MATLAB_files\addpoly.m:10
        new_x2=copy.copy(x2)
# ..\MATLAB_files\addpoly.m:11
    
    coeff_sum=new_x1 + new_x2
# ..\MATLAB_files\addpoly.m:13
    return coeff_sum