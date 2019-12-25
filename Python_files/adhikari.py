# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\adhikari.m
import numpy
from numpy import * 
from math import * 
import sys, os
frozen = 'not'
   
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

#    print(R)
#    print(C)
    
    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        frozen = 'ever so'
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    
    filename=bundle_dir+'\Pspice_files\Adhikari'
    
    line = []
    line.append(['* Python created *.cir-file for NGSpice *'])
    line.append(['.TITLE Adhikari'])
#    line.append(['.lib C:\\Cadence\\SPB_17.2\\tools\\pspice\\library\\eval.lib'])
    line.append(['vin 1 0 DC 0 AC 1'])
    line.append(['R'+str(1)+' '+str(1)+' '+str(2)+' '+str(R0)])
    line.append(['C'+str(1)+' '+str(1)+' '+str(2)+' '+str(C0)])
    for i in range(0,N + 1):
        line.append(['R'+str(i + 2)+' '+str(i + 2)+' '+str(i + 3)+' '+str(R[i])])
        line.append(['C'+str(i + 2)+' '+str(i + 2)+' '+str(i + 3)+' '+str(C[i])])
    line.append(['R'+str(N + 3)+' '+str(N + 3)+' 0 '+str(R[N + 1])])
    line.append(['.control'])
    line.append(['set wr_singlescale'])
    line.append(['save i(vin) 1 v(1)'])
    line.append(['AC DEC '+str(fstep)+' '+str(fl)+' '+str(fh)])
    line.append(['wrdata '+filename+'.out '+ 'v(1) i(vin)'])
    line.append(['.ENDC'])
    line.append(['.END'])

    # writing netlist to file
    f=open((filename+'.cir'),'w')
    for i in range(0,len(line)):
        f.write(str(line[i][0])+'\n')
    
    f.close()
    return filename
    
if __name__ == '__main__':
    pass
    