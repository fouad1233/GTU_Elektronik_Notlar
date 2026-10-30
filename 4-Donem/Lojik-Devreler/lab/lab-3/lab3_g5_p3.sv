`timescale 1ns/1ns
module lab3_g5_p3(
    //this is a 2x4 decoder
    input logic [1:0] A,
    input logic E,
    output logic [3:0] D
    );
    /*
    A1not = A[1] nand A[1]
    A0not = A[0] nand A[0]
    D[0] = (A1not nand A0not) nand (A1not nand A0not)
    D[1] = (A1not nand A0) nand (A1not nand A0)
    D[2] = (A1 nand A0not) nand (A1 nand A0not)
    D[3] = (A1 nand A0) nand (A1 nand A0)
    */
    logic A1not, A0not , D0_not, D1_not, D2_not, D3_not;
    logic [3:0] buffer;
    NAND A1not_nand(A[1], A[1], A1not);
    NAND A0not_nand(A[0], A[0], A0not);
    NAND D0_not_nand(A1not, A0not, D0_not);
    NAND D1_not_nand(A1not, A[0], D1_not);
    NAND D2_not_nand(A[1], A0not, D2_not);
    NAND D3_not_nand(A[1], A[0], D3_not);
    NAND D0_nand(D0_not, D0_not, buffer[0]);
    NAND D1_nand(D1_not, D1_not, buffer[1]);
    NAND D2_nand(D2_not, D2_not, buffer[2]);
    NAND D3_nand(D3_not, D3_not, buffer[3]);
    assign D = E ? buffer : 4'b0000;
        
    
endmodule
module NAND(a, b, y);

input logic a, b;
output logic y;

    assign y = ~(a & b);
endmodule
