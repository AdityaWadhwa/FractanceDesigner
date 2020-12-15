# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\valsa_func.m
import numpy
from numpy import * 
from math import * 
import sys, os
frozen = 'not'

def valsa_func(F=None,alp=None,fl=None,fu=None,fstep=None,phierr=None,*args,**kwargs):
    varargin = args
    nargin = 6 + len(varargin)

    if (alp > 0):
        alp=- alp
# ..\MATLAB_files\valsa_func.m:3
    
    wl=dot(dot(2,pi),fl)
# ..\MATLAB_files\valsa_func.m:6
    wu=dot(dot(2,pi),fu)
# ..\MATLAB_files\valsa_func.m:7
    ab=0.24 / (1 + phierr)
# ..\MATLAB_files\valsa_func.m:8
    logtena=dot((abs(alp)),(log10(ab)))
# ..\MATLAB_files\valsa_func.m:10
    a=10 ** logtena
# ..\MATLAB_files\valsa_func.m:11
    b=ab / a
# ..\MATLAB_files\valsa_func.m:12
    m=ceil(1 - ((log10(wu / wl)) / (log10(ab))))
# ..\MATLAB_files\valsa_func.m:14
    R=numpy.zeros([m,1])
# ..\MATLAB_files\valsa_func.m:16
    C=numpy.zeros([m,1])
# ..\MATLAB_files\valsa_func.m:17
    # we have to choose C1 and R1 so decision to keep C1 constant
    C[0]=1e-06
# ..\MATLAB_files\valsa_func.m:19
    R[0]=1 / (dot(wl,C[0]))
# ..\MATLAB_files\valsa_func.m:20
    wav=sqrt(dot(wu,wl))
# ..\MATLAB_files\valsa_func.m:22
    Rp=dot(R[0],(1 - a)) / a
# ..\MATLAB_files\valsa_func.m:24
    Cp=dot(C[0],(b ** m)) / (1 - b)
# ..\MATLAB_files\valsa_func.m:25
    for i in range(1,m):
        R[i]=dot(R[0],(a ** (i - 1)))
# ..\MATLAB_files\valsa_func.m:28
        C[i]=dot(C[0],(b ** (i - 1)))
# ..\MATLAB_files\valsa_func.m:29
    
    Y=0
# ..\MATLAB_files\valsa_func.m:31
    for i in range(0,m):
        Y=Y + (dot(dot(1j,wav),C[i])) / ((dot(dot(dot(1j,wav),C[i]),R[i])) + 1)
# ..\MATLAB_files\valsa_func.m:33
    
    Y=Y + (1 / Rp) + dot(dot(1j,wav),Cp)
# ..\MATLAB_files\valsa_func.m:36
    Z=1 / (abs(Y))
# ..\MATLAB_files\valsa_func.m:38
    Dreali=dot(Z,(wav ** abs(alp)))
# ..\MATLAB_files\valsa_func.m:40
    
    CR=F / Dreali
# ..\MATLAB_files\valsa_func.m:42
    
    R=multiply(R,CR)
# ..\MATLAB_files\valsa_func.m:44
    Rp=dot(Rp,CR)
# ..\MATLAB_files\valsa_func.m:45
    C=C / CR
# ..\MATLAB_files\valsa_func.m:46
    Cp=Cp / CR
    
    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        frozen = 'ever so'
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    
    filename=os.path.join(bundle_dir,'Pspice_files\Valsa')
    
    line = []
    line.append(['* Python created *.cir-file for NGSpice *'])
    line.append(['.TITLE Adhikari'])
#    line.append(['.lib C:\\Cadence\\SPB_17.2\\tools\\pspice\\library\\eval.lib'])
    line.append(['vin 1 0 DC 0 AC 1'])
    line.append(['Rp'+' '+str(1)+' '+str(0)+' '+str(Rp)])
    line.append(['Cp'+' '+str(1)+' '+str(0)+' '+str(Cp[0])])
    for i in range(1,m):
        line.append(['R'+str(i)+' '+str(1)+' '+str(i + 1)+' '+str(R[i][0])])
        line.append(['C'+str(i)+' '+str(i + 1)+' '+str(0)+' '+str(C[i][0])])
    line.append(['.control'])
    line.append(['set wr_singlescale'])
    line.append(['save i(vin) 1 v(1)'])
    line.append(['AC DEC '+str(fstep)+' '+str(fl)+' '+str(fu)])
    line.append(['wrdata '+filename+'.out '+ 'v(1) i(vin)'])
    line.append(['.ENDC'])
    line.append(['.END'])

#    print(line)
    # writing netlist to file
    f=open((filename+'.cir'),'w')
# ..\MATLAB_files\valsa_func.m:65
    for i in range(0,len(line)):
        f.write(str(line[i][0])+'\n')
     
    f.close()
# ..\MATLAB_files\valsa_func.m:69
    return filename
    
if __name__ == '__main__':
    pass
    