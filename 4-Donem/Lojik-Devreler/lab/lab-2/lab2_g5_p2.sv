/* lab2_g5_p1.sv */
/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o lab2_g5_p2 tb_lab2_g5_p2.sv lab2_g5_p2.sv
vvp lab2_g5_p2

*/
module lab2_g5_p2(
input logic x3,x2,x1,x0,
output logic A,B,C,D,E,F,G

);
/*
    7 segment display elemanının ABCDEFG bölmelerindeki LEDlere bağlı 
7 tane girişi olduğunu ve her bir girişe lojik 1 gönderildiğinde
kendi bölmesini LEDi yakacak şekilde tasarlandığı kabul edilmiştir.
    Bu elemanın aşağıda gösterilen giriş kombinasyonları için belli desenler
veren devre tasarlanacaktır.
    7 segment display elemanının girişlerinin isimleri x3,x2,x1,x0 olarak
kabul edilmiştir.
    7 segment display elemanının A,B,C,D,E,F,G bölmelerindeki LEDlerin
sırasıyla isimleri olarak kabul edilmiştir.
    Gerçeklenecek çıkışlar bu şekildedir.
    Girişler | Çıkış deseni
    0000     |     -
    0010     |     E
    0011     |     3
    0101     |     L
    1100     |     C
    1101     |     2
    1110     |     5
Diğer durumlar önemsiz olarak ele alınabilir.
Çıkış fonksiyonlarının en sade hali bu şekilde bulunmuştur.
A = x3 x2 + x1
B = x3 x0 + x1 x0
C = x1 x0 + x2 x1
D = x3 + x1 + x0
E = x2 x1' + x3' x1 x0'
F = x2 x0' + x3' x2 + x1 x0'
G = x1 + x3 x0 + x3' x2'
bu devre davranışsal olarak tasarlanacaktır.
*/
assign A = x3 & x2 | x1;
assign B = x3 & x0 | x1 & x0;
assign C = x1 & x0 | x2 & x1;
assign D = x3 | x1 | x0;
assign E = x2 & ~x1 | ~x3 & x1 & ~x0;
assign F = x2 & ~x0 | ~x3 & x2 | x1 & ~x0;
assign G = x1 | x3 & x0 | ~x3 & ~x2;


endmodule