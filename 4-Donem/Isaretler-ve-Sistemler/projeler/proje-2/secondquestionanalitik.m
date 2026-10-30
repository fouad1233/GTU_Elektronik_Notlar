figure%yeni figür
n = -100:1:100;%ayrık zaman örneklem vektörünün tanımlanması
xn = xn_func(n);
stem(n,xn);
title('x[n] işareti')
xlabel('n ')
ylabel('x[n]')

figure
w = -8:0.1:8;%frekans örneklem vektörü
Xejw = @(w)(1./(1-(0.8.*(exp(-1i.*w)))));%xn şaretinin fourier transformus
%%
subplot(4,2,1)
plot(w, abs(Xejw(w)))%genliği bulmak için abs fonksiyonu kullanıldı
title('x[n] işaretinin fourier transformu genliği analitik')
xlabel('Angular frequency w (rad/s) ')
ylabel('Amplitude')

subplot(4,2,2)
plot(w, angle(Xejw(w)))%açı için de angle fonksiyonu
%bu fonksiyon açıyı radyan cinsinden dndürmektedir
title('x[n] işaretinin fourier transformu fazı analitik')
xlabel('Angular frequency w (rad/s) ')
ylabel('Phase (radyan)')
%%
Yejwb = exp(-1i.*5.*w).*Xejw(w);
subplot(4,2,3)
plot(w, abs(Yejwb))
title('y = x[n-5] işaretinin fourier transformu genliği analitik')
xlabel('Angular frequency w (rad/s) ')
ylabel('Amplitude')

subplot(4,2,4)
plot(w, angle(Yejwb))
title('y = x[n-5] işaretinin fourier transformu fazı analitik')
xlabel('Angular frequency w (rad/s) ')
ylabel('Phase (radyan)')
%%
Yejwc = (-0.8.*1i.*exp(-1i.*w))./((1-0.8.*exp(-1i.*w)).^2);
subplot(4,2,5)
plot(w, abs(Yejwc))
title('y = nx[n] işaretinin fourier transformu genliği analitik')
xlabel('Angular frequency w (rad/s) ')
ylabel('Amplitude')

subplot(4,2,6)
plot(w, angle(Yejwc))
title('y = nx[n] işaretinin fourier transformu fazı analitik')
xlabel('Angular frequency w (rad/s) ')
ylabel('Phase (radyan)')
%%
Yejwd = Xejw(-w);
subplot(4,2,7)
plot(w, abs(Yejwd))
title('y = x[-n] işaretinin fourier transformu genliği analitik')
xlabel('Angular frequency w (rad/s) ')
ylabel('Amplitude')

subplot(4,2,8)
plot(w, angle(Yejwd))
title('y = x[-n] işaretinin fourier transformu fazı analitik')
xlabel('Angular frequency w (rad/s) ')
ylabel('Phase (radyan)')
%%
figure
Yejwe = 0.5.*(Xejw(w-0.1.*pi)+ Xejw(w+0.1.*pi));
subplot(3,2,1)
plot(w, abs(Yejwe))
title('y = x[n]cos(0.1*pi*n*j) işaretinin fourier transformu genliği analitik')
xlabel('Angular frequency w (rad/s) ')
ylabel('Amplitude')

subplot(3,2,2)
plot(w, angle(Yejwe))
title('y = x[n]cos(0.1*pi*n*j) işaretinin fourier transformu fazı analitik')
xlabel('Angular frequency w (rad/s) ')
ylabel('Phase (radyan)')
%%
Hejw = exp(-5.*1i.*w)-0.8 .*exp(-6.*1i.*w) ;
subplot(3,2,3)
plot(w, abs(Hejw))
title('H(ejw) işaretinin fourier transformu genliği analitik')
xlabel('Angular frequency w (rad/s) ')
ylabel('Amplitude')

subplot(3,2,4)
plot(w, angle(Hejw))
title('H(ejw)  işaretinin fourier transformu fazı analitik')
xlabel('Angular frequency w (rad/s) ')
ylabel('Phase (radyan)')
%%

hn = dirac(n-5) - 0.8.*dirac(n-6);
idx = y == Inf; % sonsuzu bulmak ifadesi
y(idx) = 1;     % sonsuzu sonlu değer 1 'eşitlemek
subplot(3,2,5)
stem(n,y)
title('h[n]  işaretinin fourier transformu fazı analitik')
xlabel('Angular frequency w (rad/s) ')
ylabel('Phase (radyan)')


%%
function [xn] = xn_func(n)
%UNTİTLED Summary of this function goes here
%   Detailed explanation goes here
    for i=1:length(n)
        if n(i)>=0 
            xn(i) =  (0.8)^n(i);
        
        else 
            xn(i) = 0;
        end
    end
end