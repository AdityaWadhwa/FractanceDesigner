function [phik_val]= phik(k,w,alp)

prod=1;
phi_0 = w^alp;
phi_1 = (w^(1-alp))/alp;
m=1;
if(k==0)
    phik_val = phi_0;
elseif(k==1)
    phik_val = phi_1;
elseif(mod(k,2)==0)
    m=k/2;
    for i=1:1:m
        prod = prod*(i+alp)/(i-alp);
    end
    phik_val = prod*phi_0;
else
    m=(k-1)/2;
    for i=1:1:m
        prod = prod*(i-alp+1)/(i+alp);
    end
    phik_val = prod*phi_1*(m+1);
end
return
