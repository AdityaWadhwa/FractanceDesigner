function[Num, Den] = TheileSecondCFE_func(F,alp,fl,fu,N)

K=2*N+1;
wl=2*pi*fl;
wu=2*pi*fu;
p = logspace(log10(wl),log10(wu),K); %points(1) = w0
w_0 = median(p);
c_0 = phik(0,w_0,alp);
c = zeros(2*N,1);

for i=1:1:2*N
    if(i==1)
        c(i)= phik(i,w_0,alp);
    else
        c(i)=phik(i,w_0,alp)-phik(i-2,w_0,alp);
    end
end

%a_neg1 = 1; %a-1
a_0 = c_0;
b_0 = 1; 
x=[0];
po=[0];
an = zeros(2*N);
bn = zeros(2*N);

for j=1:1:2*N
    if(j==1)
        an(j,1:2) = addpoly(c(j)*a_0, [1  -w_0]);
        bn(j,1)   = c(j)*b_0;
    elseif(j==2)
        an(j,1:2) = addpoly(c(j)*an(j-1,1:2), conv([1 -w_0], a_0));
        bn(j,1:2) = addpoly(c(j)*bn(j-1,1), conv([1 -w_0], b_0));
%     elseif(j==3)
%         an(j,1:j) = addpoly(c(j)*an(j-1,1:j-1), conv([1 -w_0], an(j-2,1:2)));
%         %bn(j,1:j-1) = addpoly(d(j+1)*bn(j-1,1:j-1), conv([1 -p(j)], bn(j-2,1)));
    elseif(mod(j,2)==0)
        x = conv([1 -w_0], an(j-2,1:j-2));
        po = conv([1 -w_0], bn(j-2,1:j-1));
        an(j,1:j-1) = addpoly(x, c(j)*an(j-1,1:j-1));
        bn(j,1:j) = addpoly(po, c(j)*bn(j-1,1:j-1));
    else
        x = conv([1 -w_0], an(j-2,1:j-1));
        po = conv([1 -w_0], bn(j-2,1:j-2));
        an(j,1:j) = addpoly(x, c(j)*an(j-1,1:j-1));
        bn(j,1:j-1) = addpoly(po, c(j)*bn(j-1,1:j-1));
    end
end

Num = an(2*N,1:N+1)./an(2*N,1);
Den = bn(2*N,1:N+1)./an(2*N,1);
Num = F.*Num;
return