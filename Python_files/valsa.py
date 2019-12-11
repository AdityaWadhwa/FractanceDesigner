# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\valsa_func.m

    
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
    R=zeros(m,1)
# ..\MATLAB_files\valsa_func.m:16
    C=zeros(m,1)
# ..\MATLAB_files\valsa_func.m:17
    # we have to choose C1 and R1 so decision to keep C1 constant
    C[1]=1e-06
# ..\MATLAB_files\valsa_func.m:19
    R[1]=1 / (dot(wl,C(1)))
# ..\MATLAB_files\valsa_func.m:20
    wav=sqrt(dot(wu,wl))
# ..\MATLAB_files\valsa_func.m:22
    Rp=dot(R(1),(1 - a)) / a
# ..\MATLAB_files\valsa_func.m:24
    Cp=dot(C(1),(b ** m)) / (1 - b)
# ..\MATLAB_files\valsa_func.m:25
    for i in arange(2,m,1).reshape(-1):
        R[i]=dot(R(1),(a ** (i - 1)))
# ..\MATLAB_files\valsa_func.m:28
        C[i]=dot(C(1),(b ** (i - 1)))
# ..\MATLAB_files\valsa_func.m:29
    
    Y=0
# ..\MATLAB_files\valsa_func.m:31
    for i in arange(1,m,1).reshape(-1):
        Y=Y + (dot(dot(1j,wav),C(i))) / ((dot(dot(dot(1j,wav),C(i)),R(i))) + 1)
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
# ..\MATLAB_files\valsa_func.m:47
    filename='D:\\DocumentsHDD\\BTP\\GUIapp\\Pspice_files\\Valsa'
# ..\MATLAB_files\valsa_func.m:49
    line[1]=concat(['* Matlab created *.cir-file *'])
# ..\MATLAB_files\valsa_func.m:51
    line[2]=concat(['.lib C:\\Cadence\\SPB_17.2\\tools\\pspice\\library\\eval.lib'])
# ..\MATLAB_files\valsa_func.m:52
    line[3]=concat(['VIN        1   0   AC 1V'])
# ..\MATLAB_files\valsa_func.m:53
    line[4]=concat(['Rp',' ',num2str(1),' ',num2str(0),' ',num2str(Rp)])
# ..\MATLAB_files\valsa_func.m:54
    line[5]=concat(['Cp',' ',num2str(1),' ',num2str(0),' ',num2str(Cp)])
# ..\MATLAB_files\valsa_func.m:55
    for i in arange(1,m,1).reshape(-1):
        line[dot(2,i) + 4]=concat(['R',num2str(i),' ',num2str(1),' ',num2str(i + 1),' ',num2str(R(i))])
# ..\MATLAB_files\valsa_func.m:57
        line[dot(2,i) + 5]=concat(['C',num2str(i),' ',num2str(i + 1),' ',num2str(0),' ',num2str(C(i))])
# ..\MATLAB_files\valsa_func.m:58
    
    line[dot(2,m) + 9]=concat(['.AC DEC ',num2str(fstep),' ',num2str(fl),' ',num2str(fu)])
# ..\MATLAB_files\valsa_func.m:60
    line[dot(2,m) + 10]=concat(['.PRINT AC VM(1) VP(1) IM(VIN) IP(VIN)'])
# ..\MATLAB_files\valsa_func.m:61
    line[dot(2,m) + 11]=concat(['.END'])
# ..\MATLAB_files\valsa_func.m:62
    # writing netlist to file
    fid=fopen(concat([filename,'.cir']),'w')
# ..\MATLAB_files\valsa_func.m:65
    for i in arange(1,length(line)).reshape(-1):
        fwrite(fid,concat([line[i],char(13),char(10)]),'char')
    
    fid=fclose(fid)
# ..\MATLAB_files\valsa_func.m:69
    return filename
    
if __name__ == '__main__':
    pass
    