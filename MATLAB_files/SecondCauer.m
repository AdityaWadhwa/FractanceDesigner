function filename = SecondCauer(Numerator,Denominator,fl,fh,fstep)

q = Numerator;
p = Denominator;

filename = 'D:\DocumentsHDD\BTP\GUIapp\Pspice_files\SecondCauer';

Num=p;
Den=q;

[M,N] = size(q);

R = zeros(1,2*N);
C = zeros(1,2*N+1);

for i = 1:1:2*N+1
    
    idxN = find(abs(Num)>1E-5, 1, 'last');
    idxD = find(abs(Den)>1E-5, 1, 'last');
    
    Num(idxN+1:end)=0;
    Den(idxD+1:end)=0;
    
    if isempty(idxD)
        break;
    end
    
    if idxN == idxD    
        qu = Num(idxN)/Den(idxD);
        re = Num-(Den*qu);
        R(i) = 1/qu;
    else
        if i == 1
            qu = 0;
        else
            qu = Num(idxN)/Den(idxD);
        end
        re = Num-circshift((Den*qu),[0,1]);
        C(i) = 1/qu;
    end
    
    Num = Den;
    Den = re;
end

if C(i) ~= 0
    R(i+1) = 1/Num(1);
end

line{01} = ['* Matlab created *.cir-file *'];
line{02} = ['.lib C:\Cadence\SPB_17.2\tools\pspice\library\eval.lib'];
line{03} = ['VIN        1   0   AC 1V'];
k = find(C~=0, 1, 'last')/2;
for i=1:1:k
    if R(2*i-1) ~= 0
        line{2*i+2} = ['R' num2str(i) ' ' num2str(i) ' 0 ' num2str(R(2*i-1))];
    end
    if C(2*i) ~= 0
        line{2*i+3} = ['C' num2str(i+1) ' ' num2str(i) ' ' num2str(i+1) ' ' num2str(C(2*i))];
    end
end
line{length(C)+4} = ['R' num2str(i+2) ' ' num2str(i+1) ' 0 ' num2str(R(2*k+1))];
line{length(C)+5} = ['.AC DEC ' num2str(fstep) ' ' num2str(fl) ' ' num2str(fh)];
line{length(C)+6} = ['.PRINT AC VM(1) VP(1) IM(VIN) IP(VIN)'];
line{length(C)+7} = ['.END'];

% writing netlist to file
fid = fopen([filename '.cir'], 'w');
for i = 1:length(line)
    fwrite(fid, [line{i} char(13) char(10)], 'char');
end
fid = fclose(fid);

end