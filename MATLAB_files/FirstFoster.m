function filename = FirstFoster(Num,Den,fl,fh,fstep)

b = Num;
a = Den;

filename = 'D:\DocumentsHDD\BTP\GUIapp\Pspice_files\FirstFoster';

[r,p,k] = residue(b,a);         %inbuilt function for partial fractions

C = 1./r;
R = -r./p;

if ~isempty(k)
    R = vertcat(R,k);
end

line{01} = ['* Matlab created *.cir-file *'];
line{02} = ['.lib C:\Cadence\SPB_17.2\tools\pspice\library\eval.lib'];
line{03} = ['VIN        1   0   AC 1V'];
for i=1:1:length(C)
    if R(i) ~= -Inf
        line{2*i+2} = ['R' num2str(i) ' ' num2str(i) ' ' num2str(i+1) ' ' num2str(R(i))];
    end
    line{2*i+3} = ['C' num2str(i) ' ' num2str(i) ' ' num2str(i+1) ' ' num2str(C(i))];
end 
line{2*length(C)+5} = ['R' num2str(i+1) ' ' num2str(i+1) ' 0 ' num2str(R(length(R)))];
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