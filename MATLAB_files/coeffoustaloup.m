function [Num,Den] = coeffoustaloup(F,alp,fl,fh,N)

Num  = [1];
Den  = [1];

wl = fl;        %not multiplied by 2pi on purpose...plots match by doing so
wh = fh;

wu = sqrt(wl*wh);

C0 = wu/wh;

N = floor(N/2);

for k = -N:1:N
    w_k = wl*(wh/wl)^((k+N+1/2-alp/2)/(2*N+1));
    wk  = wl*(wh/wl)^((k+N+1/2+alp/2)/(2*N+1));
    Num = conv(Num ,[wk  wk*w_k]);
    Den = conv(Den ,[w_k  w_k*wk]);
end
Num = (C0^alp).*Num;

normalizer = Den(1);
Num = Num./normalizer;
Den = Den./normalizer;
Num = F.*Num;

end