n = 0:100;  % Time indices
Xw = fft(xn_func(n));  % Compute the Fourier transform of xn

% Plot the magnitude spectrum
subplot(4,2,1)
w = linspace(-pi, pi, length(n));
stem(w, abs(fftshift(Xw)));
xlabel('Angular Frequency (w)');
ylabel('Magnitude |X(w)|');
title('Fourier Transform of xn');
subplot(4,2,2)
stem(w, angle(fftshift(Xw)));
xlabel('Angular Frequency (w)');
ylabel('Phase');
title('Fourier Transform of xn');

%%
shifted_n = n - 5;  % Shift the time index by 5
Ywb = fft(xn_func(shifted_n));  % Compute the Fourier transform of x[n-5]

% Plot the magnitude spectrum
subplot(4,2,3)
w = linspace(-pi, pi, length(shifted_n));
stem(w, abs(fftshift(Ywb)));
xlabel('Angular Frequency (w)');
ylabel('Magnitude |X(w)|');
title('Fourier Transform of x[n-5]');
subplot(4,2,4)
stem(w, angle(fftshift(Ywb)));
xlabel('Angular Frequency (w)');
ylabel('Phase');
title('Fourier Transform of x[n-5]');
%%
% Compute the signal y[n]
ync = n .* xn_func(n);

% Compute the Fourier transform of y[n]
Ywc = fft(ync);

% Plot the magnitude spectrum
subplot(4, 2, 5)
w = linspace(-pi, pi, length(n));
stem(w, abs(fftshift(Ywc)));
xlabel('Angular Frequency (w)');
ylabel('Magnitude |Y(w)|');
title('Fourier Transform of y[n] = nx[n]');

% Plot the phase spectrum
subplot(4, 2, 6)
stem(w, angle(fftshift(Ywc)));
xlabel('Angular Frequency (w)');
ylabel('Phase');
title('Fourier Transform of y[n] = nx[n]');
%%
n = -100:0;
% Compute the signal y[n]
ynd = xn_func(-n);

% Compute the Fourier transform of y[n]
Ywd = fft(ynd);

% Plot the magnitude spectrum
subplot(4, 2, 7)
w = linspace(-pi, pi, length(n));
stem(w, abs(fftshift(Ywd)));
xlabel('Angular Frequency (w)');
ylabel('Magnitude |Y(w)|');
title('Fourier Transform of y[n]');

% Plot the phase spectrum
subplot(4, 2, 8)
stem(w, angle(fftshift(Ywd)));
xlabel('Angular Frequency (w)');
ylabel('Phase');
title('Fourier Transform of y[n]');

%%
n = 0:100;  % Time indices
figure
yn = yn_function(n);
Yw = fft(yn);
Hw = Yw./Xw;
subplot(2,1,1)
plot(w, abs(fftshift(Hw)));
xlabel('Angular Frequency (w)');
ylabel('Amplitude');
title('Frequency responce H(ejw ) Magnitude');
subplot(2,1,2)
plot(w, angle(fftshift(Hw)));
xlabel('Angular Frequency (w)');
ylabel('Amplitude');
title('Frequency responce H(ejw ) phase');
%%
function [yn] = yn_function(n)
    yn = zeros(size(n));
    for i=1:length(n)
        if n(i)==5 
            yn(i) =  1;
        
        else 
            yn(i) = 0;
        end
    end
end


function [xn] = xn_func(n)

    xn = zeros(size(n));
    for i=1:length(n)
        if n(i)>=0 
            xn(i) =  (0.8)^n(i);
        
        else 
            xn(i) = 0;
        end
    end
end