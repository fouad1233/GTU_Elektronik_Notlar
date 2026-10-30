Ts = 0.0001; %determination of the sample coefficient
%define the time vector for simulating the signal in time
Tlow = 0;
time = Tlow:Ts:10-Ts;
%define the m(t) signal
m = @(t) 4*cos(2*pi*290.*t);
%%
%Calculations
mt = m(time);
%%
%plot m(t) in the time domian
figure Name 'm(t) in time domain'
grid on;
plot(time, mt,"LineWidth",2)
title('m(t) signal in time domain')
xlabel('Time(sec)')
ylabel('Amplitude')
%%
%%Take fourier transform using fft
mf = fft(mt)/length(mt);%take the fourşer transform using fft
fs = 1/Ts;
figure Name 'M(f)'
n = length(mt);
%take the shift of the spectra of the fourier transform
fshift = (-n/2:n/2-1)*(fs/n);
mfshift = fftshift(mf);
plot(fshift,abs(mfshift))
%xlim([-50,50])%limit the frequency x axis
% between -50 and 50 for best view
title('|M(f)|')
xlabel('Frequency (Hz)')
ylabel('Magnitude')