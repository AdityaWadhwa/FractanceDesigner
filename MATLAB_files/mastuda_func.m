function[num, den] = mastuda_func(F,alp,fl,fu,N)

wl=2*pi*fl;
%wl=fl;
wu=2*pi*fu;
%wu=fu;
K =2*N+1;%2N+1 LogramithicLLY spaced points
p = logspace(log10(wl),log10(wu),K); %points(1) = w0
d = zeros(K,1);

d(1) = p(1)^alp; %d0
d(2) = (p(2)-p(1))/((p(2)^alp)-(p(1)^alp));
for i= 3:1:K
    d(i) = (p(i)-p(1))/(-d(1)+ p(i)^alp);
    for j= 2:1:i-1
        d(i) = (p(i)-p(j))/(-d(j) + d(i));
    end 
end

a_neg1 = 1; %a-1
a_0 = d(1);
b_0 = 1; 
x=[0];
po=[0];
an = zeros(2*N);
bn = zeros(2*N);
for j=1:1:2*N
    if(j==1)
        an(j,1:2) = addpoly(d(j+1)*a_0, [1  -p(j)]);
        bn(j,1)   = d(j+1)*b_0;
    elseif(j==2)
        an(j,1:2) = addpoly(d(j+1)*an(j-1,1:2), conv([1 -p(j)], a_0));
        bn(j,1:2) = addpoly(d(j+1)*bn(j-1,1), conv([1 -p(j)], b_0));
    elseif(j==3)
        an(j,1:j) = addpoly(d(j+1)*an(j-1,1:j-1), conv([1 -p(j)], an(j-2,1:2)));
        bn(j,1:j-1) = addpoly(d(j+1)*bn(j-1,1:j-1), conv([1 -p(j)], bn(j-2,1)));
    elseif(mod(j,2)==0)
        x = conv([1 -p(j)], an(j-2,1:j-2));
        po = conv([1 -p(j)], bn(j-2,1:j-1));
        an(j,1:j-1) = addpoly(x, d(j+1)*an(j-1,1:j-1));
        bn(j,1:j) = addpoly(po, d(j+1)*bn(j-1,1:j-1));
    else
        x = conv([1 -p(j)], an(j-2,1:j-1));
        po = conv([1 -p(j)], bn(j-2,1:j-2));
        an(j,1:j) = addpoly(x, d(j+1)*an(j-1,1:j-1));
        bn(j,1:j-1) = addpoly(po, d(j+1)*bn(j-1,1:j-1));
    end
end

num = an(2*N,1:N+1)./an(2*N,1);
den = bn(2*N,1:N+1)./an(2*N,1);

num = F.*num;

return