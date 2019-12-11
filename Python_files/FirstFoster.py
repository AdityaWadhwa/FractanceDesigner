# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\FirstFoster.m
import copy
    
def FirstFoster_func(Num=None,Den=None,fl=None,fh=None,fstep=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    b=copy.copy(Num)
# ..\MATLAB_files\FirstFoster.m:3
    a=copy.copy(Den)
# ..\MATLAB_files\FirstFoster.m:4
    filename='D:\\DocumentsHDD\\BTP\\GUIapp\\Pspice_files\\FirstFoster'
# ..\MATLAB_files\FirstFoster.m:6
    r,p,k=residue(b,a,nargout=3)
# ..\MATLAB_files\FirstFoster.m:8
    
    C=1.0 / r
# ..\MATLAB_files\FirstFoster.m:10
    R=- r / p
# ..\MATLAB_files\FirstFoster.m:11
    if logical_not(isempty(k)):
        R=vertcat(R,k)
# ..\MATLAB_files\FirstFoster.m:14
    
    line[1]=concat(['* Matlab created *.cir-file *'])
# ..\MATLAB_files\FirstFoster.m:17
    line[2]=concat(['.lib C:\\Cadence\\SPB_17.2\\tools\\pspice\\library\\eval.lib'])
# ..\MATLAB_files\FirstFoster.m:18
    line[3]=concat(['VIN        1   0   AC 1V'])
# ..\MATLAB_files\FirstFoster.m:19
    for i in arange(1,length(C),1).reshape(-1):
        if R(i) != - Inf:
            line[dot(2,i) + 2]=concat(['R',num2str(i),' ',num2str(i),' ',num2str(i + 1),' ',num2str(R(i))])
# ..\MATLAB_files\FirstFoster.m:22
        line[dot(2,i) + 3]=concat(['C',num2str(i),' ',num2str(i),' ',num2str(i + 1),' ',num2str(C(i))])
# ..\MATLAB_files\FirstFoster.m:24
    
    line[dot(2,length(C)) + 5]=concat(['R',num2str(i + 1),' ',num2str(i + 1),' 0 ',num2str(R(length(R)))])
# ..\MATLAB_files\FirstFoster.m:26
    line[dot(2,length(C)) + 6]=concat(['.AC DEC ',num2str(fstep),' ',num2str(fl),' ',num2str(fh)])
# ..\MATLAB_files\FirstFoster.m:27
    line[dot(2,length(C)) + 7]=concat(['.PRINT AC VM(1) VP(1) IM(VIN) IP(VIN)'])
# ..\MATLAB_files\FirstFoster.m:28
    line[dot(2,length(C)) + 8]=concat(['.END'])
# ..\MATLAB_files\FirstFoster.m:29
    # writing netlist to file
    fid=fopen(concat([filename,'.cir']),'w')
# ..\MATLAB_files\FirstFoster.m:32
    for i in arange(1,length(line)).reshape(-1):
        fwrite(fid,concat([line[i],char(13),char(10)]),'char')
    
    fid=fclose(fid)
# ..\MATLAB_files\FirstFoster.m:36
    return filename
    
if __name__ == '__main__':
    pass
    