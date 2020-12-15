# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\FirstFoster.m
from copy import copy
from numpy import * 
from math import * 
from scipy.signal import residue
import sys, os
frozen = 'not'
    
def FirstFoster_func(Num=None,Den=None,fl=None,fh=None,fstep=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    b=copy(Num)
# ..\MATLAB_files\FirstFoster.m:3
    a=copy(Den)

    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        frozen = 'ever so'
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    
    filename=os.path.join(bundle_dir,'Pspice_files\FirstFoster')
    
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
    line.append(['* Python created *.cir-file for NGSpice *'])
    line.append(['.TITLE First Foster'])
#    line.append(['.lib C:\\Cadence\\SPB_17.2\\tools\\pspice\\library\\eval.lib'])
    line.append(['vin 1 0 DC 0 AC 1'])
    for i in range(0,len(C)):
        if R[i] != - Inf:
            line.append(['R'+str(i+1)+' '+str(i+1)+' '+str(i+2)+' '+str(R[i])])
        line.append(['C'+str(i+1)+' '+str(i+1)+' '+str(i+2)+' '+str(C[i])])
    line.append(['R'+str(i + 2)+' '+str(i + 2)+' 0 '+str(R[len(R)-1])])
    line.append(['.control'])
    line.append(['set wr_singlescale'])
    line.append(['save i(vin) 1 v(1)'])
    line.append(['AC DEC '+str(fstep)+' '+str(fl)+' '+str(fh)])
    line.append(['wrdata '+filename+'.out '+ 'v(1) i(vin)'])
    line.append(['.ENDC'])
    line.append(['.END'])

# ..\MATLAB_files\FirstFoster.m:29
    # writing netlist to file
    f=open(filename+'.cir','w')
# ..\MATLAB_files\FirstFoster.m:32
    for i in range(0,len(line)):
        f.write(str(line[i][0])+'\n')
    
    f.close()
# ..\MATLAB_files\FirstFoster.m:36
    return filename
    
if __name__ == '__main__':
    pass
    