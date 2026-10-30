/* lab2_g5_p1.sv */
/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o lab2_g5_p1 tb_lab2_g5_p1.sv lab2_g5_p1.sv
vvp lab2_g5_p1

*/
`timescale 1ns/1ns
module lab2_g5_p1(
input logic A,B,C,D,
output logic Y,X

);
// Y = AB' C +C' D
/* İlk terimi B' AC olarak ele alınsın. İlk önce B nın değili alınmalıdır buna
n1 denilsin -> n1 = B' olacak. Sonra A ve C nin AND i alınacak buna da n2 denilecek.
ve Y nın ilk terimini oluşturmak için n1 ve n2 nin AND i alınacak. Bu işlem
y1 = n1 n2 şeklinde gösterilebilir.
İkinci terim C' D olarak ele alınsın. İlk önce C nin değili alınmalıdır buna n3 denilsin.
sonrasında ise D ile AND i alınmalıdır. Bu işlem y2 = n3 D şeklinde gösterilebilir.
Son olarak y1 ve y2 nin OR u alınarak Y nin değeri bulunur. Y = y1 + y2.
Her işlem sırasında 2ns gecikme koyulacaktır.
*/
assign #2 n1 = ~B;
assign #2 n2 = A & C;
assign #2 y1 = n1 & n2;
assign #2 n3 = ~C;
assign #2 y2 = n3 & D;
assign #2 Y = y1 | y2;
// X = AB' C +C' D+ AB' D
/*
Bu fonksiyon Glitch sıkıntısı gidermek amacıyla kullanılmıştır.
Y fonksiyomnuna ek olarak X fonksiyonu da tanımlanmıştır.
X fonksiyonu Y fonksiyonuna ek olarak AB' D terimini de içermektedir.
Bu terim y3 olarak adlandırılacaktır.
n4 = AD olacak şekilde tanımlanırsa y3 = n1 n4 şeklinde gösterilebilir.
yine burdaki her yeni kapı için 2ns gecikme koyulacaktır.
ve X = y1 + y2 + y3 şeklinde gösterilebilir.
*/
assign #2 n4 = A & D;
assign #2 y3 = n1 & n4;
assign #2 x2 = y2 | y3;
assign #2 X = x2 | y1;

endmodule