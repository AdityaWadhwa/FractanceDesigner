# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\FirstFoster.m
from copy import copy
from numpy import * 
from math import * 
from scipy.signal import residue
    
def FirstFoster_func(Num=None,Den=None,fl=None,fh=None,fstep=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    b=copy(Num)
# ..\MATLAB_files\FirstFoster.m:3
    a=copy(Den)
# ..\MATLAB_files\FirstFoster.m:4
    filename='D:\\DocumentsHDD\\BTP\\GUIapp\\Pspice_files\\FirstFoster'
# ..\MATLAB_files\FirstFoster.m:6
    r,p,k=residue(b,a)
# ..\MATLAB_files\FirstFoster.m:8
    
    C=1.0 / r
# ..\MATLAB_files\FirstFoster.m:10
    R=- r / p
# ..\MATLAB_files\FirstFoster.m:11
    if size(k) != 0:
        R = append(R,k)
# ..\MATLAB_files\FirstFoster.m:14
    
    line = []
    line.append(['* Matlab created *.cir-file *'])
# ..\MATLAB_files\FirstFoster.m:17
    line.append(['.lib C:\\Cadence\\SPB_17.2\\tools\\pspice\\library\\eval.lib'])
# ..\MATLAB_files\FirstFoster.m:18
    line.append(['VIN        1   0   AC 1V'])
# ..\MATLAB_files\FirstFoster.m:19
    for i in range(0,len(C)):
        if R[i] != - Inf:
            line.append(['R'+str(i+1)+' '+str(i+1)+' '+str(i+2)+' '+str(R[i])])
# ..\MATLAB_files\FirstFoster.m:22
        line.append(['C'+str(i+1)+' '+str(i+1)+' '+str(i+2)+' '+str(C[i])])
# ..\MATLAB_files\FirstFoster.m:24
    
    line.append(['R'+str(i + 2)+' '+str(i + 2)+' 0 '+str(R[len(R)-1])])
# ..\MATLAB_files\FirstFoster.m:26
    line.append(['.AC DEC '+str(fstep)+' '+str(fl)+' '+str(fh)])
# ..\MATLAB_files\FirstFoster.m:27
    line.append(['.PRINT AC VM(1) VP(1) IM(VIN) IP(VIN)'])
# ..\MATLAB_files\FirstFoster.m:28
    line.append(['.END'])
# ..\MATLAB_files\FirstFoster.m:29
    # writing netlist to file
    f=open(filename+'.cir','w')
# ..\MATLAB_files\FirstFoster.m:32
    for i in range(0,len(line)):
        f.write(str(line[i][0])+'\n');
    
    f.close()
# ..\MATLAB_files\FirstFoster.m:36
    return filename
    
if __name__ == '__main__':
    pass
    