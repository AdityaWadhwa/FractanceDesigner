# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\readOut.m
import copy
import numpy
    
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
    N=['VR(1)','VI(1)','IR(VIN)','II(VIN)']
    return N
        
    
def readData(filename=None,*args,**kwargs):

    C = numpy.loadtxt(filename,dtype='float')

    F = C[:,0]
    D = C[:,1:]
    return F,D
    
if __name__ == '__main__':
    pass
    
    