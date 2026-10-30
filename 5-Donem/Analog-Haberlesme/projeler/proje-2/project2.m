Ts = 0.001; %determination of the sample coefficient
%define the time vector for simulating the signal in time
Tlow = -10;
time = Tlow:Ts:10-Ts;
%define the m(t) signal
m = @(t) square_wave((t - 1)./2 ) - square_wave((t - 3)./2 );
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
mf = fft(mt)*Ts;%take the fourşer transform using fft
fs = 1/Ts;
figure Name 'M(f)'
n = length(mt);
%take the shift of the spectra of the fourier transform
fshift = (-n/2:n/2-1)*(fs/n);
mfshift = fftshift(mf);
plot(fshift,abs(mfshift))
xlim([-50,50])%limit the frequency x axis
% between -50 and 50 for best view
title('M(f)')
xlabel('Frequency (Hz)')
ylabel('Magnitude')
%%
kf = 50;
fi = @(t) 2*pi*kf.*integral(m,Tlow,t);

fit = zeros(size(time));
for i = 1:length(time)
    fit(i) = fi(time(i));
end
yt = 5.*(cos(500*pi.*time+ fit));

figure Name 'y(t) in time domian'
plot(time, yt,"LineWidth",2)
title('y(t) signal in time domain')
xlim([-0.01,0.01])
xlabel('Time(sec)')
ylabel('Amplitude')


%%


%%

function [yt] = square_wave(xt)
% return a square wave with amplitude equal to 1 and width 1
    yt = zeros(size(xt));
    for i = 1:length(xt)
        if abs(xt(i)) >= -1/2 && abs(xt(i)) <=  1/2
            yt(i) = 1;
        else
            yt(i) = 0;
        end
    end
end


