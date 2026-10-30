/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o lab2_g5_p1 tb_lab2_g5_p1.sv lab2_g5_p1.sv
vvp lab2_g5_p1

*/
`timescale 1ns/1ns
module sillyfunction(
input logic a,b,c,
output logic y

);
//y = (B'&C') + (A&B')
assign y = (~b & ~c) | (a & ~b);

endmodule