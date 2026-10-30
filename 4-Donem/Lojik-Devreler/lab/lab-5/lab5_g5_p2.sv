`timescale 1ns/1ns
module lab5_g5_p2(
    
    input  logic clk, reset, en,
    input  logic [ 4:0] psc,
    input  logic [15:0] reload,
    output logic [15:0] cnt,
    output logic bitti
    );
    
    logic tick;
    lab5_g5_p1 impulse(.clk(clk), .reset(reset),.en(en), .psc(psc), .tick(tick));
    
    //with sencron active low reset
    always_ff @(posedge clk ) begin
        if (!reset) begin
            //cnt <= 16'b0;
            cnt <= reload;
            
        end 
        else begin
                if (en) begin
                    if (cnt == 0) begin
                        cnt <= reload;
                        bitti <= 1'b1;
                    end 
                    else if (cnt!= 0 && tick)begin
                        cnt <= cnt - 1;
                        bitti <= 1'b0;
                    end
                    else begin
                        bitti <= 1'b0;
                    end 
                end
                else begin
                    cnt <= reload;
                end
            end
    end
endmodule

module lab5_g5_p1(
    
    input logic clk, reset, en,
    input logic [4:0] psc,
    output logic tick
    );
    
    logic [4:0] count;
    
    //with sencron active low reset
    always @(posedge clk ) begin
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

