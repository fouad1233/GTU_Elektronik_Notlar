In1 = [12-20i, 20i,0;
       20i, -18.5i, -3i;
       0, -3i, 6i+5];
O1 = [100;0;0];
Currents1 = In1\O1;
In2 = [12-20i, 20i,0;
       20i, -18.5i, -3i;
       0, -3i, 5-16i];
O2 = [100;0;0];
Currents2 = In2\O2;
I3 =  -1.41 + 0.76i;
Vab = I3* (-20i);
Isc = 2.53+1.77i;
Zth = Vab/Isc;
I = Vab/(Zth + conj(Zth));
Complex_power = (Vab/2)* conj(I);
%%
Zy1 = (-100i)/3;
Zy = 100i;
Zes = (Zy * Zy1)/(Zy + Zy1);
Ia = 220
