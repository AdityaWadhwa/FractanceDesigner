# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\SecondFoster.m
from copy import copy
from numpy import * 
from math import * 
from scipy.signal import residue,deconvolve
    
def SecondFoster_func(Num=None,Den=None,fl=None,fh=None,fstep=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    b=copy(Num)
# ..\MATLAB_files\SecondFoster.m:3
    a=copy(Den)
# ..\MATLAB_files\SecondFoster.m:4
    filename='D:\\DocumentsHDD\\BTP\\GUIapp\\Pspice_files\\SecondFoster'
# ..\MATLAB_files\SecondFoster.m:6
    if len(a[a>0]) > len(b[b>0]): #find(a > 0,1,'first') > find(b > 0,1,'first'):
        Clast=a[0] / b[0]
# ..\MATLAB_files\SecondFoster.m:9
        a = a - append((Clast*b),0)
# ..\MATLAB_files\SecondFoster.m:10
        a=a[1:end]
# ..\MATLAB_files\SecondFoster.m:11
    else:
        Clast=0
# ..\MATLAB_files\SecondFoster.m:13
    
    Rlast=b[b>0][-1] / a[a>0][-1]
# ..\MATLAB_files\SecondFoster.m:16
    a=a - dot((1 / Rlast),b)
# ..\MATLAB_files\SecondFoster.m:17
    
    r,p,k=residue(a,b)
# ..\MATLAB_files\SecondFoster.m:19
    
    for i in range(0,len(p)):
        Num=copy(a)
# ..\MATLAB_files\SecondFoster.m:22
        Den=convolve(b,[1,0])
# ..\MATLAB_files\SecondFoster.m:23
        Den,_=deconvolve(Den,[1,- p[i]])
# ..\MATLAB_files\SecondFoster.m:24
        r[i]=polyval(Num,p[i]) / polyval(Den,p[i])
# ..\MATLAB_files\SecondFoster.m:25
    
    
    R=1.0 / r
# ..\MATLAB_files\SecondFoster.m:28
    C=- r / p
# ..\MATLAB_files\SecondFoster.m:29
    if Rlast != 0:
        R=append(R,Rlast)
# ..\MATLAB_files\SecondFoster.m:32
    
    if Clast != 0:
        R=append(R,0)
# ..\MATLAB_files\SecondFoster.m:37
        C=append(C,Clast)
# ..\MATLAB_files\SecondFoster.m:38
    
    line = []
    line.append(['* Matlab created *.cir-file *'])
# ..\MATLAB_files\SecondFoster.m:41
    line.append(['.lib C:\\Cadence\\SPB_17.2\\tools\\pspice\\library\\eval.lib'])
# ..\MATLAB_files\SecondFoster.m:42
    line.append(['VIN        1   0   AC 1V'])
# ..\MATLAB_files\SecondFoster.m:43
    for i in range(0,len(C)):
        line.append(['R'+str(i+1)+' 1 '+str(i+2)+' '+str(R[i])])
# ..\MATLAB_files\SecondFoster.m:45
        line.append(['C'+str(i+1)+' '+str(i+2)+' 0 '+str(C[i])])
# ..\MATLAB_files\SecondFoster.m:46
    
    line.append(['R'+str(len(R))+' 1 '+str(i+2)+' '+str(R[len(R)-1])])
# ..\MATLAB_files\SecondFoster.m:48
    line.append(['.AC DEC '+str(fstep)+' '+str(fl)+' '+str(fh)])
# ..\MATLAB_files\SecondFoster.m:49
    line.append(['.PRINT AC VM(1) VP(1) IM(VIN) IP(VIN)'])
# ..\MATLAB_files\SecondFoster.m:50
    line.append(['.END'])
# ..\MATLAB_files\SecondFoster.m:51
    # writing netlist to file
    f = open(filename+'.cir','w')
# ..\MATLAB_files\SecondFoster.m:54
    for i in range(0,len(line)):
        f.write(str(line[i])+'\n')
    
    f.close()
# ..\MATLAB_files\SecondFoster.m:58
    return filename
    
if __name__ == '__main__':
    pass
    