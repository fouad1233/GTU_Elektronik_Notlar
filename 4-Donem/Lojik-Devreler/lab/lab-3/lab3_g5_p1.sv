`timescale 1ns/1ns
module lab3_g5_p1(
    //this is a 2x1 MUX
    input logic [1:0] A,
    input  logic S,
    output logic Y
    );
    // Y = ((S nand 1) nand A[0]) nand (S nand A[1])
    
    logic nand1, nand2, nand3;
    NAND n1(S, 1'b1, nand1);
    NAND n2(nand1, A[0], nand2);
    NAND n3(S, A[1], nand3);
    NAND n4(nand2, nand3, Y);
    //assign nand1 = ~(S & 1'b1);
    //assign nand2 = ~(nand1 & A[0]);
    //assign nand3 = ~(S & A[1]);
    //assign Y = ~(nand2 & nand3);

endmodule
module NAND(a, b, y);

input logic a, b;
output logic y;

    assign y = ~(a & b);
endmodule
