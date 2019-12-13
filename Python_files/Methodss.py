# Generated with SMOP  0.41-beta
# from libsmop import *
# ..\MATLAB_files\Methodss.m
import os
import numpy
import matplotlib.pyplot as plt

from numpy import *
from math import *

from adhikari import adhikari_func
from carlson import coeffcarlson
from charef import charef_func_TS
from error import errorcalculator
from FirstCauer import FirstCauer_func
from SecondCauer import SecondCauer_func
from FirstFoster import FirstFoster_func
from SecondFoster import SecondFoster_func
from mastuda import mastuda_func
from modoustaloup import coeffmodoustaloup
from oustaloup import coeffoustaloup
from TheileSecondCFE import TheileSecondCFE_func
from valsa import valsa_func
from readOut import readOut_func
    
def calculator(F=None,alp=None,fl=None,fu=None,s1=None,fstep=None,*args,**kwargs):
    varargin = args
    nargin = 6 + len(varargin)

    # param 1 is which form to choose F1,F2,S2,S1
    
    #param 2 is N /derr/phierr-
#param2 -N(i)adhikari,oustaloup,modifiedoustaloup,mastuda,theile2,carlson
    
    # param 2(iii) is phierror- valsa
    
    # param 2(ii) is derr-charef_func_TS
    fh=fu
# ..\MATLAB_files\Methodss.m:10
    l=nargin - 6
# ..\MATLAB_files\Methodss.m:11
    ############################11111##################################
    if (s1=='adhikari'):
        if (l == 0):
            N=10
# ..\MATLAB_files\Methodss.m:16
        else:
            if (l == 1):
                N=varargin[0]
# ..\MATLAB_files\Methodss.m:18
        filename=adhikari_func(F,alp,fl,fh,fstep,N)
# ..\MATLAB_files\Methodss.m:20
        ##############################2222222###################################
    else:
        if (s1=='valsa'):
            if (l == 0):
                phierr=0.3
# ..\MATLAB_files\Methodss.m:24
            else:
                if (l == 1):
                    phierr=varargin[0]
# ..\MATLAB_files\Methodss.m:26
            filename=valsa_func(F,alp,fl,fu,fstep,phierr)
# ..\MATLAB_files\Methodss.m:28
            #############################33333333#####################################
        else:
            if (s1=='mastuda'):
                if (l == 0):
                    N=4
# ..\MATLAB_files\Methodss.m:32
                    param1='FirstFoster'
# ..\MATLAB_files\Methodss.m:33
                else:
                    if (l == 1):
                        N=varargin[0]
# ..\MATLAB_files\Methodss.m:35
                        param1='FirstFoster'
# ..\MATLAB_files\Methodss.m:36
                    else:
                        if (l == 2):
                            N=varargin[0]
# ..\MATLAB_files\Methodss.m:38
                            param1=varargin[1]
# ..\MATLAB_files\Methodss.m:39
                num,den=mastuda_func(F,alp,fl,fu,N)
# ..\MATLAB_files\Methodss.m:41
                if (param1=='FirstFoster'):
                    filename=FirstFoster_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:44
                else:
                    if (param1=='SecondFoster'):
                        filename=SecondFoster_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:46
                    else:
                        if (param1=='FirstCauer'):
                            filename=FirstCauer_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:48
                        else:
                            if (param1=='SecondCauer'):
                                filename=SecondCauer_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:50
                ########################44444444######################################
            else:
                if (s1=='TheileSecond'):
                    if (l == 0):
                        N=4
# ..\MATLAB_files\Methodss.m:55
                        param1='FirstFoster'
# ..\MATLAB_files\Methodss.m:56
                    else:
                        if (l == 1):
                            N=varargin[0]
# ..\MATLAB_files\Methodss.m:58
                            param1='FirstFoster'
# ..\MATLAB_files\Methodss.m:59
                        else:
                            if (l == 2):
                                N=varargin[0]
# ..\MATLAB_files\Methodss.m:61
                                param1=varargin[1]
# ..\MATLAB_files\Methodss.m:62
                    num,den=TheileSecondCFE_func(F,alp,fl,fu,N)
# ..\MATLAB_files\Methodss.m:64
                    if (param1=='FirstFoster'):
                        filename=FirstFoster_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:67
                    else:
                        if (param1=='SecondFoster'):
                            filename=SecondFoster_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:69
                        else:
                            if (param1=='FirstCauer'):
                                filename=FirstCauer_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:71
                            else:
                                if (param1=='SecondCauer'):
                                    filename=SecondCauer_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:73
                    ###########################555555555###################################
                else:
                    if (s1=='Oustaloup'):
                        if (l == 0):
                            N=4
# ..\MATLAB_files\Methodss.m:78
                            param1='FirstFoster'
# ..\MATLAB_files\Methodss.m:79
                        else:
                            if (l == 1):
                                N=varargin[0]
# ..\MATLAB_files\Methodss.m:81
                                param1='FirstFoster'
# ..\MATLAB_files\Methodss.m:82
                            else:
                                if (l == 2):
                                    N=varargin[0]
# ..\MATLAB_files\Methodss.m:84
                                    param1=varargin[1]
# ..\MATLAB_files\Methodss.m:85
                        num,den=coeffoustaloup(F,alp,fl,fh,N,nargout=2)
# ..\MATLAB_files\Methodss.m:87
                        if (param1=='FirstFoster'):
                            filename=FirstFoster_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:90
                        else:
                            if (param1=='SecondFoster'):
                                filename=SecondFoster_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:92
                            else:
                                if (param1=='FirstCauer'):
                                    filename=FirstCauer_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:94
                                else:
                                    if (param1=='SecondCauer'):
                                        filename=SecondCauer_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:96
                        ###########################66666666666###################################
                    else:
                        if (s1=='ModiOustaloup'):
                            if (l == 0):
                                N=4
