% Küreler için potansiyeller (r = 5 cm ve r = 10 cm)
V1 = 5;
V2 = 10;
r1 = 5*10^-2;  % Cm cinsinden verildiği için metreye çeviriyoruz
r2 = 10*10^-2;   % Cm cinsinden verildiği için metreye çeviriyoruz

r = 0 :10^-6: 2*r2;
[Vr,Er] = potansiyelAndField(r,r1,r2,V1,V2);

figure;
subplot(2,1,1);
plot(r,Vr,"LineWidth",3,"Color","black")
ylim([4,11])
title("V(r): r'ye göre potansiyelin değişimi")
xlabel('r (m)')
ylabel('V(r) (V)')

subplot(2,1,2);
plot(r,Er,"LineWidth",3,"Color","black")
ylim([-201,201])
title("E(r): r'ye göre elektrik alanın değişimi")
xlabel('r (m)')
ylabel('E(r) (V/m)')


function [Vr,Er] = potansiyelAndField(r,r1,r2,V1,V2)
    % Initialize the output signal
    Vr = zeros(size(r));
    Er = zeros(size(r));


    A = (V1- V2)/((1/r1) - (1/r2));
    B = V1 - A/r1;
    A2 = V2*r2;
    for n = 1:length(r)
        if r(n)>= r1 && r(n)<= r2
            Vr(n) = A/r(n) +B;
            Er(n) = A/r(n)^2;
        elseif r(n)<= r1
            Vr(n) = V1;
            Er(n) = 0;
        elseif r(n)>= r2
            Vr(n) = A2/r(n);
            Er(n) = A2/r(n)^2;
        end
    end
end