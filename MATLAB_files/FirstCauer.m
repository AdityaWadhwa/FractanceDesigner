function filename = FirstCauer(Numerator,Denominator,fl,fh,fstep)

q = Denominator;
p = Numerator;

filename = 'D:\DocumentsHDD\BTP\GUIapp\Pspice_files\FirstCauer';

Num=p;
Den=q;

[M,N] = size(q);

R = zeros(1,2*N);
C = zeros(1,2*N+1);

for i = 1:1:2*N+1
    
    idxN = find(abs(Num)>1E-5, 1, 'first');
    idxD = find(abs(Den)>1E-5, 1, 'first');
    
    Num(1:idxN-1) = 0;
    Den(1:idxD-1) = 0;
    
    if isempty(idxD)
        break;
    end
    
    if idxN == idxD
        qu = Num(idxN)/Den(idxD);
        re = Num-(Den*qu);
        R(i) = qu;
    else
        if i == 1
            qu = 0;
        else
            qu = Num(idxN)/Den(idxD);
        end
        re = Num-circshift((Den*qu),[0,-1]);
        C(i) = qu;
    end
    Num = Den;
    Den = re;
end

if C(i) ~= 0
    R(i+1) = 1/re(N);
end

line{01} = ['* Matlab created *.cir-file *'];
line{02} = ['.lib C:\Cadence\SPB_17.2\tools\pspice\library\eval.lib'];
line{03} = ['VIN        1   0   AC 1V'];
for i=1:1:find(C~=0, 1, 'last')/2
    line{2*i+2} = ['R' num2str(i) ' ' num2str(i) ' ' num2str(i+1) ' ' num2str(R(2*i-1))];
    line{2*i+3} = ['C' num2str(i+1) ' ' num2str(i+1) ' 0 ' num2str(C(2*i))];
end 
line{length(C)+4} = ['R' num2str(i+2) ' ' num2str(i+1) ' 0 ' num2str(R(length(R)-1))];
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