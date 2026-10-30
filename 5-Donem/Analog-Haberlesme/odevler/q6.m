
t = -1000:0.01:1000;
sinc= @(x)sin(pi.*x)./(pi.*x);%sinc function
y = sinc(t);
plot(t,y);
figure;
z = 100*sinc(t./100).*exp(1i.*400.*pi.*t) +100*sinc(t./100).*exp(-1i.*400.*pi.*t);

plot(t,z);
hold on
w = 200*sinc(t./100);
plot(t,w,"LineStyle","--","MarkerIndices",10)