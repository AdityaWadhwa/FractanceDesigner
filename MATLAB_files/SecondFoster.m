function filename = SecondFoster(Num,Den,fl,fh,fstep)

b = Num;
a = Den;

filename = 'D:\DocumentsHDD\BTP\GUIapp\Pspice_files\SecondFoster';

if find(a>0, 1, 'first') > find(b>0, 1, 'first')    %checking if degree is different, then a capacitor come out
    Clast = a(1)/b(1);
    a = a - [Clast*b 0];
    a = a(2:end);
else
    Clast = 0;
end

Rlast = b(find(b>0, 1, 'last'))/a(find(a>0, 1, 'last'));
a = a - (1/Rlast)*b;                                %removing constant term

[r,p,k] = residue(a,b);                             %use Y(s) for second foster form

for i = 1:1:length(p)
    Num = a;
    Den = conv(b,[1 0]);                            %divide by s
    Den = deconv(Den,[1 -p(i)]);                    %multiply by (s-p)
    r(i) = polyval(Num,p(i)) / polyval(Den,p(i));
end
   
R = 1./r;
C = -r./p;

if Rlast ~= 0
    R = vertcat(R,Rlast);
    %C = vertcat(C,1/0);
end

if Clast ~= 0
    R = vertcat(R,0);
    C = vertcat(C,Clast);
end

line{01} = ['* Matlab created *.cir-file *'];
line{02} = ['.lib C:\Cadence\SPB_17.2\tools\pspice\library\eval.lib'];
line{03} = ['VIN        1   0   AC 1V'];
for i=1:1:length(C)
    line{2*i+2} = ['R' num2str(i) ' 1 ' num2str(i+1) ' ' num2str(R(i))];
    line{2*i+3} = ['C' num2str(i) ' '   num2str(i+1) ' 0 ' num2str(C(i))];
end 
line{2*length(C)+5} = ['R' num2str(length(R)) ' 1 ' num2str(i+1) ' ' num2str(R(length(R)))];
line{2*length(C)+6} = ['.AC DEC ' num2str(fstep) ' ' num2str(fl) ' ' num2str(fh)];
line{2*length(C)+7} = ['.PRINT AC VM(1) VP(1) IM(VIN) IP(VIN)'];
line{2*length(C)+8} = ['.END'];

% writing netlist to file
fid = fopen([filename '.cir'], 'w');
for i = 1:length(line)
    fwrite(fid, [line{i} char(13) char(10)], 'char');
end
fid = fclose(fid);

end