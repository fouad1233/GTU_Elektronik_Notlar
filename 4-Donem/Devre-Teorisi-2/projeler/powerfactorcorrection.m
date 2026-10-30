Vs = 230;
f = 50;
w = 2.*pi.*f;
%load1
pf1 = 0.68;%inductive
fi1 = acosd(pf1);%derece cinsinden açı değeri
S1 = 28000;
S1vector = S1 .* exp(fi1.*1i.* (pi ./ 180));
P1 = real(S1vector);
Q1 = imag(S1vector);
%load2
pf2 = 0.82;%Capacitive
fi2 = -acosd(pf2);%derece cinsinden açı değeri
P2 = 5000;
S2 = P2./pf2;
S2vector = S2 .* exp(fi2.*1i.* (pi ./ 180));
Q2 = imag(S2vector);
%load3
pf3 = 1 ;
fi3 = acosd(pf3);%derece cinsinden açı değeri
P3 = 10000;
S3 = P3./pf3;
S3vector = S3 .* exp(fi3.*1i.* (pi ./ 180));
Q3 = imag(S3vector);
%Total
PT = P1 + P2 + P3 ;
QT = Q1 + Q2 + Q3 ;
STvector = PT + 1i*QT;
ST = abs(STvector);
pfT =  PT./ST;
%Compenzation 
pfn = 0.7 : 0.01 : 1;
Qaf = PT.*tand(acosd(pfn));
Qc = QT - Qaf;
Xc = Vs.^2 ./ Qc;
C = 1./(100.*pi.*Xc);
Snvector = PT + 1i.*Qaf;
Sn = abs(Snvector);
Is = Sn./Vs;
plot3(pfn, C, Is)
xlabel("Power factor")
ylabel("Capacitor needed for power factor correction","Rotation",-30,"HorizontalAlignment","right")
zlabel("Current drawn by the source")
figure
mdl = scatteredInterpolant(pfn(:), C(:), Is(:));
[xg, yg] = meshgrid(unique(pfn), unique(C));
zg = mdl(xg, yg);

surf( xg,yg,zg)

xlabel("Power factor")
ylabel("Capacitor needed for power factor correction","Rotation",-30,"HorizontalAlignment","right")
zlabel("Current drawn by the source")
%%
figure
time = out.tout;
current_before = out.currents(:,1);
current_after = out.currents(:,2);
legend()
plot(time,current_before)
hold on 
plot(time,current_after)
legend('Current before compenzation','Current after compenzation',...
    'FontSize',12)
xlabel('Time', 'FontSize',14)
ylabel('Amplitude of currents','FontSize',14)
