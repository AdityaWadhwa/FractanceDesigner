# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\readOut.m
import copy
from numpy import * 
from math import * 
    
def readOut_func(filename=None,*args,**kwargs):
    varargin = args
    nargin = 1 + len(varargin)
    f = {}
    data = {}

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
            filename=(path+file)
# ..\MATLAB_files\readOut.m:17
    
    # open the file
    f['id'] = open(filename,'r')
# ..\MATLAB_files\readOut.m:21
    # node name import
    data['Name'] = readNodes(filename)
# ..\MATLAB_files\readOut.m:24
    # import the time line (very important - time is not spaced linearly!!!)
    data['Freq'],data['Data']=readData(filename,nargout=2)
# ..\MATLAB_files\readOut.m:26
    # continue with data import
#data.Data = readData(f);
    
    f['id'].close()
# ..\MATLAB_files\readOut.m:30
    # the following code checks what you want and formats the data accordingly
    return data 
    
def readNodes(filename=None,*args,**kwargs):
    varargin = args
    nargin = 1 + len(args)

    N=list()
# ..\MATLAB_files\readOut.m:72
    C=loadtxt(filename,dtype='str',delimiter='\n')
# ..\MATLAB_files\readOut.m:73
#    idx=find(logical_not(cellfun('isempty',strfind(C[1,1],'FREQ'))),1)
# ..\MATLAB_files\readOut.m:74
    NameLine=C[char.find(C,'FREQ')!=-1]
# ..\MATLAB_files\readOut.m:75
    Names=NameLine[0].split()
# ..\MATLAB_files\readOut.m:76
    N=Names[1:]
# ..\MATLAB_files\readOut.m:77
    return N
        
    
def readData(filename=None,*args,**kwargs):
    varargin = args
    nargin = 1 + len(args)

    F=[]
# ..\MATLAB_files\readOut.m:81
    D=[]
# ..\MATLAB_files\readOut.m:82
#    frewind(f.id)
    C=loadtxt(filename,dtype='str',delimiter='\n')
# ..\MATLAB_files\readOut.m:84
    idx=char.find(C,'FREQ')!=-1
    idx=where(idx==True)[0][0]
# ..\MATLAB_files\readOut.m:85
    idx=idx + 1
# ..\MATLAB_files\readOut.m:86
    
    
#    i=1
# ..\MATLAB_files\readOut.m:88
    while 1:

        Line=C[idx]
# ..\MATLAB_files\readOut.m:90
#        if Line == []:
#            break
#        frmt=repmat('%.6f ',1,length(data.Name) + 1)
# ..\MATLAB_files\readOut.m:94
        temp=fromstring(Line,dtype='float',sep='   ')
        if(len(temp)<2):
            break
# ..\MATLAB_files\readOut.m:95
        F.append(temp[0])
# ..\MATLAB_files\readOut.m:96
        D.append(temp[1:])
# ..\MATLAB_files\readOut.m:98
#        i =i + 1
# ..\MATLAB_files\readOut.m:100
        idx+=1
# ..\MATLAB_files\readOut.m:101

    F = array(F)
    D = array(D)
    return F,D
    
if __name__ == '__main__':
    pass
    
    