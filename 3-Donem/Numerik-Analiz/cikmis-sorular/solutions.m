%cholesky
L = [1,0,0;1,-1,0;-1,-1,1];
Lt = L.';
A= L*Lt;
b = [1;2;-1];
syms y1 
syms y2
syms y3

y = [y1;y2;y3];
pn_1 = -1.6882;
pn = pn_1 + ((pn_1^3 + cos(pn_1)) /-3*(pn_1)^2+sin(pn_1)) 

