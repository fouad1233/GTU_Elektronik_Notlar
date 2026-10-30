Vm = 5;
Vs = Vm;
f = 2500  ;
w = 2.*pi.*f;
ZR2 = 500;%500 ohm
L1 = 33.* 10.^-3; %%33mH
ZL1 = 1i.*w.*L1;
Zload = ZR2 + ZL1;
ZR1 = 10 ;%10 ohm iç direnç
[Zloadabs, Zloadangle] = rectangulartopolar(Zload);
fprintf('Zload %.4f+%.4fi,Zload abs: %.4f ,Zload angle:%.4f \n',real(Zload),imag(Zload), Zloadabs,Zloadangle ); 
Zeq = Zload + ZR1;
[Zeqabs, Zeqangle] = rectangulartopolar(Zeq);
fprintf('Zeq %.4f+%.4fi,Zeq abs: %.4f ,Zeq angle:%.4f \n',real(Zeq),imag(Zeq), Zeq,Zeqangle ); 

IsA = (Vs ./ Zeq);%A
Is = (Vs ./ Zeq)*1000;%ma
[Isabs, Isangle] = rectangulartopolar(Is);
fprintf('Is %.4f%.4fi,Is abs: %.4f ,Is angle:%.4f \n',real(Is),imag(Is), Isabs,Isangle ); 

Svector = Vs.*conj(Is) ./2;
P = real(Svector);
Q = imag(Svector);
Sapperent = abs(Svector);
pf = P./Svector;
fprintf('Svector %.4f+%.4fi,P: %.4f ,Q:%.4f ,Sapperent:%.4f, pf: %.4f\n',P,Q , P,Q,Sapperent,pf ); 
%%
fprintf('\n\nFor C1,C2,C3:\n')

ZR2 = 500;%500 ohm
L1 = 33.* 10.^-3; %%33mH
ZL1 = 1i.*w.*L1;
Zload = ZR2 + ZL1;
ZR1 = 10 ;%10 ohm iç direnç
C1 = [2.2,22,47] .* 10^-9;
ZC1 = 1 ./(1i .* w.* C1);
ZloadC1 = (Zload.* ZC1) ./ (Zload+ ZC1)
[ZloadC1abs, ZloadC1angle] = rectangulartopolar(ZloadC1)
Zeq = ZloadC1 + ZR1
[Zeqabs, Zeqangle] = rectangulartopolar(Zeq)

IsA = (Vs ./ Zeq);%A
Is = (Vs ./ Zeq)*1000%ma
[Isabs, Isangle] = rectangulartopolar(Is)

Svector = Vs.*conj(Is) ./2
P = real(Svector)
Q = imag(Svector)
Sapperent = abs(Svector)
pf = P./Sapperent
