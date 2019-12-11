# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\SecondFoster.m
import copy
    
def SecondFoster_func(Num=None,Den=None,fl=None,fh=None,fstep=None,*args,**kwargs):
    varargin = args
    nargin = 5 + len(varargin)

    b=copy.copy(Num)
# ..\MATLAB_files\SecondFoster.m:3
    a=copy.copy(Den)
# ..\MATLAB_files\SecondFoster.m:4
    filename='D:\\DocumentsHDD\\BTP\\GUIapp\\Pspice_files\\SecondFoster'
# ..\MATLAB_files\SecondFoster.m:6
    if find(a > 0,1,'first') > find(b > 0,1,'first'):
        Clast=a(1) / b(1)
# ..\MATLAB_files\SecondFoster.m:9
        a=a - concat([dot(Clast,b),0])
# ..\MATLAB_files\SecondFoster.m:10
        a=a(arange(2,end()))
# ..\MATLAB_files\SecondFoster.m:11
    else:
        Clast=0
# ..\MATLAB_files\SecondFoster.m:13
    
    Rlast=b(find(b > 0,1,'last')) / a(find(a > 0,1,'last'))
# ..\MATLAB_files\SecondFoster.m:16
    a=a - dot((1 / Rlast),b)
# ..\MATLAB_files\SecondFoster.m:17
    
    r,p,k=residue(a,b,nargout=3)
# ..\MATLAB_files\SecondFoster.m:19
    
    for i in arange(1,length(p),1).reshape(-1):
        Num=copy(a)
# ..\MATLAB_files\SecondFoster.m:22
        Den=conv(b,concat([1,0]))
# ..\MATLAB_files\SecondFoster.m:23
        Den=deconv(Den,concat([1,- p(i)]))
# ..\MATLAB_files\SecondFoster.m:24
        r[i]=polyval(Num,p(i)) / polyval(Den,p(i))
# ..\MATLAB_files\SecondFoster.m:25
    
    
    R=1.0 / r
# ..\MATLAB_files\SecondFoster.m:28
    C=- r / p
# ..\MATLAB_files\SecondFoster.m:29
    if Rlast != 0:
        R=vertcat(R,Rlast)
# ..\MATLAB_files\SecondFoster.m:32
    
    if Clast != 0:
        R=vertcat(R,0)
# ..\MATLAB_files\SecondFoster.m:37
        C=vertcat(C,Clast)
# ..\MATLAB_files\SecondFoster.m:38
    
    line[1]=concat(['* Matlab created *.cir-file *'])
# ..\MATLAB_files\SecondFoster.m:41
    line[2]=concat(['.lib C:\\Cadence\\SPB_17.2\\tools\\pspice\\library\\eval.lib'])
# ..\MATLAB_files\SecondFoster.m:42
    line[3]=concat(['VIN        1   0   AC 1V'])
# ..\MATLAB_files\SecondFoster.m:43
    for i in arange(1,length(C),1).reshape(-1):
        line[dot(2,i) + 2]=concat(['R',num2str(i),' 1 ',num2str(i + 1),' ',num2str(R(i))])
# ..\MATLAB_files\SecondFoster.m:45
        line[dot(2,i) + 3]=concat(['C',num2str(i),' ',num2str(i + 1),' 0 ',num2str(C(i))])
# ..\MATLAB_files\SecondFoster.m:46
    
    line[dot(2,length(C)) + 5]=concat(['R',num2str(length(R)),' 1 ',num2str(i + 1),' ',num2str(R(length(R)))])
# ..\MATLAB_files\SecondFoster.m:48
    line[dot(2,length(C)) + 6]=concat(['.AC DEC ',num2str(fstep),' ',num2str(fl),' ',num2str(fh)])
# ..\MATLAB_files\SecondFoster.m:49
    line[dot(2,length(C)) + 7]=concat(['.PRINT AC VM(1) VP(1) IM(VIN) IP(VIN)'])
# ..\MATLAB_files\SecondFoster.m:50
    line[dot(2,length(C)) + 8]=concat(['.END'])
# ..\MATLAB_files\SecondFoster.m:51
    # writing netlist to file
    fid=fopen(concat([filename,'.cir']),'w')
# ..\MATLAB_files\SecondFoster.m:54
    for i in arange(1,length(line)).reshape(-1):
        fwrite(fid,concat([line[i],char(13),char(10)]),'char')
    
    fid=fclose(fid)
# ..\MATLAB_files\SecondFoster.m:58
    return filename
    
if __name__ == '__main__':
    pass
    