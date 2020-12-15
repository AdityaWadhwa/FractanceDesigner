function [magError,phaError] = Methodss(F,alp,fl,fu,s1,fstep,varargin)
% param 1 is which form to choose F1,F2,S2,S1

%param 2 is N /derr/phierr-
%param2 -N(i)adhikari,oustaloup,modifiedoustaloup,mastuda,theile2,carlson

% param 2(iii) is phierror- valsa

% param 2(ii) is derr-charef_func_TS
fh = fu;
l = nargin-6;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%11111%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if (strcmpi(s1,'OZASSB'))
    if(l==0)
        N = 10;
    elseif(l==1)
        N = varargin{1};
    end
    filename = adhikari(F,alp,fl,fh,fstep,N);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%2222222%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    
elseif(strcmpi(s1,'VV'))
    if(l==0)
        phierr = 0.3;
    elseif(l==1)
        phierr = varargin{1};
    end
    filename = valsa_func(F,alp,fl,fu,fstep,phierr);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%33333333%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
elseif(strcmpi(s1,'MF'))
    if(l==0)
       N = 4;
       param1 = 'FirstFoster';
    elseif(l==1)
       N = varargin{1};
       param1 = 'FirstFoster';
    elseif(l==2)
       N = varargin{1};
       param1 = varargin{2} ;        
    end
    [num , den ] = mastuda_func(F,alp,fl,fu,N);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if(strcmpi(param1,'FirstFoster'))
        filename = FirstFoster(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'SecondFoster'))
        filename = SecondFoster(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'FirstCauer'))
        filename = FirstCauer(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'SecondCauer'))
        filename = SecondCauer(num,den,fl,fu,fstep);
    end
%%%%%%%%%%%%%%%%%%%%%%%%44444444%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    
elseif(strcmpi(s1,'THEILE2'))
    if(l==0)
       N = 4;
       param1 = 'FirstFoster';
    elseif(l==1)
       N = varargin{1};
       param1 = 'FirstFoster';
    elseif(l==2)
       N = varargin{1};
       param1 = varargin{2} ;        
    end
    [num , den ] = TheileSecondCFE_func(F,alp,fl,fu,N);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if(strcmpi(param1,'FirstFoster'))
        filename = FirstFoster(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'SecondFoster'))
        filename = SecondFoster(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'FirstCauer'))
        filename = FirstCauer(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'SecondCauer'))
        filename = SecondCauer(num,den,fl,fu,fstep);
    end
%%%%%%%%%%%%%%%%%%%%%%%%%%%555555555%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
elseif(strcmpi(s1,'OUSTALOUP'))
    if(l==0)
       N = 4;
       param1 = 'FirstFoster';
    elseif(l==1)
       N = varargin{1};
       param1 = 'FirstFoster';
    elseif(l==2)
       N = varargin{1};
       param1 = varargin{2} ;        
    end
    [num , den ] = coeffoustaloup(F,alp,fl,fh,N);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if(strcmpi(param1,'FirstFoster'))
        filename = FirstFoster(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'SecondFoster'))
        filename = SecondFoster(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'FirstCauer'))
        filename = FirstCauer(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'SecondCauer'))
        filename = SecondCauer(num,den,fl,fu,fstep);
    end    
%%%%%%%%%%%%%%%%%%%%%%%%%%%66666666666%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
elseif(strcmpi(s1,'MODIFIED OUSTALOUP'))
    if(l==0)
       N = 4;
       param1 = 'FirstFoster';
    elseif(l==1)
       N = varargin{1};
       param1 = 'FirstFoster';
    elseif(l==2)
       N = varargin{1};
       param1 =varargin{2} ;        
    end
    [num , den ] = coeffmodoustaloup(F,alp,fl,fh,N);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if(strcmpi(param1,'FirstFoster'))
        filename = FirstFoster(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'SecondFoster'))
        filename = SecondFoster(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'FirstCauer'))
        filename = FirstCauer(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'SecondCauer'))
        filename = SecondCauer(num,den,fl,fu,fstep);
    end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%7777777%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
elseif(strcmpi(s1,'CHAREF'))
    if(l==0)
       derr = 1;
       param1 ='FirstFoster';
    elseif(l==1)
       derr = varargin{1};
       param1 = 'FirstFoster';
    elseif(l==2)
       derr = varargin{1};
       param1 = varargin{2} ;        
    end
    [num , den ] = charef_func_TS(F,alp,fl,fu,derr);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if(strcmpi(param1,'FirstFoster'))
        filename = FirstFoster(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'SecondFoster'))
        filename = SecondFoster(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'FirstCauer'))
        filename = FirstCauer(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'SecondCauer'))
        filename = SecondCauer(num,den,fl,fu,fstep);
    end
elseif(strcmpi(s1,'CH'))
    if(l==0)
       N = 1;
       param1 ='FirstFoster';
    elseif(l==1)
       N = varargin{1};
       param1 = 'FirstFoster';
    elseif(l==2)
       N = varargin{1};
       param1 = varargin{2} ;        
    end
    [num , den ] = coeffcarlson(F,alp,fl,fu,N);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if(strcmpi(param1,'FirstFoster'))
        filename = FirstFoster(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'SecondFoster'))
        filename = SecondFoster(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'FirstCauer'))
        filename = FirstCauer(num,den,fl,fu,fstep);
    elseif(strcmpi(param1,'SecondCauer'))
        filename = SecondCauer(num,den,fl,fu,fstep);
    end
else
    disp('method mentioned cant be implemented');
end


system(['C:\Cadence\SPB_17.2\tools\bin\psp_cmd.exe -r ' filename '.cir' ' -wONLY']);

data = readOut([filename '.out']);

Zmag = 20*log10(data.Data(:,1)./data.Data(:,3));            %magnitude response
Zpha = data.Data(:,2) - data.Data(:,4);                     %phase response

if alp<0
    Zpha = Zpha - 180;
else 
    Zpha = mod(Zpha,180);
end

[magError,phaError] = errorcalculator(Zmag,Zpha,F,alp,fl,fh,fstep);

figure;

subplot(1,2,1);
semilogx(data.Freq,magError,'linewidth',2);
grid on;
xlabel('Frequency','FontSize',12,'FontWeight','bold');
ylabel('Magnitude(dB) Non Relative Error','FontSize',12,'FontWeight','bold');

subplot(1,2,2);
semilogx(data.Freq,phaError,'linewidth',2);
grid on;
xlabel('Frequency','FontSize',12,'FontWeight','bold');
ylabel('Phase Relative Error','FontSize',12,'FontWeight','bold');

return