Vcc = 24;
Vc = 16 ;

Ic = 0.25*10^-3;
Rc = 8/Ic;
fprintf("Rc= %f\n",Rc)
beta  = 200;
Ie = ((beta + 1)/beta)* Ic;
fprintf("Ie= %f\n",Ie)
Ib = Ic/beta;
R1 = 600000;
Vb = Vcc - ((Ic*R1)/10);
fprintf("Vb= %f\n",Vb)
old_vbe_ic = [8.74599-8.12896,0.00024253];

Vt = 0.025;
Is = Ic/(exp(old_vbe_ic(1)/Vt));
for i = 1:100
    Vbe = old_vbe_ic(1) +Vt*log( Ic/ old_vbe_ic(2));
    old_vbe_ic(2) = Ic;
    old_vbe_ic(1) = Vbe;
    Ic = Is * exp(old_vbe_ic(1) /Vt);
    
    
end
Ve = Vb - Vbe;
fprintf("Ve= %f\n",Ve)
Re = Ve/Ie;
fprintf("Re= %f\n",Re)
R2 = (R1*Vb / (Vcc-Vb));
fprintf("R2= %f\n",R2)
Vce = (Vc - Ve);
fprintf("Vce= %f\n",Vce)






