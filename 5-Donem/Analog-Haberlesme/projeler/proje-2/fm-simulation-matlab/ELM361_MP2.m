save_path = 'figures/';
mkdir(save_path)
%%
fig_counter = 1;
%%
Ts = 0.00001; %determination of the sample coefficient
%define the time vector for simulating the signal in time
Tlow = -3;
time = Tlow:Ts:5-Ts;
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
saveas(gcf,append(save_path,string(fig_counter),'- m(t) in time domain'),'png')
fig_counter=fig_counter+ 1;
%%
%%Take fourier transform using fft
fs = 1/Ts;
mf = fft(mt)/fs;%take the fourier transform using fft
figure Name 'M(f)'
n = length(mt);
%take the shift of the spectra of the fourier transform
fshift = (-n/2:n/2-1)*(fs/n);
mfshift = fftshift(mf);
plot(fshift,abs(mfshift))
xlim([-50,50])%limit the frequency x axis
% between -50 and 50 for best view
title('|M(f)|')
xlabel('Frequency (Hz)')
ylabel('Magnitude')
saveas(gcf,append(save_path,string(fig_counter),'- M(f)'),'png')
fig_counter=fig_counter+ 1;

%%
kf = 50;
%fi = @(t) 2*pi*kf.*integral(m,-1,t);

fit = zeros(size(time));
for i = 2:length(time)
    fit(i) = fit(i-1) + (2*pi*kf*mt(i) *Ts);
end
Ac =5;
yt = Ac.*(cos(500*pi.*time+ fit));

%%
figure Name 'fi(t) in time domain'
plot(time, fit,"LineWidth",2)
title('fi(t) signal in time domain')
%xlim([-0.01,0.01])
xlabel('Time(sec)')
ylabel('Amplitude')
saveas(gcf,append(save_path,string(fig_counter),'- fi(t) in time domain'),'png')
fig_counter=fig_counter+ 1;

%%
%%Take fourier transform using fft
fs = 1/Ts;
yf = fft(fit)/fs;%take the fourşer transform using fft
figure Name 'Fi(f)'
n = length(fit);
%take the shift of the spectra of the fourier transform
fshift = (-n/2:n/2-1)*(fs/n);
fifshift = fftshift(yf);
plot(fshift,abs(fifshift))
xlim([-20,20])%limit the frequency x axis
% between -10 and 10 for best view
title('|Fi(f)|')
xlabel('Frequency (Hz)')
ylabel('Magnitude')
saveas(gcf,append(save_path,string(fig_counter),'- Fi(f)'),'png')
fig_counter=fig_counter+ 1;

%%
figure Name 'y(t) in time domian'
plot(time, yt,"LineWidth",2)
title('y(t) signal in time domain')
%xlim([-0.01,0.01])
xlabel('Time(sec)')
ylabel('Amplitude')
saveas(gcf,append(save_path,string(fig_counter),'- y(t) signal in time domain'),'png')
fig_counter=fig_counter+ 1;
%%
figure Name 'y(t) in time domian from 3.95 to 4.05'
plot(time, yt,"LineWidth",2)
title('y(t) signal in time domain from 3.95 to 4.05')
xlim([3.95,4.05])
xlabel('Time(sec)')
ylabel('Amplitude')
saveas(gcf,append(save_path,string(fig_counter),'- y(t) in time domian from 3.95 to 4.05'),'png')
fig_counter=fig_counter+ 1;
%%
figure Name 'y(t) in time domian from 1.95 to 2.05'
plot(time, yt,"LineWidth",2)
title('y(t) signal in time domain from 1.95 to 2.05')
xlim([1.95,2.05])
xlabel('Time(sec)')
ylabel('Amplitude')
saveas(gcf,append(save_path,string(fig_counter),'- y(t) in time domian from 1.95 to 2.05'),'png')
fig_counter=fig_counter+ 1;

