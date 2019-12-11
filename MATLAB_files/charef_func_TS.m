% charef's method, more realistic for higher frequencies
function[num,den]=charef_func_TS(F,alp,fl,fu,derr)

err= 1E-5;%max allowed error in dB
wl = fl;
%wl = 2*pi*fl;
wu =fu;
%wu = 2*pi*fu;

alpha = abs(alp);           %method was working only for postive alp, so do this and swap num and den later
    
div = 10^(err/(10*alpha))-1;
wc = abs(wl*(sqrt(div)));

num = [1];
den = [1];

powa = derr/(10*(1-alpha));
powb = derr/(10*alpha);
powz0 = derr/(20*alpha);
z0 = wc*(10^powz0);
a = 10^powa;
b = 10^powb;
p0 = a*z0;
wmax=100*wu;

Kd = wc^alpha;
nu = log10(wmax/z0);
d = log10(a*b);
x=1;

N = floor(nu/d)+1;
for i=0:1:N
    x=(a*b)^i;
    num = conv(num,[1/(z0*x) 1]);
    den = conv(den,[1/(p0*x) 1]);
end
x=Kd*F;
num = x.*num;

if alp<0
    [num,den] = deal(den,num);
end

normalizer = den(1);
num = num./normalizer;
den = den./normalizer;

end
