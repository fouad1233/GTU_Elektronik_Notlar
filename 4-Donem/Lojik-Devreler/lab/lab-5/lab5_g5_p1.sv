`timescale 1ns/1ns
module lab5_g5_p1(
    
    input logic clk, reset, en,
    input logic [4:0] psc,
    output logic tick
    );
    
    logic [4:0] count;
    
    //with sencron active low reset
    always_ff @(posedge clk ) begin
        if (!reset) begin
            count <= 5'b0;
            tick <= 1'b0;
        end 
        else begin
            if (en ) begin
                if (count == psc) begin
                    count <= 5'b0;
                    tick <= 1'b1;
                end 
                else begin
                    count <= count + 1;
                    tick <= 1'b0;
                end
            end 
            else begin
                tick <= 1'b0;
            end
            end
    end
endmodule
