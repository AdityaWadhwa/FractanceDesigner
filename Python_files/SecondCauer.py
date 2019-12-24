# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\SecondCauer.m
from copy import copy
import numpy
from numpy import * 
from math import * 
    
def SecondCauer_func(Numerator=None,Denominator=None,fl=None,fh=None,fstep=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    q=copy(Numerator)
# ..\MATLAB_files\SecondCauer.m:3
    p=copy(Denominator)
# ..\MATLAB_files\SecondCauer.m:4
    filename='D:\\DocumentsHDD\\BTP\\GUIapp\\Pspice_files\\SecondCauer'
# ..\MATLAB_files\SecondCauer.m:6
    Num=copy(p)
# ..\MATLAB_files\SecondCauer.m:8
    Den=copy(q)
# ..\MATLAB_files\SecondCauer.m:9
    N=size(q)
# ..\MATLAB_files\SecondCauer.m:11
    R=zeros(2*N)
# ..\MATLAB_files\SecondCauer.m:13
    C=zeros(2*N+1)
# ..\MATLAB_files\SecondCauer.m:14
    for i in range(0,2*N+2):

        if size(nonzero(Num>0)[0])==0:
            break
        else:
            idxN=nonzero(Num>0)[0][-1]
# ..\MATLAB_files\SecondCauer.m:18
        if size(nonzero(Den>0)[0])==0:
            break
        else:
            idxD=nonzero(Den>0)[0][-1]
# ..\MATLAB_files\SecondCauer.m:19
        Num[idxN+1:]=0
# ..\MATLAB_files\SecondCauer.m:21
        Den[idxD+1:]=0
# ..\MATLAB_files\SecondCauer.m:22
#        if isempty(idxD):
#            break
        if idxN == idxD:
            qu=Num[idxN] / Den[idxD]
# ..\MATLAB_files\SecondCauer.m:29
            re=Num - (dot(Den,qu))
# ..\MATLAB_files\SecondCauer.m:30
            R[i]=1 / qu
# ..\MATLAB_files\SecondCauer.m:31
        else:
            if i == 0:
                qu=0
                re=Num
# ..\MATLAB_files\SecondCauer.m:34
            else:
                qu=Num[idxN] / Den[idxD]
# ..\MATLAB_files\SecondCauer.m:36
                re=Num - roll(Den*qu,1)
# ..\MATLAB_files\SecondCauer.m:38
                C[i]=1 / qu
# ..\MATLAB_files\SecondCauer.m:39
        Num=copy(Den)
# ..\MATLAB_files\SecondCauer.m:42
        Den=copy(re)
# ..\MATLAB_files\SecondCauer.m:43
    
    if C[i] != 0:
        R[i + 1]=1 / Num[0]
# ..\MATLAB_files\SecondCauer.m:47
    
    line = []
    line.append(['* Python created *.cir-file for NGSpice *'])
    line.append(['.TITLE Second Cauer'])
#    line.append(['.lib C:\\Cadence\\SPB_17.2\\tools\\pspice\\library\\eval.lib'])
    line.append(['vin 1 0 DC 0 AC 1'])
    if size(nonzero(C!=0)[0])==0:
        k = 0
    else:
        k = nonzero(C!=0)[0][-1]//2 + 1
    for i in range(0,k+1):
        if R[2*i] != 0:
            line.append(['R'+str(i+1)+' '+str(i+1)+' 0 '+str(R[2*i])])
        if C[2*i+1] != 0:
            line.append(['C'+str(i+2)+' '+str(i+1)+' '+str(i+2)+' '+str(C[2*i+1])])    
    line.append(['R'+str(i + 2)+' '+str(i+1)+' 0 '+str(R[2*k])])
    line.append(['.control'])
    line.append(['set wr_singlescale'])
    line.append(['save i(vin) 1 v(1)'])
    line.append(['AC DEC '+str(fstep)+' '+str(fl)+' '+str(fh)])
    line.append(['wrdata '+filename+'.out '+ 'v(1) i(vin)'])
    line.append(['.ENDC'])
    line.append(['.END'])

# ..\MATLAB_files\SecondCauer.m:65
    # writing netlist to file
    f=open(filename+'.cir','w')
# ..\MATLAB_files\SecondCauer.m:68
    for i in range(0,len(line)):
        f.write(str(line[i][0])+'\n');
    
    f.close()
# ..\MATLAB_files\SecondCauer.m:72
    return filename
    
if __name__ == '__main__':
    pass
    