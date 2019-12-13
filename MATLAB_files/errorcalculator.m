function [magError,phaError] = errorcalculator(Zmag,Zpha,F,alp,fl,fh,fstep)

f = logspace(log10(fl),log10(fh),(log10(fh/fl))*fstep+1)'; %fstep is no. of points in a decade
s = 1i*2*pi*f;                                             %sometimes multiplying by 2*pi gave good results

Zmagi = 20*log10(abs(F.*s.^alp));
Zphai = (180/pi)*angle(F.*s.^alp);

magError = abs((Zmag - Zmagi));
phaError = abs((Zpha - Zphai)./Zphai);

figure;
subplot(1,2,1);
semilogx(f,Zmagi,f,Zmag,'linewidth',2);
grid on;
xlabel('Frequency','FontSize',12,'FontWeight','bold');
ylabel('Magnitude(dB)','FontSize',12,'FontWeight','bold');


subplot(1,2,2);
semilogx(f,Zphai,f,Zpha,'linewidth',2);
grid on;
xlabel('Frequency','FontSize',12,'FontWeight','bold');
ylabel('Phase (degree)','FontSize',12,'FontWeight','bold');

end