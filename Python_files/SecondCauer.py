# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\SecondCauer.m
import copy
    
def SecondCauer_func(Numerator=None,Denominator=None,fl=None,fh=None,fstep=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    q=copy.copy(Numerator)
# ..\MATLAB_files\SecondCauer.m:3
    p=copy.copy(Denominator)
# ..\MATLAB_files\SecondCauer.m:4
    filename='D:\\DocumentsHDD\\BTP\\GUIapp\\Pspice_files\\SecondCauer'
# ..\MATLAB_files\SecondCauer.m:6
    Num=copy.copy(p)
# ..\MATLAB_files\SecondCauer.m:8
    Den=copy.copy(q)
# ..\MATLAB_files\SecondCauer.m:9
    M,N=size(q,nargout=2)
# ..\MATLAB_files\SecondCauer.m:11
    R=zeros(1,dot(2,N))
# ..\MATLAB_files\SecondCauer.m:13
    C=zeros(1,dot(2,N) + 1)
# ..\MATLAB_files\SecondCauer.m:14
    for i in arange(1,dot(2,N) + 1,1).reshape(-1):
        idxN=find(abs(Num) > 1e-05,1,'last')
# ..\MATLAB_files\SecondCauer.m:18
        idxD=find(abs(Den) > 1e-05,1,'last')
# ..\MATLAB_files\SecondCauer.m:19
        Num[arange(idxN + 1,end())]=0
# ..\MATLAB_files\SecondCauer.m:21
        Den[arange(idxD + 1,end())]=0
# ..\MATLAB_files\SecondCauer.m:22
        if isempty(idxD):
            break
        if idxN == idxD:
            qu=Num(idxN) / Den(idxD)
# ..\MATLAB_files\SecondCauer.m:29
            re=Num - (dot(Den,qu))
# ..\MATLAB_files\SecondCauer.m:30
            R[i]=1 / qu
# ..\MATLAB_files\SecondCauer.m:31
        else:
            if i == 1:
                qu=0
# ..\MATLAB_files\SecondCauer.m:34
            else:
                qu=Num(idxN) / Den(idxD)
# ..\MATLAB_files\SecondCauer.m:36
            re=Num - circshift((dot(Den,qu)),concat([0,1]))
# ..\MATLAB_files\SecondCauer.m:38
            C[i]=1 / qu
# ..\MATLAB_files\SecondCauer.m:39
        Num=copy.copy(Den)
# ..\MATLAB_files\SecondCauer.m:42
        Den=copy.copy(re)
# ..\MATLAB_files\SecondCauer.m:43
    
    if C(i) != 0:
        R[i + 1]=1 / Num(1)
# ..\MATLAB_files\SecondCauer.m:47
    
    line[1]=concat(['* Matlab created *.cir-file *'])
# ..\MATLAB_files\SecondCauer.m:50
    line[2]=concat(['.lib C:\\Cadence\\SPB_17.2\\tools\\pspice\\library\\eval.lib'])
# ..\MATLAB_files\SecondCauer.m:51
    line[3]=concat(['VIN        1   0   AC 1V'])
# ..\MATLAB_files\SecondCauer.m:52
    k=find(C != 0,1,'last') / 2
# ..\MATLAB_files\SecondCauer.m:53
    for i in arange(1,k,1).reshape(-1):
        if R(dot(2,i) - 1) != 0:
            line[dot(2,i) + 2]=concat(['R',num2str(i),' ',num2str(i),' 0 ',num2str(R(dot(2,i) - 1))])
# ..\MATLAB_files\SecondCauer.m:56
        if C(dot(2,i)) != 0:
            line[dot(2,i) + 3]=concat(['C',num2str(i + 1),' ',num2str(i),' ',num2str(i + 1),' ',num2str(C(dot(2,i)))])
# ..\MATLAB_files\SecondCauer.m:59
    
    line[length(C) + 4]=concat(['R',num2str(i + 2),' ',num2str(i + 1),' 0 ',num2str(R(dot(2,k) + 1))])
# ..\MATLAB_files\SecondCauer.m:62
    line[length(C) + 5]=concat(['.AC DEC ',num2str(fstep),' ',num2str(fl),' ',num2str(fh)])
# ..\MATLAB_files\SecondCauer.m:63
    line[length(C) + 6]=concat(['.PRINT AC VM(1) VP(1) IM(VIN) IP(VIN)'])
# ..\MATLAB_files\SecondCauer.m:64
    line[length(C) + 7]=concat(['.END'])
# ..\MATLAB_files\SecondCauer.m:65
    # writing netlist to file
    fid=fopen(concat([filename,'.cir']),'w')
# ..\MATLAB_files\SecondCauer.m:68
    for i in arange(1,length(line)).reshape(-1):
        fwrite(fid,concat([line[i],char(13),char(10)]),'char')
    
    fid=fclose(fid)
# ..\MATLAB_files\SecondCauer.m:72
    return filename
    
if __name__ == '__main__':
    pass
    