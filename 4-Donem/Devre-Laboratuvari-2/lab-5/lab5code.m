R= 500;
C = 47.*10.^-9;
L = 33.*10.^-3;
w0  = 1./ sqrt(L*C)
f0 = w0./ (2.*pi)
w1 = - (R./(2*L)) + sqrt( ( (R ./ (2*L)).^2) + 1./(L.*C) )
f1 = w1./ (2.*pi)
w2 =  (R./(2*L)) + sqrt( ( (R ./ (2*L)).^2) + 1./(L.*C) )
f2 = w2./ (2.*pi)
B = w2 - w1
Q = (w0.*L)./R

wc = 1 ./(R.*C)
fc = wc ./ (2.*pi)
Hs1 = tf([R,0],[L,R,1/C]);
bode(Hs1)
xlim([1,10*10^9])
grid on
figure 
Hs2 = tf([R,1/C],[L,R,1/C]);
bode(Hs2)
xlim([1,10*10^9])
grid on

%%
frequency = [1,2,2.5,3,3.5,3.75,4.041,4.5,5,6,7,9,12];
voltage = [0.82,1.82,2.46,2.54,2.54,2.54,2.54,2.54,2.54,2.54,2.20,1.70,1.18];
plot(frequency,voltage)
xlabel('Frequency (Khz)')
ylabel('Voltage(V)')
%%
frequency = [1,2,2.5,3,3.5,3.75,4.041,4.5,5,6,7,9,12];
voltage = [0.624,0.736,0.816,0.888,0.960,0.880,0.840,0.720,0.664,...
    0.468,0.384,0.296,0.208];

plot(frequency,voltage)
xlabel('Frequency (Khz)')
ylabel('Voltage(V)')

%%
figure
plot(frequency,20.*log(voltage./5))
