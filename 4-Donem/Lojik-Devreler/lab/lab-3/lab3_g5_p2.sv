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
module NOR_MUX(input logic A,B, output logic Y);
    //A[0] = A; A[1] = A; S = B; 
    logic [1:0] Aarray;
    NOT_MUX not1(A, Anot);
    always_comb begin
        Aarray[0] = Anot;
        Aarray[1] = 0;
    end
    lab3_g5_p1 mux(Aarray, B, Y);
endmodule
module NAND_MUX(input logic A,B, output logic Y);
    //A[0] = A'; A[1] = 1; S = B; 
    logic Anot;
    logic [1:0] Aarray;
    NOT_MUX not1(A, Anot);
    always_comb begin
        Aarray[0] = 1;
        Aarray[1] = Anot;
    end
    lab3_g5_p1 mux(Aarray, B, Y);
endmodule
module NOT_MUX(input logic A, output logic Y);
    //A[0] = A; A[1] = A; S = B; 
    logic [1:0] Aarray;
    always_comb begin
        Aarray[0] = 1;
        Aarray[1] = 0;
    end
    lab3_g5_p1 mux(Aarray, A, Y);
endmodule
module AND_MUX(input logic A,B, output logic Y);
    //A[0] = 0; A[1] = A; S = B; 
    logic [1:0] Aarray;
    always_comb begin
        Aarray[0] = 0;
        Aarray[1] = A;
    end
    lab3_g5_p1 mux(Aarray, B, Y);
endmodule
module OR_MUX(input logic A,B, output logic Y);
    //A[0] = A; A[1] = 1; S = B; 
    logic [1:0] Aarray;
    always_comb begin
        Aarray[0] = A;
        Aarray[1] = 1;
    end
    lab3_g5_p1 lab3_g5_p1(Aarray, B, Y);
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