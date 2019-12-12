# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\errorcalculator.m
import numpy
import matplotlib.pyplot as plt
from numpy import *
from math import * 

    
def errorcalculator(Zmag=None,Zpha=None,F=None,alp=None,fl=None,fh=None,fstep=None,*args,**kwargs):
    varargin = args
    nargin = 7 + len(varargin)

    f=logspace(numpy.log10(fl),numpy.log10(fh),dot((numpy.log10(fh / fl)),fstep) + 1).T
# ..\MATLAB_files\errorcalculator.m:3
    
    s=dot(dot(dot(1j,2),pi),f)
# ..\MATLAB_files\errorcalculator.m:4
    
    Zmagi=multiply(20,numpy.log10(abs(multiply(F,s ** alp))))
# ..\MATLAB_files\errorcalculator.m:6
    Zphai=dot((180 / pi),angle(multiply(F,s ** alp)))
# ..\MATLAB_files\errorcalculator.m:7
    magError=abs((Zmag - Zmagi))
# ..\MATLAB_files\errorcalculator.m:9
    phaError=abs((Zpha - Zphai) / Zphai)
# ..\MATLAB_files\errorcalculator.m:10
#    figure
    plt.subplot(1,2,1)
    plt.semilogx(f,Zmagi,f,Zmag)
    
    plt.subplot(1,2,2)
    plt.semilogx(f,Zphai,f,Zpha)

    plt.show()

    return magError,phaError
    
if __name__ == '__main__':
    pass
    