function filename = valsa_func(F,alp,fl,fu,fstep,phierr)
if(alp>0)
    alp=-alp;
end

wl=2*pi*fl;
wu=2*pi*fu;
ab = 0.24/(1+phierr);

logtena = (abs(alp))*(log10(ab));
a = 10^logtena;
b = ab/a;

m = ceil(1-((log10(wu/wl))/(log10(ab))));

R = zeros(m,1);
C = zeros(m,1);
% we have to choose C1 and R1 so decision to keep C1 constant
C(1) = 1E-6;
R(1) = 1/(wl*C(1));

wav = sqrt(wu*wl);

Rp = R(1)*(1-a)/a;
Cp = C(1)*(b^m)/(1-b);

for i=2:1:m
    R(i) =  R(1)*(a^(i-1));
    C(i) =  C(1)*(b^(i-1));
end
Y = 0;
for i=1:1:m
    Y = Y+ (1i*wav*C(i))/((1i*wav*C(i)*R(i))+1);
end

Y = Y + (1/Rp) + 1i*wav*Cp;

Z = 1/(abs(Y));

Dreali = Z*(wav^abs(alp)); %realised value of admittance

CR = F/Dreali; %correction ratio

R = R.*CR;
Rp = Rp*CR;
C = C./CR;
Cp = Cp/CR;

filename = 'D:\DocumentsHDD\BTP\GUIapp\Pspice_files\Valsa';

line{01} = ['* Matlab created *.cir-file *'];
line{02} = ['.lib C:\Cadence\SPB_17.2\tools\pspice\library\eval.lib'];
line{03} = ['VIN        1   0   AC 1V'];
line{04} = ['Rp'  ' ' num2str(1) ' ' num2str(0) ' ' num2str(Rp)];
line{05} = ['Cp'  ' ' num2str(1) ' ' num2str(0) ' ' num2str(Cp)];
for i=1:1:m
    line{2*i+4} = ['R' num2str(i) ' ' num2str(1) ' ' num2str(i+1) ' ' num2str(R(i))];
    line{2*i+5} = ['C' num2str(i) ' ' num2str(i+1) ' ' num2str(0) ' ' num2str(C(i))];
end
line{2*m+9} = ['.AC DEC ' num2str(fstep) ' ' num2str(fl) ' ' num2str(fu)];
line{2*m+10} = ['.PRINT AC VM(1) VP(1) IM(VIN) IP(VIN)'];
line{2*m+11} = ['.END'];

% writing netlist to file
fid = fopen([filename '.cir'], 'w');
for i = 1:length(line)
    fwrite(fid, [line{i} char(13) char(10)], 'char');
end
fid = fclose(fid);


end