%%
%%Take fourier transform using fft
yf = fft(yt)/length(yt);%take the fourşer transform using fft
fs = 1/Ts;
figure Name 'Y(f)'
n = length(yt);
%take the shift of the spectra of the fourier transform
fshift = (-n/2:n/2-1)*(fs/n);
yfshift = fftshift(yf);
plot(fshift,abs(yfshift))
xlim([-1000,1000])%limit the frequency x axis
% between -10 and 10 for best view
title('|Y(f)|')
xlabel('Frequency (Hz)')
ylabel('Magnitude')
saveas(gcf,append(save_path,string(fig_counter),'- Y(f)'),'png')
fig_counter=fig_counter+ 1;
%%
%Take the derivative of the y(t) signal and plot in time domain
ydt = diff(yt)/Ts;
figure Name 'y(t) derivative yd(t) in time domain'
plot(time(1:end-1), ydt,"LineWidth",2)
title('y(t) derivative in time domain')
%xlim([-0.01,0.01])
xlabel('Time(sec)')
ylabel('Amplitude')
saveas(gcf,append(save_path,string(fig_counter),'- y(t) derivative yd(t) in time domain'),'png')
fig_counter=fig_counter+ 1;
%%
%Take fourier transform using fft and plot in frequency domain
ytdf = fft(ydt)/length(ydt);%take the fourşer transform using fft
fs = 1/Ts;
figure Name '|Yd(f)| '
n = length(ydt);
%take the shift of the spectra of the fourier transform
fshift = (-n/2:n/2-1)*(fs/n);
ytdfshift = fftshift(ytdf);
plot(fshift,abs(ytdfshift))
xlim([-1000,1000])%limit the frequency x axis
% between -10 and 10 for best view
title('|Yd(f)|')
xlabel('Frequency (Hz)')
saveas(gcf,append(save_path,string(fig_counter),'- |Yd(f)|'),'png')
fig_counter=fig_counter+ 1;

%%
sinc = @(x) sin(pi.*x)./(pi.*x);
%%
fshift = -100:0.001:100;
figure Name 'M(f) from analitic solution'
mfanalitic = (2.*sinc(2.*fshift)).*(exp(-1i*2*pi.*fshift)-exp(-1i*2*pi*3.*fshift));
plot(fshift,abs(mfanalitic))
xlim([-50,50])%limit the frequency x axis
title('|M(f)| from analitic')
xlabel('Frequency (Hz)')
ylabel('Magnitude')
%saveas(gcf,append(save_path,string(fig_counter),'- |M(f)| from analitic'),'png')
%fig_counter=fig_counter+ 1;


%%
C1 = 1000*10^-9;
R1 = 100*10^3;


%%
at = envelope_detector(time(1:end-1),ydt,C1,R1);
figure Name 'a(t)'
plot(time(1:end-1), at)
title('a(t) signal: envelope detector circuit')
xlabel('Time(sec)')
ylabel('Amplitude')
saveas(gcf,append(save_path,string(fig_counter),'- a(t) signal: envelope detector circuit'),'png')
fig_counter=fig_counter+ 1;
%%
%calculate the fourier transform of a(t) 
af = fft(at)/length(at);
figure Name '|A(f)|'
n = length(at);
fshift = (-n/2:n/2-1)*(fs/n);
afshift = fftshift(af);
plot(fshift,abs(afshift))
xlim([-5000,5000])
title('|A(f)|')
xlabel('Frequency (Hz)')
ylabel('Magnitude')
saveas(gcf,append(save_path,string(fig_counter),'- |A(f)|'),'png')
fig_counter=fig_counter+ 1;
%%
figure Name '|E(f)|'
%to filter the ripples, a low pass filter is used 
% because ripples have high frequency
fc = 20;
[et,ef] = lowPassFilterFrequencyDomain(afshift,fshift,fs,fc);
plot(fshift,abs(ef))
xlim([-50,50])
title('|E(f)|: the signal A(f) fitered in frequency domain')
xlabel('Frequency (Hz)')
ylabel('Magnitude')
saveas(gcf,append(save_path,string(fig_counter),'- |E(f)|'),'png')
fig_counter=fig_counter+ 1;
%%
figure Name 'e(t)'
plot(time(1:end-1),et)
title('e(t): the signal a(t) fitered to remove ripples')
xlabel('Time(sec)')
ylabel('Amplitude')
saveas(gcf,append(save_path,string(fig_counter),'- e(t): the signal b(t) fitered to remove ripples'),'png')
fig_counter=fig_counter+ 1;
%%
figure Name 'en(t)'
ent = et./(2*pi*kf*Ac);
plot(time(1:end-1),ent)
title('en(t): e(t) signal normalized')
xlabel('Time(sec)')
ylabel('Amplitude')
saveas(gcf,append(save_path,string(fig_counter),'- en(t): e(t) signal normalized'),'png')
fig_counter=fig_counter+ 1;

