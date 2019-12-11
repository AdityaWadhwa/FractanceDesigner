# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\readOut.m
import copy
    
def readOut(filename=None,*args,**kwargs):
    varargin = args
    nargin = 1 + len(varargin)

    global oldpath
    if nargin < 1:
        # this keeps the recently used path - very useful!
        if logical_not(ischar(oldpath)):
            oldpath=''
# ..\MATLAB_files\readOut.m:7
        # open file dialog
        file,path=uigetfile(cellarray(['*.out','PSpice binary files']),'Open PSpice data file',oldpath,nargout=2)
# ..\MATLAB_files\readOut.m:10
        if file == 0:
            return data,text
        else:
            oldpath=copy.copy(path)
# ..\MATLAB_files\readOut.m:16
            filename=concat([path,file])
# ..\MATLAB_files\readOut.m:17
    
    # open the file
    f.id = copy.copy(fopen(filename))
# ..\MATLAB_files\readOut.m:21
    # node name import
    data.Name = copy.copy(readNodes(f))
# ..\MATLAB_files\readOut.m:24
    # import the time line (very important - time is not spaced linearly!!!)
    data.Freq,data.Data=readData(f,nargout=2)
# ..\MATLAB_files\readOut.m:26
    # continue with data import
#data.Data = readData(f);
    
    f.id = copy.copy(fclose(f.id))
# ..\MATLAB_files\readOut.m:30
    # the following code checks what you want and formats the data accordingly
    if 1 == nargout:
        if data.Name[1](1) == 'F':
            #             data.Real = data.Data(1:2:end,:);
#             data.Imag = data.Data(2:2:end,:);
#             data.Cmplx = data.Real + 1i.*data.Imag;
#             data = rmfield(data,'Data');
            pass
        #         data.Name(1) = []; # time is extra, therefore delete its node name
    else:
        if 2 == nargout:
            text=data.Name.T
# ..\MATLAB_files\readOut.m:44
            if data.Name[1](1) == 'F':
                data=concat([data.Freq,data.Data(arange(1,end(),2),arange())])
# ..\MATLAB_files\readOut.m:46
                data=copy.copy(data)
# ..\MATLAB_files\readOut.m:47
            else:
                data=concat([data.Freq,data.Data])
# ..\MATLAB_files\readOut.m:49
        else:
            if data.Name[1](1) == 'F':
                subplot(2,1,1)
                semilogx(data.Time,data.Data(arange(1,end(),2),arange()))
                set(gca,'XTickLabel',[])
                legend(data.Name(arange(2,end())))
                ylabel('real')
                subplot(2,1,2)
                semilogx(data.Time,data.Data(arange(2,end(),2),arange()))
                xlabel(data.Name[1])
                ylabel('imaginary')
            else:
                plot(data.Freq,data.Data)
                xlabel(data.Name[1])
                legend(data.Name(arange(2,end())))
            clear('data')
    
    
@function
def readNodes(f=None,*args,**kwargs):
    varargin = args
    nargin = 1 + len(args)

    N=cellarray([])
# ..\MATLAB_files\readOut.m:72
    C=textscan(f.id,'%s','Delimiter','\\n')
# ..\MATLAB_files\readOut.m:73
    idx=find(logical_not(cellfun('isempty',strfind(C[1,1],'FREQ'))),1)
# ..\MATLAB_files\readOut.m:74
    NameLine=C[1,1][idx,1]
# ..\MATLAB_files\readOut.m:75
    Names=textscan(NameLine,'%s')
# ..\MATLAB_files\readOut.m:76
    N=Names[1,1](arange(2,end())).T
# ..\MATLAB_files\readOut.m:77
    return N
    
if __name__ == '__main__':
    pass
    
    
@function
def readData(f=None,*args,**kwargs):
    varargin = args
    nargin = 1 + len(args)

    F=[]
# ..\MATLAB_files\readOut.m:81
    D=[]
# ..\MATLAB_files\readOut.m:82
    frewind(f.id)
    C=textscan(f.id,'%s','Delimiter','\\n')
# ..\MATLAB_files\readOut.m:84
    idx=find(logical_not(cellfun('isempty',strfind(C[1,1],'FREQ'))),1)
# ..\MATLAB_files\readOut.m:85
    idx=idx + 3
# ..\MATLAB_files\readOut.m:86
    
    
    i=1
# ..\MATLAB_files\readOut.m:88
    while 1:

        Line=C[1,1][idx,1]
# ..\MATLAB_files\readOut.m:90
        if (isempty(Line)):
            break
        frmt=repmat('%.6f ',1,length(data.Name) + 1)
# ..\MATLAB_files\readOut.m:94
        temp=textscan(Line,frmt,'Delimiter','\\n')
# ..\MATLAB_files\readOut.m:95
        F[i,1]=temp[1,1]
# ..\MATLAB_files\readOut.m:96
        for j in arange(2,length(data.Name) + 1,1).reshape(-1):
            D[i,j - 1]=temp[1,j]
# ..\MATLAB_files\readOut.m:98
        i=i + 1
# ..\MATLAB_files\readOut.m:100
        idx=idx + 1
# ..\MATLAB_files\readOut.m:101

    
    return F,D
    
if __name__ == '__main__':
    pass
    
    return F,D
    
if __name__ == '__main__':
    pass
    