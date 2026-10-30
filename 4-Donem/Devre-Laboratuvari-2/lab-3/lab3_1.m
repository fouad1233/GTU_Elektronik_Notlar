Vs = 5;
%w = 10^4 * pi;
f = 100:100:10^6;
w = 2.*pi.*f;
Z1 = 820 + 1i.*w.*33*10^-3;
Z2 = 820 + 1./(1i.*w.*47.*10^-9);
Zr1 = 820;
Zr2 = 820;
Zl = 1i *w*33*10^-3;
Zc = 1./(1i.*w.*47.*10^-9);
Vz1 = (Z1./(Z1+Z2)) .* Vs;
Vz2 = (Z2./(Z1+Z2)) .* Vs;
Vr1 = (Zr1./(Z1+Z2)) .* Vs;
Vr2 = (Zr2./(Z1+Z2)) .* Vs;
Vl = (Zl./(Z1+Z2)) .* Vs;
Vc = (Zc./(Z1+Z2)) .* Vs;
Is = Vr2./Zr2;
plot(f, abs(Is))
title("Akımın frekansa göre değişimi(Fouad Aladhami)")
xlabel("f","FontWeight","bold")
ylabel("|I|","FontWeight","bold")
%Fouad Aladhami