Vs = 5;
%w = 10^4 * pi;
f = 100:100:10^6;
w = 2.*pi.*f;
Zr1 = 820;
Zr2 = 820;
Zl = 1i *w*33*10^-3;
Zc = 1./(1i.*w.*47.*10^-9);
Z1 = Zr1 + Zl;
Z2 = 820 + Zc;
Zeq = (Z1.*Z2) ./(Z1+Z2);
Is = Vs./Zeq;
Isabs = abs(Is)*1000;%ma
Isph = angle(Is).*180./pi;
I1 = (Z2/(Z1+Z2)).*Is;
Is1abs = abs(I1).*1000;%ma
Is1ph = angle(I1).*180./pi;
I2 = (Z1/(Z1+Z2)).*Is;
Is2abs = abs(I2).*1000;%ma
Is2ph = angle(I2).*180./pi;
Vr1 = I1.*Zr1;
Vr1abs = abs(Vr1);
Vr1phase = angle(Vr1).*180./pi;
Vr2 = I2.*Zr2;
Vr2abs = abs(Vr2);
Vr2phase = angle(Vr2).*180./pi;
Vl1 = I1.*Zl;
Vl1abs = abs(Vl1);
Vl1phase = angle(Vl1).*180./pi;
Vc1 = I2.*Zc;
Vc1abs = abs(Vc1);
Vc1phase = angle(Vc1).*180./pi;

subplot(2,1,1)
plot(f, abs(I1))
title("I1 Akımının frekansa göre değişimi(Fouad Aladhami)")
xlabel("f","FontWeight","bold")
ylabel("|I1|","FontWeight","bold")

subplot(2,1,2)
plot(f,abs(I2))
title("I2 Akımının frekansa göre değişimi(Fouad Aladhami)")
xlabel("f","FontWeight","bold")
ylabel("|I2|","FontWeight","bold")
%Fouad Aladhami