function [Num,Den] = coeffmodoustaloup(F,alp,fl,fh,N)

Num   = [1];
Den   = [1];
alpha = abs(alp);

wb = fl;     %not multiplied by 2pi on purpose...plots match by doing so
wh = fh;

d=9;
b=10;
N = floor(N/2);

K = ((d*wb/b)^alpha);
for k = -N:1:N
    w_k = (d*wb/b)^((alpha-2*k)/(2*N+1));
    wk  = (b*wh/d)^((alpha+2*k)/(2*N+1));
    Num = conv(Num ,[wk  wk*w_k]);
    Den = conv(Den ,[w_k  wk*w_k]);
end

Num = conv(Num,[d  b*wh 0]);
Den = conv(Den,[d*(1-alpha) b*wh d*alpha]);
Num = K.*Num;
     
if alp<0
    [Den,Num] = deal(Num,Den);      %function is made for abs(alp) and if alp<0 then Num and Den are swapped
end

normalizer = Den(1);
Num = Num./normalizer;
Den = Den./normalizer;
Num = F.*Num;

end