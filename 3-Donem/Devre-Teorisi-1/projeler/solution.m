i = linspace(-6,10,10000) ;
Rth = -5/8;
v = (-Rth * i) - 5; 
plot( i,v)
R1 =  2;
R2 =  2;
d = (((R1* R2)/Rth) - (R1 + R2))/R2;
Isc = 8;
Voc = -5;
Vs = (Isc * R1)/(d+1) ;

ia = (i + (v/R2))/(1+d);
hold on;
plot(i , ia)
axh = gca; % use current axes
color = 'k'; % black, or [0 0 0]
linestyle = ':'; % dotted
line(get(axh,'XLim'), [0 0], 'Color', color, 'LineStyle', linestyle);
line([0 0], get(axh,'YLim'), 'Color', color, 'LineStyle', linestyle);
