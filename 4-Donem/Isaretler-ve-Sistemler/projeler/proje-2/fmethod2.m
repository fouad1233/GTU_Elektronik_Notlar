Fs = 10;            % Sampling frequency                    
T = 1/Fs;             % Sampling period       
L = 1500;             % Length of signal
t = (0:L-1)*T;        % Time vector
xt = xt_func(t);      %the signal as vector

plot(t,xt)
title("The amplitude of x(t)")
xlabel("t")
ylabel("|x(t)|")
figure
plot(t,angle(xt))
title("The amplitude of x(t)")
xlabel("t")
ylabel("|x(t)|")

y = fft(xt);          %the fourier transform of the signal
P2 = y/L;
P1 = P2(1:L/2+1);
%P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(L/2))/L;
figure
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
plot(f,abs(z))
title("Double-Sided Amplitude Spectrum of x(t)")
xlabel("Frequency (Hz)")
ylabel("|y|")

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