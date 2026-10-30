clear all
n_vec = -10:1:10;
for i= 1:length(n_vec)
    xn(i) = xn_func(n_vec(i));
    hn(i) = hn_func(n_vec(i));
end
%% x[n] ve h[n] fonksiyonun konvülayonu 
yn = zeros(1,length(n_vec));
for i= 1:length(n_vec)
    for y = -10000:10000
        yn(i) = yn(i)+ xn_func(y)*hn_func(n_vec(i)-y);
    end
end
%%

subplot(2,3,1)
stem(n_vec , xn)
title("x[n] sinyali")
xlabel("n","FontWeight","bold")
ylabel("x[n]","FontWeight","bold")

subplot(2,3,2)
stem(n_vec , hn)
title("h[n] sinyali")
xlabel("n","FontWeight","bold")
ylabel("h[n]","FontWeight","bold")

subplot(2,3,3)
stem(n_vec , yn)
xlabel('n',"FontWeight","bold");
ylabel('y[n]',"FontWeight","bold");
title('x[n] ve h[n] sinyalinin konvülasyonu');
%%
dt = 0.001;
t_vec = -10:0.01:10;
for i= 1:length(t_vec)
    xt(i) = xt_func(t_vec(i));
    ht(i) = ht_func(t_vec(i));
end
%% x(t) ve h(t) fonksiyonun konvülayonu 
yt = zeros(1,length(t_vec));
for i= 1:length(t_vec)
    for y =-10:dt:10
        yt(i) = yt(i)+ dt*(xt_func(y)*ht_func(t_vec(i)-y));
        %sürekli zamanda integral almak için nümerik integral yöntemi olan...
        %reimann integrali kullanılmıştır. Bundan dolayı dt ile çarpım
        %yapılmıştır. dt yi küçültmek integralin çözünürlüğünü arttırır ve
        %sonuca daha da yakınlaşmamızı sağlar.
        
    end
end


subplot(2,3,4)
plot(t_vec , xt)
title("x(t) sinyali")
xlabel("t","FontWeight","bold")
ylabel("x(t)","FontWeight","bold")

subplot(2,3,5)
plot(t_vec , ht)
title("h(t) sinyali")
xlabel("t","FontWeight","bold")
ylabel("h(t)","FontWeight","bold")

subplot(2,3,6)
plot(t_vec , yt)
xlabel('t',"FontWeight","bold");
ylabel('y(t)',"FontWeight","bold");
title('x(t) ve h(t) fonksiyonun konvülasyonu ');


%%
function [xn] = xn_func(n)
    if n>= 0 && n<= 5
        xn = (1/4)^n;
    else
        xn = 0 ; 
    end
end
function [hn] = hn_func(n)
    if n>= -3 && n<= 2
        hn = (1/2)^n;
    else
        hn = 0 ; 
    end
end
function [xt] = xt_func(t)
    if t>= 0 && t<= 2
        xt =sin(pi*t);
    else
        xt = 0 ; 
    end
end
function [ht] = ht_func(t)
    if t>= -2 && t<= 5
        ht = (1/2);
    else
        ht = 0 ; 
    end
end


