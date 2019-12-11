clc;
clear all;
close all;

F   = 1;
alp = -0.5;
fl  = 1E0;
fh  = 1E3;
N   = 5;
fstep = 100;
 
[Num,Den] = coeffoustaloup(F,alp,fl,fh,N);
filename = Brunes(Num,Den,fl,fh,fstep);

% filename = valsa_func(F,alp,fl,fh,fstep,0.5);

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
semilogx(data.Freq,magError);
grid on;
xlabel('Frequency');
ylabel('Magnitude(dB) Non Relative Error');

subplot(1,2,2);
semilogx(data.Freq,phaError);
grid on;
xlabel('Frequency');
ylabel('Phase Relative Error');