`timescale 1ns/1ns
module lab3_g5_p5(
    input logic A,B,C,D,
    output logic F1,F2
    );
    //F1 is the sum of minterms 1,3,7,11,12,13,15
    MUX16x1 mux1(16'b1011_1000_1000_1010, {A,B,C,D}, F1);
    MUX16x1 mux2(16'b1111_1111_0100_0011, {A,B,C,D}, F2);
    
endmodule

module MUX16x1(input logic [15:0] A , input logic [3:0] S, output logic Y);
    //A[0] = A; A[1] = A; A[2] = A; A[3] = A; A[4] = A; A[5] = A; A[6] = A; A[7] = A; A[8] = A; A[9] = A; A[10] = A; A[11] = A; A[12] = A; A[13] = A; A[14] = A; A[15] = A; S = S; 
    logic [15:0] Aarray;
    logic y1, y2;
    MUX8x1 mux1(A[7:0], S[2:0], y2);
    MUX8x1 mux2(A[15:8], S[2:0], y1);
    lab3_g5_p1 mux3({y1,y2}, S[3], Y);
endmodule
module MUX8x1(input logic [7:0] A , input logic [2:0] S, output logic Y);
    //A[0] = A; A[1] = A; A[2] = A; A[3] = A; A[4] = A; A[5] = A; A[6] = A; A[7] = A; S = S; 
    logic [7:0] Aarray;
    logic y1, y2;
    MUX4x1 mux1(A[3:0], S[1:0], y2);
    MUX4x1 mux2(A[7:4], S[1:0], y1);
    lab3_g5_p1 mux3({y1,y2}, S[2], Y);
endmodule
module MUX4x1(input logic [3:0] A, input logic [1:0] S, output logic Y);
    //A[0] = A; A[1] = A; A[2] = A; A[3] = A; S = S; 
    logic [3:0] Aarray;
    logic y1, y2;
    lab3_g5_p1 mux1(A[1:0], S[0], y2);
    lab3_g5_p1 mux2(A[3:2], S[0], y1);
    lab3_g5_p1 mux3({y1,y2}, S[1], Y);
endmodule

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

