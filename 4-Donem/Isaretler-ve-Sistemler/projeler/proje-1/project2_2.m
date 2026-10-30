clear all
t = -10:0.001:10;%zamanı temsil etmesi için t vektörü oluşturuldu
%%
for i= 1:length(t)
    xt(i) = xt_func(t(i));%xt fonksiyonun t vektörü için çıttıları elde edildi
end
subplot (4,1,1);
plot(t,xt)%fonksiyon çizdirildi
title("x(t) sinyali")
xlabel("t","FontWeight","bold")
ylabel("x(t)","FontWeight","bold")
ylim([-2 2])% y ekseninin -2 , 2 arasını göstermesini sağlar
xlim([-2 5])% x ekseninin -2 , 5 arasını göstermesini sağlar

%%
for i= 1:length(t)
    xt_a(i) = xt_func(2*t(i));%a şıkkındaki fonksiyonu ...
    % elde etmek için t(i) 2 ile çarpılmıştır, böylece x(2t) yi temsil
    % etmiştir.
end

subplot (4,1,2);
plot(t,xt_a)
title("x(2t) sinyali")
xlabel("t","FontWeight","bold")
ylabel("x(2t)","FontWeight","bold")
ylim([-2 2])
xlim([-2 5])

%%
for i= 1:length(t)
    xt_b(i) = xt_func(t(i)-5/2);%b şıkkındaki fonksiyonu ...
    % elde etmek için t(i) den 5/2 çıkarılmıştır ile çarpılmıştır,
    % böylece x(2t - (5/2)) yi temsil etmiştir.
    
end
subplot (4,1,3);
plot(t,xt_b)
title("x(t-(5/2)) sinyali")
xlabel("t","FontWeight","bold")
ylabel("x(t-(5/2))","FontWeight","bold")
ylim([-2 2])
xlim([-2 5])

%%
for i= 1:length(t)
    xt_c(i) = xt_func(-2*t(i)+5);%burda ise eksi iki ile çarpıldı ve 5 eklendi
end
subplot (4,1,4);
plot(t,xt_c)
title("x(-2t+5) sinyali")
xlabel("t","FontWeight","bold")
ylabel("x(-2t+5)","FontWeight","bold")
ylim([-2 2])
xlim([-2 5])% x ekseninin -8 , -1 arasını göstermesini sağlar
%%
function xt = xt_func(t)
    if (t >= -1) && (t < 0)%xt fonksiyonu -1<=t<0 iken 1+t değeri alır
        xt = 1 + t;
    elseif (t >= 0) && (t < 2)%xt fonksiyonu 0<=t<2 iken 1 değeri alır
        xt = 1;
    else
        xt = 0;% farklı durumlarda ise 0 değerini alır
    end
end

%%
% function [xt] = xt_func(scale,t,delay)
%     
%     if ((t*scale)+delay>-1) && ((t*scale)+delay<0)
%         xt = 1+(t*scale+delay);
%     elseif ((t*scale)+delay>=0) && ((t*scale)+delay<2)
%         xt = 1;
%     else
%         xt = 0;
% 
%     end
% end
