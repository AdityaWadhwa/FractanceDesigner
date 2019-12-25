# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\FirstCauer.m
from copy import copy
import numpy
from numpy import * 
from math import * 
import sys, os
frozen = 'not'
    
def FirstCauer_func(Numerator=None,Denominator=None,fl=None,fh=None,fstep=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    q=copy(Denominator)
# ..\MATLAB_files\FirstCauer.m:3
    p=copy(Numerator)

    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        frozen = 'ever so'
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    
    filename=bundle_dir+'\Pspice_files\FirstCauer'
    
# ..\MATLAB_files\FirstCauer.m:6
    Num=copy(p)
# ..\MATLAB_files\FirstCauer.m:8
    Den=copy(q)
# ..\MATLAB_files\FirstCauer.m:9
    N=size(q)
# ..\MATLAB_files\FirstCauer.m:11
    R=zeros(2*N)
# ..\MATLAB_files\FirstCauer.m:13
    C=zeros(2*N+1)
# ..\MATLAB_files\FirstCauer.m:14
    for i in range(0,2*N+2):
        if size(nonzero(abs(Num) > 1e-05)[0])==0:
            break
        else:
            idxN=nonzero(abs(Num) > 1e-05)[0][0]
# ..\MATLAB_files\FirstCauer.m:18
        if size(nonzero(abs(Den) > 1e-05)[0])==0:
            break
        else:
            idxD=nonzero(abs(Den) > 1e-05)[0][0]
# ..\MATLAB_files\FirstCauer.m:19
        Num[0:idxN]=numpy.zeros([1,idxN])
# ..\MATLAB_files\FirstCauer.m:21
        Den[0:idxN]=numpy.zeros([1,idxN])
# ..\MATLAB_files\FirstCauer.m:22
#        if idxD==[]:
#            break
        if idxN == idxD:
            qu=Num[idxN] / Den[idxD]
# ..\MATLAB_files\FirstCauer.m:29
            re=Num - (dot(Den,qu))
# ..\MATLAB_files\FirstCauer.m:30
            R[i]=qu
# ..\MATLAB_files\FirstCauer.m:31
        else:
            if i == 0:
                qu=0
# ..\MATLAB_files\FirstCauer.m:34
            else:
                qu=Num[idxN] / Den[idxD]
# ..\MATLAB_files\FirstCauer.m:36
            re=Num - roll(Den*qu,-1)
# ..\MATLAB_files\FirstCauer.m:38
            C[i]=qu
# ..\MATLAB_files\FirstCauer.m:39
        Num=copy(Den)
# ..\MATLAB_files\FirstCauer.m:41
        Den=copy(re)
# ..\MATLAB_files\FirstCauer.m:42
    
    if C[i] != 0:
        R[i+1]=1 / re(N)
# ..\MATLAB_files\FirstCauer.m:46
    
    line = []
    line.append(['* Python created *.cir-file for NGSpice *'])
    line.append(['.TITLE First Cauer'])
#    line.append(['.lib C:\\Cadence\\SPB_17.2\\tools\\pspice\\library\\eval.lib'])
    line.append(['vin 1 0 DC 0 AC 1'])
    for i in range(0,nonzero(C>0)[0][-1]//2):
        line.append(['R'+str(i+1)+' '+str(i+1)+' '+str(i+2)+' '+str(R[2*i])])
        line.append(['C'+str(i+2)+' '+str(i+2)+' 0 '+str(C[2*i+1])])
    if R[len(R) - 2] != 0:
        line.append(['R'+str(i + 2)+' '+str(i + 2)+' 0 '+str(R[len(R) - 2])])
    line.append(['.control'])
    line.append(['set wr_singlescale'])
    line.append(['save i(vin) 1 v(1)'])
    line.append(['AC DEC '+str(fstep)+' '+str(fl)+' '+str(fh)])
    line.append(['wrdata '+filename+'.out '+ 'v(1) i(vin)'])
    line.append(['.ENDC'])
    line.append(['.END'])

# ..\MATLAB_files\FirstCauer.m:59
    # writing netlist to file
    f=open(filename+'.cir','w')
# ..\MATLAB_files\FirstCauer.m:62
    for i in range(0,len(line)):
        f.write(str(line[i][0])+'\n');
    
    f.close()
# ..\MATLAB_files\FirstCauer.m:66
    return filename
    
if __name__ == '__main__':
    pass
    