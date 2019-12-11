# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\adhikari.m

    
def adhikari_func(F=None,alp=None,fl=None,fh=None,fstep=None,N=None,*args,**kwargs):
    varargin = args
    nargin = 6 + len(varargin)

    if alp < 0:
        alp=abs(alp)
# ..\MATLAB_files\adhikari.m:4
        F=1 / F
# ..\MATLAB_files\adhikari.m:5
    
    R=zeros(1,N + 2)
# ..\MATLAB_files\adhikari.m:8
    C=zeros(1,N + 1)
# ..\MATLAB_files\adhikari.m:9
    b=exp(dot(- 1.5,((1 - alp) ** (2 / 3))))
# ..\MATLAB_files\adhikari.m:11
    b=b - rem(b,0.1)
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
    R[arange(1,N)]=dot(a ** concat([arange(1,N,1)]),r)
# ..\MATLAB_files\adhikari.m:35
    C[arange(1,N)]=dot(b ** concat([arange(1,N,1)]),c)
# ..\MATLAB_files\adhikari.m:36
    R[N + 1]=dot(dot(0.5,a ** (N + 1)),r)
# ..\MATLAB_files\adhikari.m:38
    C[N + 1]=dot(dot(2,b ** (N + 1)),c)
# ..\MATLAB_files\adhikari.m:39
    R[N + 2]=dot(dot(- a ** (N + 1),r),(1 / log(a)))
# ..\MATLAB_files\adhikari.m:41
    filename='D:\\DocumentsHDD\\BTP\\GUIapp\\Pspice_files\\Adhikari'
# ..\MATLAB_files\adhikari.m:43
    line[1]=concat(['* Matlab created *.cir-file *'])
# ..\MATLAB_files\adhikari.m:45
    line[2]=concat(['.lib C:\\Cadence\\SPB_17.2\\tools\\pspice\\library\\eval.lib'])
# ..\MATLAB_files\adhikari.m:46
    line[3]=concat(['VIN        1   0   AC 1V'])
# ..\MATLAB_files\adhikari.m:47
    line[4]=concat(['R',num2str(1),' ',num2str(1),' ',num2str(2),' ',num2str(R0)])
# ..\MATLAB_files\adhikari.m:48
    line[5]=concat(['C',num2str(1),' ',num2str(1),' ',num2str(2),' ',num2str(C0)])
# ..\MATLAB_files\adhikari.m:49
    for i in arange(1,N + 1,1).reshape(-1):
        line[dot(2,i) + 4]=concat(['R',num2str(i + 1),' ',num2str(i + 1),' ',num2str(i + 2),' ',num2str(R(i))])
# ..\MATLAB_files\adhikari.m:51
        line[dot(2,i) + 5]=concat(['C',num2str(i + 1),' ',num2str(i + 1),' ',num2str(i + 2),' ',num2str(C(i))])
# ..\MATLAB_files\adhikari.m:52
    
    line[dot(2,N) + 8]=concat(['R',num2str(N + 3),' ',num2str(N + 3),' 0 ',num2str(R(N + 2))])
# ..\MATLAB_files\adhikari.m:54
    line[dot(2,N) + 9]=concat(['.AC DEC ',num2str(fstep),' ',num2str(fl),' ',num2str(fh)])
# ..\MATLAB_files\adhikari.m:55
    line[dot(2,N) + 10]=concat(['.PRINT AC VM(1) VP(1) IM(VIN) IP(VIN)'])
# ..\MATLAB_files\adhikari.m:56
    line[dot(2,N) + 11]=concat(['.END'])
# ..\MATLAB_files\adhikari.m:57
    # writing netlist to file
    fid=fopen(concat([filename,'.cir']),'w')
# ..\MATLAB_files\adhikari.m:60
    for i in arange(1,length(line)).reshape(-1):
        fwrite(fid,concat([line[i],char(13),char(10)]),'char')
    
    fid=fclose(fid)
# ..\MATLAB_files\adhikari.m:64
    return filename
    
if __name__ == '__main__':
    pass
    