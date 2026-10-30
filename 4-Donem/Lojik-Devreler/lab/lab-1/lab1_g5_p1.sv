/* lab1_g5_p1.sv */

module lab1_g5_p1(
input logic G,T,U,E,
output logic Y

);
assign Y = (~G & T & ~U & E) | ( G & T & U & E ) | ( G & ~T & ~U & E ) | ( G & T & ~U & E ) | ( ~G & T & U & E ) | ( ~G & ~T & U & E ) | ( G & T & U & ~E);
endmodule