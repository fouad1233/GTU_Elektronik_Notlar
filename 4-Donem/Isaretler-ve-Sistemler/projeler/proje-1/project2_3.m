clear all
t = -10:0.001:10;
%%
for i= 1:length(t)
    xt(i) = xt_func(t(i));
    xminust(i) = xt_func(-t(i));
end
subplot (4,3,1);
plot(t,xt)
title("x(t) sinyali")
xlabel("t","FontWeight","bold")
ylabel("x(t)","FontWeight","bold")
ylim([-2 2])% y ekseninin -2 , 2 arasını göstermesini sağlar
xlim([-2 5])% x ekseninin -2 , 5 arasını göstermesini sağlar

subplot (4,3,2);
xt_even = (1/2).*(xt+xminust);% 1/2(f(x) + f(-x))
plot(t,xt_even)
title("x(t) sinyalinin çift kısmı")
xlabel("t","FontWeight","bold")
ylabel("x(t) çift","FontWeight","bold")
ylim([-2 2])% y ekseninin -2 , 2 arasını göstermesini sağlar
xlim([-2 5])% x ekseninin -2 , 5 arasını göstermesini sağlar

subplot (4,3,3);
xt_odd = (1/2).*(xt-xminust);% 1/2(f(x) - f(-x))
plot(t,xt_odd)
title("x(t) sinyalinin tek kısmı")
xlabel("t","FontWeight","bold")
ylabel("x(t) tek","FontWeight","bold")
ylim([-2 2])% y ekseninin -2 , 2 arasını göstermesini sağlar
xlim([-2 5])% x ekseninin -2 , 5 arasını göstermesini sağlar

%%
for i= 1:length(t)
    xt_a(i) = xt_func(2*t(i));
    xminust_a(i) = xt_func(-2*t(i));
end

subplot (4,3,4);
plot(t,xt_a)
title("x(2t) sinyali")
xlabel("t","FontWeight","bold")
ylabel("x(2t)","FontWeight","bold")
ylim([-2 2])% y ekseninin -2 , 2 arasını göstermesini sağlar
xlim([-2 5])% x ekseninin -2 , 5 arasını göstermesini sağlar

subplot (4,3,5);
xt_even_a = (1/2).*(xt_a+xminust_a);% 1/2(f(x) + f(-x))
plot(t,xt_even_a)
title("x(2t) sinyalinin çift kısmı")
xlabel("t","FontWeight","bold")
ylabel("x(2t) çift","FontWeight","bold")
ylim([-2 2])% y ekseninin -2 , 2 arasını göstermesini sağlar
xlim([-2 5])% x ekseninin -2 , 5 arasını göstermesini sağlar

subplot (4,3,6);
xt_odd_a = (1/2).*(xt_a-xminust_a);% 1/2(f(x) - f(-x))
plot(t,xt_odd_a)
title("x(2t) sinyalinin tek kısmı")
xlabel("t","FontWeight","bold")
ylabel("x(2t) tek","FontWeight","bold")
ylim([-2 2])% y ekseninin -2 , 2 arasını göstermesini sağlar
xlim([-2 5])% x ekseninin -2 , 5 arasını göstermesini sağlar
check_a = all(xt_even_a + xt_odd_a == xt_a);% çift ve tek kısmın
% toplamının fonksiyonun kendisini verip vermediğini kontrol eder

%%
for i= 1:length(t)
    xt_b(i) = xt_func(t(i)-5/2);
    xminust_b(i) = xt_func(-(t(i)-5/2));
end
subplot (4,3,7);
plot(t,xt_b)
title("x(t-(5/2)) sinyali")
xlabel("t","FontWeight","bold")
ylabel("x(t-(5/2))","FontWeight","bold")
ylim([-2 2])% y ekseninin -2 , 2 arasını göstermesini sağlar
xlim([-2 5])% x ekseninin -2 , 5 arasını göstermesini sağlar

subplot (4,3,8);
xt_even_b = (1/2).*(xt_b+xminust_b);% 1/2(f(x) + f(-x))
plot(t,xt_even_b)
title("x(t-(5/2) sinyalinin çift kısmı")
xlabel("t","FontWeight","bold")
ylabel("x(t-(5/2) çift","FontWeight","bold")
ylim([-2 2])% y ekseninin -2 , 2 arasını göstermesini sağlar
xlim([-2 5])% x ekseninin -2 , 5 arasını göstermesini sağlar

subplot (4,3,9);
xt_odd_b = (1/2).*(xt_b-xminust_b);% 1/2(f(x) - f(-x))
plot(t,xt_odd_b)
title("x(t-(5/2) sinyalinin tek kısmı")
xlabel("t","FontWeight","bold")
ylabel("x(t-(5/2) tek","FontWeight","bold")
ylim([-2 2])% y ekseninin -2 , 2 arasını göstermesini sağlar
xlim([-2 5])% x ekseninin -2 , 5 arasını göstermesini sağlar
check_b = all(xt_even_b + xt_odd_b == xt_b);

%%
for i= 1:length(t)
    xt_c(i) = xt_func(-2*t(i)+5);
    xminust_c(i) = xt_func(-(-2*t(i)+5));
end
subplot (4,3,10);
plot(t,xt_c)
title("x(-2t+5) sinyali")
xlabel("t","FontWeight","bold")
ylabel("x(-2t+5)","FontWeight","bold")
ylim([-2 2])
xlim([-2 5])

subplot (4,3,11);
xt_even_c = (1/2).*(xt_c+xminust_c);% 1/2(f(x) + f(-x))
plot(t,xt_even_c)
title("x(-2t+5) sinyalinin çift kısmı")
xlabel("t","FontWeight","bold")
ylabel("x(-2t+5) çift","FontWeight","bold")
ylim([-2 2])
xlim([-2 5])

subplot (4,3,12);
xt_odd_c = (1/2).*(xt_c-xminust_c);% 1/2(f(x) - f(-x))
plot(t,xt_odd_c)
title("x(-2t+5) sinyalinin tek kısmı")
xlabel("t","FontWeight","bold")
ylabel("x(-2t+5) tek","FontWeight","bold")
ylim([-2 2])
xlim([-2 5])

check_c = all(xt_even_c + xt_odd_c == xt_c);
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


