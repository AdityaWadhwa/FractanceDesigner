# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\errorcalculator.m

    
def errorcalculator(Zmag=None,Zpha=None,F=None,alp=None,fl=None,fh=None,fstep=None,*args,**kwargs):
    varargin = args
    nargin = 7 + len(varargin)

    f=logspace(log10(fl),log10(fh),dot((log10(fh / fl)),fstep) + 1).T
# ..\MATLAB_files\errorcalculator.m:3
    
    s=dot(dot(dot(1j,2),pi),f)
# ..\MATLAB_files\errorcalculator.m:4
    
    Zmagi=dot(20,log10(abs(multiply(F,s ** alp))))
# ..\MATLAB_files\errorcalculator.m:6
    Zphai=dot((180 / pi),angle(multiply(F,s ** alp)))
# ..\MATLAB_files\errorcalculator.m:7
    magError=abs((Zmag - Zmagi))
# ..\MATLAB_files\errorcalculator.m:9
    phaError=abs((Zpha - Zphai) / Zphai)
# ..\MATLAB_files\errorcalculator.m:10
    figure
    subplot(1,2,1)
    semilogx(f,Zmagi,f,Zmag)
    subplot(1,2,2)
    semilogx(f,Zphai,f,Zpha)
    return magError,phaError
    
if __name__ == '__main__':
    pass
    