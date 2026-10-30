%firstquestionanalitik.m
Ts = 0.1;%%örneklem katsayısının belirlenmesi
t = -5:Ts: 5;
xt = xt_func(t);
plot(t,xt)
grid on;
ylim([-2,2])
title('x(t) işareti')
xlabel('t (zaman) ')
ylabel('x(t)')
%%
figure
f = -10:0.001:10;
Xf = @(f)(1i./(pi.*f)).*(cos(8.*pi.*f)...
    - (sin(4.*pi.*f)./(4.*pi.*f)));

subplot(4,2,1)
plot(f, abs(Xf(f)))
title('x(t) işaretinin fourier transformu genliği analitik')
xlabel('Frequency Hz ')
ylabel('Amplitude')

subplot(4,2,2)
plot(f, angle(Xf(f)))
title('x(t) işaretinin fourier transformu fazı analitik')
xlabel('Frequency Hz ')
ylabel('Phase (radyan)')
%%
Yfb = exp(-1i.*10.*pi.*f).*Xf(f);
subplot(4,2,3)
plot(f, abs(Yfb))
title('y(t) = x(t-5) işaretinin fourier transformu genliği analitik')
xlabel('Frequency Hz ')
ylabel('Amplitude')

subplot(4,2,4)
plot(f, angle(Yfb))
title('y(t) = x(t-5) işaretinin fourier transformu fazı analitik')
xlabel('Frequency Hz ')
ylabel('Phase (radyan)')
%%
Yfc  = Xf(f-5);
subplot(4,2,5)
plot(f, abs(Yfc))
title('y(t) = x(t).exp(j.10.pi.t) işaretinin fourier transformu genliği analitik')
xlabel('Frequency Hz ')
ylabel('Amplitude')

subplot(4,2,6)
plot(f, angle(Yfc))
title('y(t) = x(t).exp(j.10.pi.t) işaretinin fourier transformu fazı analitik')
xlabel('Frequency Hz ')
ylabel('Phase (radyan)')
%%
Yfd  = 3.*Xf(3.*f);
subplot(4,2,7)
plot(f, abs(Yfd))
title('y(t) = (1/3)x(t/3) işaretinin fourier transformu genliği analitik')
xlabel('Frequency Hz ')
ylabel('Amplitude')

subplot(4,2,8)
plot(f, angle(Yfd))
title('y(t) = (1/3)x(t/3) işaretinin fourier transformu fazı analitik')
xlabel('Frequency Hz ')
ylabel('Phase (radyan)')
%%
figure 
Hf = -1./(cos(8.*pi.*f) - (sin(4.*pi.*f)./(4.*pi.*f)));
subplot(2,1,1)
plot(f, abs(Hf))
title('H(f) frekans tepkisi işaretinin genlik spektrumu analitik')
xlabel('Frequency Hz ')
ylabel('Amplitude')

subplot(2,1,2)
plot(f, angle(Hf))
title('H(f) frekans tepkisi işaretinin faz spektrumu analitik')
xlabel('Frequency Hz ')
ylabel('Phase (radyan)')

%%

function [xt] = xt_func(t)

    for i=1:length(t)
        if t(i)>-4 && t(i)< -2 
            xt(i) =  -1;
        elseif t(i) >= -2 && t(i)<=2
            xt(i) = t(i)/2;
        elseif t(i)> 2 && t(i)<=4
            xt(i) = 1;
        else 
            xt(i) = 0;
        end
    end
end
