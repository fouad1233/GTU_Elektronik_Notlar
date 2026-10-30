%%
Ts = 0.1;%%örneklem katsayısının belirlenmesi
t = -5:Ts: 5;
xt = xt_func(t);
%subplot(4,2,1)
%plot(t,xt)
%title('xt işareti')
%xlabel('Time (seconds)')
%ylabel('Amplitude')


y = fft(xt)*Ts;
fs = 1/Ts;
f= (0:length(y)-1)*fs/length(y);
%subplot(4,1,2)
%plot(f,abs(y))
%xlabel('Frequency (Hz)')
%ylabel('Magnitude')
%title('Magnitude')


subplot(4,2,1)
n = length(xt);
fshift = (-n/2:n/2-1)*(fs/n);
yshift = fftshift(y);
plot(fshift,abs(yshift))
xlim([-10,10])
title('Matlab ile fft genliği')
xlabel('Frequency (Hz)')
ylabel('Magnitude')

subplot(4,2,2)
%tol = 1e-6;
%yshift(abs(yshift) < tol) = 0;
plot(fshift,angle(yshift))
xlim([-10,10])
title('Matlab ile fft fazı')
xlabel('Frequency (Hz)')
ylabel('Phase (Degree)')
%%
Ts = 0.1;%%örneklem katsayısının belirlenmesi
t = -5:Ts: 5;
xt = xt_func(t-5);

y = fft(xt)*Ts;
fs = 1/Ts;
f= (0:length(y)-1)*fs/length(y);

subplot(4,2,3)
n = length(xt);
fshift = (-n/2:n/2-1)*(fs/n);
yshift = fftshift(y);
plot(fshift,abs(yshift))
xlim([-10,10])
title('Matlab ile fft genliği')
xlabel('Frequency (Hz)')
ylabel('Magnitude')

subplot(4,2,4)

plot(fshift,angle(yshift))
xlim([-10,10])
title('Matlab ile fft fazı')
xlabel('Frequency (Hz)')
ylabel('Phase (Degree)')
%%
Ts = 0.1;%%örneklem katsayısının belirlenmesi
t = -5:Ts: 5;
xt = exp(10i.*pi.*t).*xt_func(t);
y = fft(xt)*Ts;
fs = 1/Ts;
f= (0:length(y)-1)*fs/length(y);

subplot(4,2,5)
n = length(xt);
fshift = (-n/2:n/2-1)*(fs/n);
yshift = fftshift(y);
plot(fshift,abs(yshift))
xlim([-10,10])
title('Matlab ile fft genliği')
xlabel('Frequency (Hz)')
ylabel('Magnitude')

subplot(4,2,6)

plot(fshift,angle(yshift))
xlim([-10,10])
title('Matlab ile fft fazı')
xlabel('Frequency (Hz)')
ylabel('Phase (Degree)')
%%
Ts = 0.1;%%örneklem katsayısının belirlenmesi
t = -5:Ts: 5;
xt = (1/3)*xt_func(t./3);
y = fft(xt)*Ts;
fs = 1/Ts;
f= (0:length(y)-1)*fs/length(y);

subplot(4,2,7)
n = length(xt);
fshift = (-n/2:n/2-1)*(fs/n);
yshift = fftshift(y);
plot(fshift,abs(yshift))
xlim([-10,10])
title('Matlab ile fft genliği')
xlabel('Frequency (Hz)')
ylabel('Magnitude')

subplot(4,2,8)
%tol = 1e-6;
%yshift(abs(yshift) < tol) = 0;
plot(fshift,angle(yshift))
xlim([-10,10])
title('Matlab ile fft fazı')
xlabel('Frequency (Hz)')
ylabel('Phase (Degree)')



function [xt] = xt_func(t)
%UNTİTLED Summary of this function goes here
%   Detailed explanation goes here
    for i=1:length(t)
        if t(i)>-4 && t(i)< -2 
            xt(i) =  -1;
        elseif t(i) >= -2 && t(i)<=2
            xt(i) = t(i)/2;
        elseif t(i)> 2 && t(i)<=4
            xt(i) = 1;
        else 
            xt(i) = 0;
        end
    end
end
