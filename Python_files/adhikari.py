# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\adhikari.m
import numpy
from numpy import * 
from math import * 
   
def adhikari_func(F=None,alp=None,fl=None,fh=None,fstep=None,N=None,*args,**kwargs):
    varargin = args
    nargin = 6 + len(varargin)

    if alp < 0:
        alp=abs(alp)
# ..\MATLAB_files\adhikari.m:4
        F=1 / F
# ..\MATLAB_files\adhikari.m:5
    
    R=[]
# ..\MATLAB_files\adhikari.m:8
    C=[]
# ..\MATLAB_files\adhikari.m:9
    b=exp(dot(- 1.5,((1 - alp) ** (2 / 3))))
# ..\MATLAB_files\adhikari.m:11
    b=b - remainder(b,0.1)
# ..\MATLAB_files\adhikari.m:12
    a=exp(dot((alp / (1 - alp)),log(b)))
# ..\MATLAB_files\adhikari.m:14
    a=round(a,4)
# ..\MATLAB_files\adhikari.m:15
    t=dot(11.1,((b ** 2) / fl))
# ..\MATLAB_files\adhikari.m:17
    w=dot(dot(2,pi),((dot(fl,fh)) ** 0.5))
# ..\MATLAB_files\adhikari.m:19
    K=(0.5 - 1 / log(b)) / (1 + dot(dot(1j,w),t))
# ..\MATLAB_files\adhikari.m:21
    p=dot(a,b)
# ..\MATLAB_files\adhikari.m:22
    for i in arange(1,N + 1,1).reshape(-1):
        K=K + (a ** i) / (1 + dot(dot(dot(1j,w),p ** i),t))
# ..\MATLAB_files\adhikari.m:24
    
    K=K - (a ** (N + 1)) / log(b)
# ..\MATLAB_files\adhikari.m:26
    K=abs(K)
# ..\MATLAB_files\adhikari.m:27
    r=1 / (dot(dot(K,F),w ** alp))
# ..\MATLAB_files\adhikari.m:29
    c=t / r
# ..\MATLAB_files\adhikari.m:30
    R0=dot((0.5 - 1 / log(b)),r)
# ..\MATLAB_files\adhikari.m:32
    C0=c / (0.5 - 1 / log(b))
# ..\MATLAB_files\adhikari.m:33
    R = append(R,dot(power(a,[arange(1,N+1)]),r))
# ..\MATLAB_files\adhikari.m:35
    C = append(C,dot(power(b,[arange(1,N+1)]),c))
# ..\MATLAB_files\adhikari.m:36
    R = append(R,dot(dot(0.5,a ** (N + 1)),r))
# ..\MATLAB_files\adhikari.m:38
    C = append(C,dot(dot(2,b ** (N + 1)),c))
# ..\MATLAB_files\adhikari.m:39
    R = append(R,dot(dot(- a ** (N + 1),r),(1 / log(a))))

    print(R)
    print(C)
# ..\MATLAB_files\adhikari.m:41
    filename='D:\\DocumentsHDD\\BTP\\GUIapp\\Pspice_files\\Adhikari'

    line = []
# ..\MATLAB_files\adhikari.m:43
    line.append(['* Matlab created *.cir-file *'])
# ..\MATLAB_files\adhikari.m:45
    line.append(['.lib C:\\Cadence\\SPB_17.2\\tools\\pspice\\library\\eval.lib'])
# ..\MATLAB_files\adhikari.m:46
    line.append(['VIN        1   0   AC 1V'])
# ..\MATLAB_files\adhikari.m:47
    line.append(['R'+str(1)+' '+str(1)+' '+str(2)+' '+str(R0)])
# ..\MATLAB_files\adhikari.m:48
    line.append(['C'+str(1)+' '+str(1)+' '+str(2)+' '+str(C0)])
# ..\MATLAB_files\adhikari.m:49
    for i in range(0,N + 1):
        line.append(['R'+str(i + 2)+' '+str(i + 2)+' '+str(i + 3)+' '+str(R[i])])
# ..\MATLAB_files\adhikari.m:51
        line.append(['C'+str(i + 2)+' '+str(i + 2)+' '+str(i + 3)+' '+str(C[i])])
# ..\MATLAB_files\adhikari.m:52
    
    line.append(['R'+str(N + 3)+' '+str(N + 3)+' 0 '+str(R[N + 1])])
# ..\MATLAB_files\adhikari.m:54
    line.append(['.AC DEC '+str(fstep)+' '+str(fl)+' '+str(fh)])
# ..\MATLAB_files\adhikari.m:55
    line.append(['.PRINT AC VM(1) VP(1) IM(VIN) IP(VIN)'])
# ..\MATLAB_files\adhikari.m:56
    line.append(['.END'])
# ..\MATLAB_files\adhikari.m:57
    # writing netlist to file
    f=open((filename+'.cir'),'w')
# ..\MATLAB_files\adhikari.m:60
    for i in range(0,len(line)):
        f.write(str(line[i][0])+'\n')
    
    f.close()
# ..\MATLAB_files\adhikari.m:64
    return filename
    
if __name__ == '__main__':
    pass
    