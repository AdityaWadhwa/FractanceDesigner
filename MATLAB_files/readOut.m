function [data,text] = readOut(filename)

global oldpath
if nargin < 1 % if missing file-information ask for filename
    % this keeps the recently used path - very useful!
    if ~ischar(oldpath)
        oldpath = '';
    end
    % open file dialog
    [file, path] = uigetfile({'*.out', 'PSpice binary files'}, ...
                              'Open PSpice data file', oldpath);
    % check if a file was selcted
    if file == 0
        return
    else % save path for future use and form filename string
        oldpath = path;
        filename = [path file];
    end
end
% open the file
f.id = fopen(filename);

% node name import
data.Name = readNodes(f);
% import the time line (very important - time is not spaced linearly!!!)
[data.Freq,data.Data] = readData(f);
% continue with data import
%data.Data = readData(f);

f.id = fclose(f.id);
                    
% the following code checks what you want and formats the data accordingly
switch nargout
    case 1 % return a struct with all data
        if data.Name{1}(1) == 'F' % frequency data
%             data.Real = data.Data(1:2:end,:);
%             data.Imag = data.Data(2:2:end,:);
%             data.Cmplx = data.Real + 1i.*data.Imag;
%             data = rmfield(data,'Data');
        end
%         data.Name(1) = []; % time is extra, therefore delete its node name
        
    case 2 % return array with traces and a cell with node names
        text = data.Name';
        if data.Name{1}(1) == 'F' % frequency data (ignore phase data)
            data = [data.Freq, data.Data(1:2:end,:)];
            data = data;
        else
            data = [data.Freq, data.Data];
        end
        
    otherwise % plot data and return nothing to workspace
        if data.Name{1}(1) == 'F'
            subplot(2,1,1)
            semilogx(data.Time, data.Data(1:2:end,:));
            set(gca, 'XTickLabel', []);
            legend(data.Name(2:end));
            ylabel('real');
            subplot(2,1,2)
            semilogx(data.Time, data.Data(2:2:end,:));
            xlabel(data.Name{1});
            ylabel('imaginary');
        else
            plot(data.Freq, data.Data);
            xlabel(data.Name{1});
            legend(data.Name(2:end));
        end
        clear data
end

function N = readNodes(f)
    N = {};
    C = textscan(f.id,'%s','Delimiter','\n');
    idx = find(~cellfun('isempty',strfind(C{1,1},'FREQ')),1);
    NameLine = C{1,1}{idx,1};
    Names = textscan(NameLine,'%s');
    N = Names{1,1}(2:end)';
end

function [F,D] = readData(f)
    F = [];
    D = [];
    frewind(f.id);
    C = textscan(f.id,'%s','Delimiter','\n');
    idx = find(~cellfun('isempty',strfind(C{1,1},'FREQ')),1);
    idx = idx + 3;                                              %data starts after 2 lines
    
    i = 1;
    while 1
        Line = C{1,1}{idx,1};
        if(isempty(Line)) 
            break;
        end
        frmt = repmat('%.6f ',1,length(data.Name)+1);
        temp = textscan(Line,frmt,'Delimiter','\n');
        F(i,1) = temp{1,1};
        for j=2:1:length(data.Name)+1
            D(i,j-1) = temp{1,j};
        end
        i = i+1;
        idx = idx+1;
    end
end

end