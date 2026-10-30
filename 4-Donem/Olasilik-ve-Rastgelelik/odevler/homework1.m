p = 0.6;
n = 10;
k = 0:1:10;
okf = ( factorial(n)./(factorial(k).* factorial(n-k)) ) ...
    .* p.^(k) .*(1-p).^(n-k);
stem(k,okf,"filled",LineStyle="--",LineWidth=1)
E = sum(k.*okf);
E_x2 = sum(k.^2 .* okf) ;
E_x2_b = n^2 * p^2 - (n*p^2) + n*p;