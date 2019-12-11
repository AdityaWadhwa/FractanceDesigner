function filename = adhikari(F,alp,fl,fh,fstep,N)

if alp<0
    alp = abs(alp);
    F   = 1/F;
end

R = zeros(1,N+2);
C = zeros(1,N+1);

b = exp(-1.5*((1-alp)^(2/3)));
b = b - rem(b,0.1);

a = exp((alp/(1-alp))*log(b));
a = round(a,4);

t = 11.1*((b^2)/fl);

w = 2*pi*((fl*fh)^0.5);

K = (0.5 - 1/log(b))/(1+1i*w*t);
p = a*b;
for i = 1:1:N+1
    K = K + (a^i) / (1 + 1i*w*p^i*t);
end
K = K - (a^(N+1))/log(b);
K = abs(K);

r = 1/(K*F*w^alp);
c = t/r;

R0 = (0.5 - 1/log(b))*r;
C0 = c / (0.5-1/log(b));

R(1:N) = a.^[1:1:N] * r;
C(1:N) = b.^[1:1:N] * c;

R(N+1) = 0.5 * a^(N+1)*r;
C(N+1) = 2* b^(N+1)*c;

R(N+2) = -a^(N+1)*r*(1/log(a));

filename = 'D:\DocumentsHDD\BTP\GUIapp\Pspice_files\Adhikari';

line{01} = ['* Matlab created *.cir-file *'];
line{02} = ['.lib C:\Cadence\SPB_17.2\tools\pspice\library\eval.lib'];
line{03} = ['VIN        1   0   AC 1V'];
line{04} = ['R' num2str(1) ' ' num2str(1) ' ' num2str(2) ' ' num2str(R0)];
line{05} = ['C' num2str(1) ' ' num2str(1) ' ' num2str(2) ' ' num2str(C0)];
for i=1:1:N+1
    line{2*i+4} = ['R' num2str(i+1) ' ' num2str(i+1) ' ' num2str(i+2) ' ' num2str(R(i))];
    line{2*i+5} = ['C' num2str(i+1) ' ' num2str(i+1) ' ' num2str(i+2) ' ' num2str(C(i))];
end 
line{2*N+8} = ['R' num2str(N+3) ' ' num2str(N+3) ' 0 ' num2str(R(N+2))];
line{2*N+9} = ['.AC DEC ' num2str(fstep) ' ' num2str(fl) ' ' num2str(fh)];
line{2*N+10} = ['.PRINT AC VM(1) VP(1) IM(VIN) IP(VIN)'];
line{2*N+11} = ['.END'];

% writing netlist to file
fid = fopen([filename '.cir'], 'w');
for i = 1:length(line)
    fwrite(fid, [line{i} char(13) char(10)], 'char');
end
fid = fclose(fid);

end