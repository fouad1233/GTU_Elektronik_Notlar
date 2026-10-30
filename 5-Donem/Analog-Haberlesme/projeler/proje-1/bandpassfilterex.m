% Your existing code
m = @(t) 5.*cos(200.*pi.*t) + 10.*cos(400.*pi.*t);
c = @(t) 2.*cos(2000.*pi.*t);
x = @(t) (m(t) + c(t));
z = @(t) (60*x(t) + x(t).^2);
Ts = 0.00001; % Sample coefficient
time = -0.02:Ts:0.02;

% Calculations
mt = m(time);
ct = c(time);
xt = x(time);
zt = z(time);

% Designing the Bandpass Filter
centerFrequency = 1000; % in Hz
bandwidth = 400; % in Hz
fs = 1/Ts; % Sampling frequency

% Calculate the lower and upper cutoff frequencies
fLow = centerFrequency - bandwidth/2;
fHigh = centerFrequency + bandwidth/2;

% Design the filter
bpFilter = designfilt('bandpassfir', 'FilterOrder', 1000, ...
             'CutoffFrequency1', fLow, 'CutoffFrequency2', fHigh, ...
             'SampleRate', fs);

% Apply the filter
filteredZt = filter(bpFilter, zt);

% Plotting
figure;
subplot(2,1,1);
plot(time, zt);
title('Original Signal z(t)');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(2,1,2);
plot(time, filteredZt);
title('Filtered Signal');
xlabel('Time (s)');
ylabel('Amplitude');