# ..\MATLAB_files\Methodss.m:101
                                param1='FirstFoster'
# ..\MATLAB_files\Methodss.m:102
                            else:
                                if (l == 1):
                                    N=varargin[0]
# ..\MATLAB_files\Methodss.m:104
                                    param1='FirstFoster'
# ..\MATLAB_files\Methodss.m:105
                                else:
                                    if (l == 2):
                                        N=varargin[0]
# ..\MATLAB_files\Methodss.m:107
                                        param1=varargin[1]
# ..\MATLAB_files\Methodss.m:108
                            num,den=coeffmodoustaloup(F,alp,fl,fh,N,nargout=2)
# ..\MATLAB_files\Methodss.m:110
                            if (param1=='FirstFoster'):
                                filename=FirstFoster_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:113
                            else:
                                if (param1=='SecondFoster'):
                                    filename=SecondFoster_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:115
                                else:
                                    if (param1=='FirstCauer'):
                                        filename=FirstCauer_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:117
                                    else:
                                        if (param1=='SecondCauer'):
                                            filename=SecondCauer_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:119
                            ##############################7777777################################
                        else:
                            if (s1=='Charef'):
                                if (l == 0):
                                    derr=1
# ..\MATLAB_files\Methodss.m:124
                                    param1='FirstFoster'
# ..\MATLAB_files\Methodss.m:125
                                else:
                                    if (l == 1):
                                        derr=varargin[0]
# ..\MATLAB_files\Methodss.m:127
                                        param1='FirstFoster'
# ..\MATLAB_files\Methodss.m:128
                                    else:
                                        if (l == 2):
                                            derr=varargin[0]
# ..\MATLAB_files\Methodss.m:130
                                            param1=varargin[1]
# ..\MATLAB_files\Methodss.m:131
                                num,den=charef_func_TS(F,alp,fl,fu,derr,nargout=2)
# ..\MATLAB_files\Methodss.m:133
                                if (param1=='FirstFoster'):
                                    filename=FirstFoster_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:136
                                else:
                                    if (param1=='SecondFoster'):
                                        filename=SecondFoster_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:138
                                    else:
                                        if (param1=='FirstCauer'):
                                            filename=FirstCauer_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:140
                                        else:
                                            if (param1=='SecondCauer'):
                                                filename=SecondCauer_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:142
                            else:
                                if (s1=='Carlson'):
                                    if (l == 0):
                                        N=1
# ..\MATLAB_files\Methodss.m:146
                                        param1='FirstFoster'
# ..\MATLAB_files\Methodss.m:147
                                    else:
                                        if (l == 1):
                                            N=varargin[0]
# ..\MATLAB_files\Methodss.m:149
                                            param1='FirstFoster'
# ..\MATLAB_files\Methodss.m:150
                                        else:
                                            if (l == 2):
                                                N=varargin[0]
# ..\MATLAB_files\Methodss.m:152
                                                param1=varargin[1]
# ..\MATLAB_files\Methodss.m:153
                                    num,den=coeffcarlson(F,alp,fl,fu,N,nargout=2)
# ..\MATLAB_files\Methodss.m:155
                                    if (param1=='FirstFoster'):
                                        filename=FirstFoster_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:158
                                    else:
                                        if (param1=='SecondFoster'):
                                            filename=SecondFoster_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:160
                                        else:
                                            if (param1=='FirstCauer'):
                                                filename=FirstCauer_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:162
                                            else:
                                                if (param1=='SecondCauer'):
                                                    filename=SecondCauer_func(num,den,fl,fu,fstep)
# ..\MATLAB_files\Methodss.m:164
                                else:
                                    disp('method mentioned cant be implemented')
    
    os.system('C:\\Cadence\\SPB_17.2\\tools\\bin\\psp_cmd.exe -r '+filename+'.cir'+' -wONLY')
    data=readOut_func(filename+'.out')
# ..\MATLAB_files\Methodss.m:173
    Zmag=multiply(20,numpy.log10(divide(data['Data'][:,0],data['Data'][:,2])))
# ..\MATLAB_files\Methodss.m:175
    
    Zpha=data['Data'][:,1] - data['Data'][:,3]
# ..\MATLAB_files\Methodss.m:176
    
    if alp < 0:
        Zpha=Zpha - 180
# ..\MATLAB_files\Methodss.m:179
    else:
        Zpha=Zpha%180
# ..\MATLAB_files\Methodss.m:181
    
    Zmagi,Zphai,Zmag,Zpha,magError,phaError = errorcalculator(Zmag,Zpha,F,alp,fl,fh,fstep)
# ..\MATLAB_files\Methodss.m:184
#    figure
#    plt.subplot(1,2,1)
#    plt.semilogx(data['Freq'],magError)
#    plt.grid('on')
#    plt.xlabel('Frequency')
#    plt.ylabel('Magnitude(dB) Non Relative Error')
#    
#    plt.subplot(1,2,2)
#    plt.semilogx(data['Freq'],phaError)
#    plt.grid('on')
#    plt.xlabel('Frequency')
#    plt.ylabel('Phase Relative Error')
#
#    plt.show()

    return Zmagi,Zphai,Zmag,Zpha,magError,phaError

if __name__ == '__main__':
    pass
#    Methodss(1,-0.5,1E-3,1E3,'adhikari',100)