% Define filter parameters
R = 1000; % Resistance in ohms
C = 1e-6; % Capacitance in farads
Fs = 1000; % Sampling frequency in Hz

% Define a sample signal (mix of DC and AC)
t = 0:1/Fs:1;
x = 1 + sin(2*pi*50*t); % DC component (1) and AC component (50 Hz)

% Apply the high-pass filter
y = high_pass_filter(x, R, C, Fs);

% Plot the original and filtered signals
figure;
subplot(2,1,1);
plot(t, x);
title('Original Signal');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(2,1,2);
plot(t, y);
title('Filtered Signal (High-Pass)');
xlabel('Time (s)');
ylabel('Amplitude');


function y = high_pass_filter(x, R, C, Fs)
    % Initialize the output signal
    y = zeros(size(x));
    
    % Calculate filter coefficients
    alpha = R*C*Fs / (R*C*Fs + 1);
    beta = (R*C*Fs - 1) / (R*C*Fs + 1);
    
    % Apply the high-pass filter
    for n = 2:length(x)
        y(n) = alpha * (x(n) - x(n-1)) + beta * y(n-1);
    end
end