%%
%Lets plot m(t) and e(t)

figure Name 'm(t) and en(t) signals'
hold on
plot(time,mt,"Marker","*",MarkerIndices=1:10:length(mt))
plot(time(1:end-1),ent)
title('m(t) and en(t) signals')
legend('m(t)','en(t)')
xlabel('Time(sec)')
ylabel('Amplitude')
saveas(gcf,append(save_path,string(fig_counter),'- m(t) and en(t) signals'),'png')
fig_counter=fig_counter+ 1;
%%
%filter the dc signal of e(t)
zt = filterDC(ent);
figure Name 'z(t)'
plot(time(1:end-1),zt)
title('z(t): the signal en(t) fitered by capacitor to remove dc signal')
xlabel('Time(sec)')
saveas(gcf,append(save_path,string(fig_counter),'- z(t): the signal en(t) fitered'),'png')
fig_counter=fig_counter+ 1;
%%
%calculate the fourier transform of z(t) 
zf = fft(zt)/fs;
figure Name '|Z(f)|'
n = length(zt);
fshift = (-n/2:n/2-1)*(fs/n);
zfshift = fftshift(zf);
plot(fshift,abs(zfshift))
xlim([-50,50])
title('|Z(f)|')
xlabel('Frequency (Hz)')
ylabel('Magnitude')
saveas(gcf,append(save_path,string(fig_counter),'- |Z(f)|'),'png')
fig_counter=fig_counter+ 1;

%%
figure Name 'm(t) and z(t)'
hold on
plot(time,mt,"Marker","*",MarkerIndices=1:10000:length(mt))
plot(time(1:end-1),zt)
title('m(t) and z(t) signals')
legend('m(t)','z(t)')
xlabel('Time(sec)')
ylabel('Amplitude')
saveas(gcf,append(save_path,string(fig_counter),'- m(t) and z(t) signals'),'png')
fig_counter=fig_counter+ 1;

%%
function [at] = envelope_detector(time,yt,C1,R1)
   at = zeros(size(yt));
   at(1)= yt(1);
   i0 = 1;
   for i = 2:length(time)
        if yt(i)>0 && yt(i)>at(i-1)
            if yt(i) >= yt(i- 1)
                at(i) = yt(i);
                i0 = i;
            else
                at(i) = yt(i0).* exp(-(time(i)- time(i0))/(R1.*C1));
            end
        else
            at(i) = yt(i0).* exp(-(time(i)- time(i0))/(R1.*C1));
        end
    end
    

end

%%
function [et,ef] = lowPassFilterFrequencyDomain(bf,f,fs,fc)
% Compute the magnitude response of the filter
   H = zeros(size(f));
    for i = 1:length(f)
        if abs(f(i)) <= fc 
            H(i) = 1;
        else
            H(i) = 0;
        end
    end
    % Apply the filter to the frequency domain signal
    ef = bf .* H;
    % Obtain the time-domain signal using the inverse Fourier transform
    et = ifft(ifftshift(ef)).*length(bf);
end
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

%%
% function to filter DC signal of e(t) signal by taking the average
%  of the signal and subtracting it from the signal

function [zt] = filterDC(et)
    zt = et - mean(et);
end
