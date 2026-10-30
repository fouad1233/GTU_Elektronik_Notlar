%% a section code
% Define system function
m = @(t) 5.*cos(200.*pi.*t) + 10.*cos(400.*pi.*t);
c = @(t) 2.*cos(2000.*pi.*t);
x = @(t) (m(t) + c(t));
z = @(t) (60*x(t) + x(t).^2);
Ts = 0.00002; %determination of the sample coefficient
%define the time vector for simulating the signal in time
time = -1:Ts:1-Ts;
%%
%Calculations
mt = m(time);
et = c(time);
xt = x(time);
zt = z(time);

%%
%Plot the signals in time domian
figure
grid on;
subplot (2,2,1);
plot(time, mt)
title('m(t) signal in time domain')
xlim([-0.02,0.02])
xlabel('Time(sec)')
ylabel('Amplitude')

subplot (2,2,2);
plot(time, et)
xlim([-0.02,0.02])
title('c(t) signal in time domain')
xlabel('Time(sec)')
ylabel('Amplitude')

subplot (2,2,3);
plot(time, xt)
xlim([-0.02,0.02])
title('x(t) signal in time domain')
xlabel('Time(sec)')
ylabel('Amplitude')

subplot (2,2,4);
plot(time, zt)
xlim([-0.02,0.02])
title('z(t) signal in time domain')
xlabel('Time(sec)')
ylabel('Amplitude')

%%
%%Take fourier transform using fft
mf = fft(mt)/length(mt);%take the fourşer transform using fft
fs = 1/Ts;
figure
subplot(2,2,1)
n = length(mt);
%take the shift of the spectra of the fourier transform
fshift = (-n/2:n/2-1)*(fs/n);
mfshift = fftshift(mf);
plot(fshift,abs(mfshift))
xlim([-2000,2000])%limit the frequency x axis
% between -2000 and 2000 for best view
title('M(f)')
xlabel('Frequency (Hz)')
ylabel('Magnitude')


xf = fft(xt)* Ts;
subplot(2,2,2)
n = length(xt);
fshift = (-n/2:n/2-1)*(fs/n);
xfshift = fftshift(xf);
plot(fshift,abs(xfshift))
xlim([-2000,2000])
title('X(f)')
xlabel('Frequency (Hz)')
ylabel('Magnitude')


zf = fft(zt)* Ts;
subplot(2,2,3)
n = length(zt);
fshift = (-n/2:n/2-1)*(fs/n);
zfshift = fftshift(zf);
plot(fshift,abs(zfshift))
xlim([-2000,2000])
title('Z(f)')
xlabel('Frequency (Hz)')
ylabel('Magnitude')

%%
fc = 1000;
bw = 400;
[yt,yfshift] = bandwidthFilterFrequencyDomain(zfshift,fshift,fs,fc,bw);
subplot(2,2,4)
plot(fshift,abs(yfshift))
xlim([-2000,2000])
title('Y(f)')
xlabel('Frequency (Hz)')
ylabel('Magnitude')

%% 
figure
yt = real(yt);
plot(time,yt )
title('y(t) signal in time domain')
xlim([-0.02,0.02])
xlabel('Time(sec)')
ylabel('Amplitude')
%%
figure
plot(time, yt)
hold on 
[dtup , dtlow] = envelope(yt,100, 'peak');
plot(time,dtup)
plot(time,-dtup)
xlim([-0.02,0.02])
title('y(t), d(t) up, and d(t) down signal in time domain')
xlabel('Time(sec)')
ylabel('Amplitude')
hold off
%%
figure

subplot(2,2,1)
plot(time, yt)
hold on 
C1 = 100*10^-9;
R1 = 20*10^3;
at = envelope_detector(time,yt,C1,R1);
plot(time, at)
title('a(t) signal: envelope detector circuit')
xlabel('Time(sec)')
ylabel('Amplitude')
xlim([-0.01,0.01])
%calculate the fourier transform of a(t) 
% than add high pass filter for ignore the dc signal
af = fft(at)* Ts;

subplot(2,2,2)
n = length(at);
fshift = (-n/2:n/2-1)*(fs/n);
afshift = fftshift(af);
plot(fshift,abs(afshift))
xlim([-5000,5000])
title('A(f)')
xlabel('Frequency (Hz)')
ylabel('Magnitude')

subplot(2,2,3)
fc = 50;
[bt,bf] = highPassFilterFrequencyDomain(afshift,fshift,fs,fc);
plot(fshift,abs(bf))
xlim([-5000,5000])
title('B(f): the signal A(f) fitered in frequency domain')
xlabel('Frequency (Hz)')
ylabel('Magnitude')
subplot(2,2,4)
plot(time,bt)
xlim([-0.01,0.01])
title('b(t): the signal a(t) fitered to ignore dc signal')
xlabel('Time(sec)')
ylabel('Amplitude')

%%
figure
%to filter the ripples, a low pass filter is used 
% because ripples have high frequency
fc = 200;
[et,ef] = lowPassFilterFrequencyDomain(bf,fshift,fs,fc);
subplot(2,1,1)
plot(fshift,abs(ef))
xlim([-1000,1000])
title('E(f): the signal B(f) fitered in frequency domain')
xlabel('Frequency (Hz)')
ylabel('Magnitude')
subplot(2,1,2)
plot(time,et)
xlim([-0.01,0.01])
title('e(t): the signal b(t) fitered to remove ripples')
xlabel('Time(sec)')
ylabel('Amplitude')

%%
%Lets plot m(t) and e(t)
%%figure
hold on
plot(time,mt,"Marker","*",MarkerIndices=1:10:length(mt))
plot(time,et)
xlim([-0.01,0.01])
title('m(t) and e(t) signals')
legend('m(t)','e(t)')
xlabel('Time(sec)')
ylabel('Amplitude')



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
function [bt,bf] = highPassFilterFrequencyDomain(af,f,fs,fc)
% Compute the magnitude response of the filter
   H = zeros(size(f));
    for i = 1:length(f)
        if abs(f(i)) >= fc 
            H(i) = 1;
        else
            H(i) = 0;
        end
    end
    % Apply the filter to the frequency domain signal
    bf = af .* H;
    % Obtain the time-domain signal using the inverse Fourier transform
    bt = ifft(ifftshift(bf)).*fs;

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
    et = ifft(ifftshift(ef)).*fs;

end

%%
function [yt,yf] = bandwidthFilterFrequencyDomain(xf,f,fs,fc,bw)
% Compute the magnitude response of the filter
    H = zeros(size(f));
    for i = 1:length(f)
        if abs(f(i)) >= fc - bw/2 && abs(f(i)) <= fc + bw/2
            H(i) = 1;
        else
            H(i) = 0;
        end
    end
    % Apply the filter to the frequency domain signal
    yf = xf .* H;
    % Obtain the time-domain signal using the inverse Fourier transform
    yt = ifft(ifftshift(yf)).*fs;

end



