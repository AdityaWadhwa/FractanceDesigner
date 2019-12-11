# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\FirstCauer.m
import copy
    
def FirstCauer_func(Numerator=None,Denominator=None,fl=None,fh=None,fstep=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    q=copy.copy(Denominator)
# ..\MATLAB_files\FirstCauer.m:3
    p=copy.copy(Numerator)
# ..\MATLAB_files\FirstCauer.m:4
    filename='D:\\DocumentsHDD\\BTP\\GUIapp\\Pspice_files\\FirstCauer'
# ..\MATLAB_files\FirstCauer.m:6
    Num=copy.copy(p)
# ..\MATLAB_files\FirstCauer.m:8
    Den=copy.copy(q)
# ..\MATLAB_files\FirstCauer.m:9
    M,N=size(q,nargout=2)
# ..\MATLAB_files\FirstCauer.m:11
    R=zeros(1,dot(2,N))
# ..\MATLAB_files\FirstCauer.m:13
    C=zeros(1,dot(2,N) + 1)
# ..\MATLAB_files\FirstCauer.m:14
    for i in arange(1,dot(2,N) + 1,1).reshape(-1):
        idxN=find(abs(Num) > 1e-05,1,'first')
# ..\MATLAB_files\FirstCauer.m:18
        idxD=find(abs(Den) > 1e-05,1,'first')
# ..\MATLAB_files\FirstCauer.m:19
        Num[arange(1,idxN - 1)]=0
# ..\MATLAB_files\FirstCauer.m:21
        Den[arange(1,idxD - 1)]=0
# ..\MATLAB_files\FirstCauer.m:22
        if isempty(idxD):
            break
        if idxN == idxD:
            qu=Num(idxN) / Den(idxD)
# ..\MATLAB_files\FirstCauer.m:29
            re=Num - (dot(Den,qu))
# ..\MATLAB_files\FirstCauer.m:30
            R[i]=qu
# ..\MATLAB_files\FirstCauer.m:31
        else:
            if i == 1:
                qu=0
# ..\MATLAB_files\FirstCauer.m:34
            else:
                qu=Num(idxN) / Den(idxD)
# ..\MATLAB_files\FirstCauer.m:36
            re=Num - circshift((dot(Den,qu)),concat([0,- 1]))
# ..\MATLAB_files\FirstCauer.m:38
            C[i]=qu
# ..\MATLAB_files\FirstCauer.m:39
        Num=copy.copy(Den)
# ..\MATLAB_files\FirstCauer.m:41
        Den=copy.copy(re)
# ..\MATLAB_files\FirstCauer.m:42
    
    if C(i) != 0:
        R[i + 1]=1 / re(N)
# ..\MATLAB_files\FirstCauer.m:46
    
    line[1]=concat(['* Matlab created *.cir-file *'])
# ..\MATLAB_files\FirstCauer.m:49
    line[2]=concat(['.lib C:\\Cadence\\SPB_17.2\\tools\\pspice\\library\\eval.lib'])
# ..\MATLAB_files\FirstCauer.m:50
    line[3]=concat(['VIN        1   0   AC 1V'])
# ..\MATLAB_files\FirstCauer.m:51
    for i in arange(1,find(C != 0,1,'last') / 2,1).reshape(-1):
        line[dot(2,i) + 2]=concat(['R',num2str(i),' ',num2str(i),' ',num2str(i + 1),' ',num2str(R(dot(2,i) - 1))])
# ..\MATLAB_files\FirstCauer.m:53
        line[dot(2,i) + 3]=concat(['C',num2str(i + 1),' ',num2str(i + 1),' 0 ',num2str(C(dot(2,i)))])
# ..\MATLAB_files\FirstCauer.m:54
    
    line[length(C) + 4]=concat(['R',num2str(i + 2),' ',num2str(i + 1),' 0 ',num2str(R(length(R) - 1))])
# ..\MATLAB_files\FirstCauer.m:56
    line[length(C) + 5]=concat(['.AC DEC ',num2str(fstep),' ',num2str(fl),' ',num2str(fh)])
# ..\MATLAB_files\FirstCauer.m:57
    line[length(C) + 6]=concat(['.PRINT AC VM(1) VP(1) IM(VIN) IP(VIN)'])
# ..\MATLAB_files\FirstCauer.m:58
    line[length(C) + 7]=concat(['.END'])
# ..\MATLAB_files\FirstCauer.m:59
    # writing netlist to file
    fid=fopen(concat([filename,'.cir']),'w')
# ..\MATLAB_files\FirstCauer.m:62
    for i in arange(1,length(line)).reshape(-1):
        fwrite(fid,concat([line[i],char(13),char(10)]),'char')
    
    fid=fclose(fid)
# ..\MATLAB_files\FirstCauer.m:66
    return filename
    
if __name__ == '__main__':
    pass
    