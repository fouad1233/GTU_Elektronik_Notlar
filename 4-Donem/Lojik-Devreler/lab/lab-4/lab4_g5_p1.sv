`timescale 1ns/1ns
module DFlipFlopRisingEdge(
    //yukselen kenar duzeyinde calisan D flip flop
    input logic clk,
    input logic rst,
    input logic d,
    output  logic q
    );
    //sencronized reset is used
    always @(posedge clk )
    begin
        if(rst)
            q <= 1'b0;
        else
            q <= d;
    end
endmodule
module DFlipFlopFallingEdge(
    //dusen kenar duzeyinde calisan D flip flop
    input logic clk,
    input logic rst,
    input logic d,
    output  logic q
    );
    //sencronized reset is used
    always @(negedge clk )
    begin
        if(rst)
            q <= 1'b0;
        else
            q <= d;
    end
endmodule
module latch(  input logic clk,            
                input logic d,           
                output logic q);      
  
   
    always_latch begin
        if (clk)  
        q <= d;
        end
      
endmodule  