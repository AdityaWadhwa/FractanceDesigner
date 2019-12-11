# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\AutomationMain.m

    clc
    clear('all')
    close_('all')
    F=1
# ..\MATLAB_files\AutomationMain.m:5
    alp=- 0.5
# ..\MATLAB_files\AutomationMain.m:6
    fl=1.0
# ..\MATLAB_files\AutomationMain.m:7
    fh=1000.0
# ..\MATLAB_files\AutomationMain.m:8
    N=5
# ..\MATLAB_files\AutomationMain.m:9
    fstep=100
# ..\MATLAB_files\AutomationMain.m:10
    Num,Den=coeffoustaloup(F,alp,fl,fh,N,nargout=2)
# ..\MATLAB_files\AutomationMain.m:12
    filename=Brunes(Num,Den,fl,fh,fstep)
# ..\MATLAB_files\AutomationMain.m:13
    # filename = valsa_func(F,alp,fl,fh,fstep,0.5);
    
    system(concat(['C:\\Cadence\\SPB_17.2\\tools\\bin\\psp_cmd.exe -r ',filename,'.cir',' -wONLY']))
    data=readOut(concat([filename,'.out']))
# ..\MATLAB_files\AutomationMain.m:19
    Zmag=dot(20,log10(data.Data(arange(),1) / data.Data(arange(),3)))
# ..\MATLAB_files\AutomationMain.m:21
    
    Zpha=data.Data(arange(),2) - data.Data(arange(),4)
# ..\MATLAB_files\AutomationMain.m:22
    
    if alp < 0:
        Zpha=Zpha - 180
# ..\MATLAB_files\AutomationMain.m:25
    else:
        Zpha=mod(Zpha,180)
# ..\MATLAB_files\AutomationMain.m:27
    
    magError,phaError=errorcalculator(Zmag,Zpha,F,alp,fl,fh,fstep,nargout=2)
# ..\MATLAB_files\AutomationMain.m:30
    figure
    subplot(1,2,1)
    semilogx(data.Freq,magError)
    grid('on')
    xlabel('Frequency')
    ylabel('Magnitude(dB) Non Relative Error')
    subplot(1,2,2)
    semilogx(data.Freq,phaError)
    grid('on')
    xlabel('Frequency')
    ylabel('Phase Relative Error')