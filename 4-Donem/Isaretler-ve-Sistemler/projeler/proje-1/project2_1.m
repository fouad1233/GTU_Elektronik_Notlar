%%𝑥[𝑛] = 𝑒^^−(0.05+𝑗0.3)𝑛
% İşareti örneklemek için n vektörü tanımlayalım
n = -30:1:30;
xn = exp(-(0.05+0.3*1i)*n);%xn fonkisyonun n örnekleri için çıktısı
%%sinyali imaginer ve real kısımlarını ayarlayalım ve çizime hazırlayalım
a=real(xn);% sinaylin real kısmını a olarak ayıralım
b=imag(xn);% sinyalin sanal kısmını b olarak ayıralım
subplot (4,2,1);
stem(n,a,'filled');%ayrık olarak çiziminin gerçekleşebilmesi stem fonksiyonu kullanıldı
title("x[n] sinyalinin real kısmı")% grafiğe ad vermek için bu komut kullanılır
xlabel("n","FontWeight","bold")% x ekseninin adlandırlıması
ylabel("real(x[n])","FontWeight","bold")% y ekseninin adlandırılmasıd
subplot (4,2,2);
stem(n,b,'filled');
title("x[n] sinyalinin sanal kısmı")
xlabel("n","FontWeight","bold")
ylabel("imag(x[n])","FontWeight","bold")
%%Genliği hesaplaylım
amplitude = abs(xn);%%sqrt((a).^2 + (b).^2);
subplot (4,2,3);
stem(n,amplitude);
title("x[n] sinyalinin Genlik kısmı")
xlabel("n","FontWeight","bold")
ylabel("|x[n]|","FontWeight","bold")
%%fazı açılarını çizdirelim
phase = angle(xn);%angle fonksiyonu açıyı radyan cinsinden döndürür
subplot (4,2,4);
stem(n,phase);
title("x[n] sinyalinin faz kısmı")
xlabel("n","FontWeight","bold")
ylabel("x[n] faz kısmı","FontWeight","bold")
%%
%%𝑥(t) = 𝑒^−(0.05+𝑗0.3)t
% İşareti örneklemek için t vektörü tanımlayalım ve vektör sürekli zamana
% benzemesi için örneklemesini sıklaştıralım
t = -30:0.001:30;
xt = exp(-(0.05+0.3*1i)*t);%xt fonkisyonun t örnekleri için çıktısı
%%sinyali imaginer ve real kısımlarını ayarlayalım ve çizime hazırlayalım
at=real(xt);% sinaylin real kısmını at olarak ayıralım
bt=imag(xt);
subplot (4,2,5);
plot(t,at);%sürekli olarak çiziminin gerçekleşebilmesi plot fonksiyonu kullanıldı
title("x(t) sinyalinin real kısmı")
xlabel("t","FontWeight","bold")
ylabel("real(x(t))","FontWeight","bold")
subplot (4,2,6);
plot(t,bt);
title("x(t) sinyalinin sanal kısmı")
xlabel("t","FontWeight","bold")
ylabel("imag(x(t))","FontWeight","bold")
%%Genliği hesaplaylım
amplitude_t = abs(xt);%%sqrt((a).^2 + (b).^2);
subplot (4,2,7);
plot(t,amplitude_t);
title("x(t) sinyalinin Genlik kısmı")
xlabel("t","FontWeight","bold")
ylabel("|x(t)|","FontWeight","bold")
%%fazı açılarını çizdirelim
phase_t = angle(xt);
subplot (4,2,8);
plot(t,phase_t);
title("x(t) sinyalinin faz kısmı")
xlabel("t","FontWeight","bold")
ylabel("x(t) faz kısmı","FontWeight","bold")


