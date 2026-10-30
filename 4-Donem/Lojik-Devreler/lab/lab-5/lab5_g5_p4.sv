`timescale 1ns/1ns
module lab5_g5_p4(
    input logic baslat,clk,reset,
    input logic [4:0] D,
    output logic Y,mesgul
    );
    logic [2:0] state,next_state;
    parameter S0= 3'b000,S1= 3'b001,S2= 3'b010,S3= 3'b011,S4= 3'b100,S5= 3'b101,S6= 3'b110,S7= 3'b111;
    //sencronized reset is used
    always_ff @(clk  )
    begin
        if(reset) state <= S0;
        else state <= next_state;
    end
    always_ff @(posedge clk ) begin
        case(state)         //baslat= 1 : baslat = 0
            S0 : begin
                
                next_state <= baslat ? S1 : S0;
                Y <= 1'b1 ;
                mesgul = 1'b0;
            end
            S1 : begin
                
                next_state <=  S2 ;
                Y <= 1'b0;
                mesgul = 1'b1;
            end
            
            S2: begin 
                    
                    next_state <=S3 ;
                    Y <= D[0] ;
                    mesgul = 1'b1;
                end
            S3: begin 
                    
                    next_state <=  S4;
                    Y <= D[1] ;
                    mesgul = 1'b1;
                end
            S4: begin 
                    
                    next_state <=  S5;
                    Y <= D[2] ;
                    mesgul = 1'b1;
                end
            S5: begin 
                    
                    next_state <=   S6;
                    Y <= D[3] ;
                    mesgul = 1'b1;
                end
            S6: begin 
                    
                    next_state <=S7 ;
                    Y <= D[4] ;
                    mesgul = 1'b1;
                end
            S7: begin 
                    
                    next_state <=  S0 ;
                    Y <= 1'b1 ;
                    mesgul = 1'b0;
                end
            
            
            default: next_state = S0;
        endcase
        
    end
    
endmodule
