Fs = 10;            % Sampling frequency                    
T = 1/Fs;             % Sampling period       
L = 1500;             % Length of signal
t = (0:L-1)*T;        % Time vector
xt = xt_func(t);      %the signal as vector
y = fft(xt);          %the fourier transform of the signal

P2 = y/L;
P1 = P2(1:L/2+1);
%P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(L/2))/L;
plot(f,abs(P1)) 
title("Single-Sided Amplitude Spectrum of X(t)")
xlabel("f (Hz)")
ylabel("|P1(f)|")
figure
plot(f,angle(P1)) 
title("Single-Sided Phase Spectrum of x(t)")
xlabel("f (Hz)")
ylabel("P1(f) pahse")
%%
figure
z = fftshift(y);

P2 = abs(z/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);

plot(abs(fftshift(y)))
ly = length(z);
f = (-ly/2:ly/2-1)/ly*Fs;
plot(f,z)
title("Double-Sided Amplitude Spectrum of x(t)")
xlabel("Frequency (Hz)")
ylabel("|y|")




%%
Ts = 0.1;
t = -6:Ts: 6;
xt = xt_func(t);
subplot(4,2,1)
plot(t,xt)
xlabel('Time (seconds)')
ylabel('Amplitude')


y = fft(xt)*Ts;
fs = 1/Ts;
f= (0:length(y)-1)*fs/length(y);
%subplot(4,1,2)
%plot(f,abs(y))
%xlabel('Frequency (Hz)')
%ylabel('Magnitude')
%title('Magnitude')


subplot(4,2,2)
n = length(xt);
fshift = (-n/2:n/2-1)*(fs/n);
yshift = fftshift(y);
plot(fshift,abs(yshift))
xlabel('Frequency (Hz)')
ylabel('Magnitude')

subplot(4,2,3)
tol = 1e-6;
yshift(abs(yshift) < tol) = 0;
plot(fshift,angle(yshift).*180./pi)
xlabel('Frequency (Hz)')
ylabel('Phase (Degree)')


subplot(4,2,4)
yfhand = (1i./(pi.*fshift)).*cos(8.*pi.*fshift) +...
    (1./((pi.^2).*fshift)).*cos(4.*pi.*fshift);
plot(fshift,abs(yfhand));
xlabel('Frequency (Hz)')
ylabel('Magnitude')

subplot(4,2,5)
plot(fshift,angle(yfhand).*(180./pi));
xlabel('Frequency (Hz)')
ylabel('Phase (Degree)')













function [xt] = xt_func(t)
%UNTİTLED Summary of this function goes here
%   Detailed explanation goes here
    for i=1:length(t)
        if t(i)>-4 && t(i)< -2 
            xt(i) =  -1;
        elseif t(i) >= -2 && t(i)<2
            xt(i) = t(i)/2;
        elseif t(i)>= 2 && t(i)<4
            xt(i) = 1;
        else 
            xt(i) = 0;
        end
    end
end
