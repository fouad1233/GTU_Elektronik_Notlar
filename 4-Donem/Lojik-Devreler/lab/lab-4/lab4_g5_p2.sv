`timescale 1ns/1ns
module halfadder(
    
    input logic A,B,
    output  logic Y, Cout
    );
    assign Y = A ^ B;
    assign Cout = A & B;

    
endmodule
module fulladder(
    //full adder
    input logic A,B,Cin,
    output  logic Y, Cout
    );
    logic Y1, Cout1,Cout2;
    halfadder HA1(A,B,Y1,Cout1);
    halfadder HA2(Cin,Y1,Y,Cout2);
    assign Cout = Cout1 | Cout2;
    
endmodule
module RippleCarryAdder(
    input logic [4:0] A,B,
    output logic [4:0] Y,
    output logic Cout
    );
    logic [4:0] Y1;
    logic Cout1,Cout2,Cout3,Cout4;
    fulladder FA1(A[0],B[0],1'b0,Y[0],Cout1);
    fulladder FA2(A[1],B[1],Cout1,Y[1],Cout2);
    fulladder FA3(A[2],B[2],Cout2,Y[2],Cout3);
    fulladder FA4(A[3],B[3],Cout3,Y[3],Cout4);
    fulladder FA5(A[4],B[4],Cout4,Y[4],Cout);

endmodule