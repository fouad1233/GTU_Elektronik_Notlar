//hw3_p2_moore.sv
`timescale 1ns/1ns
module hm3_p2_moore(
    //bit array detector that detecet 01001
    input logic clk,
    input logic reset,
    input logic A,
    output  logic B
    );
    logic [2:0] state,next_state;
    parameter S0 = 3'b000,S1 = 3'b001,S2 = 3'b010,S3 = 3'b011,S4 = 3'b100,S5 = 3'b101;
    //sencronized reset is used
    always_ff @(posedge clk )
    begin
        if(reset) state <= S0;
        else state <= next_state;
    end
    //Next state as function of current state and input

    always_comb  begin
        case(state)          //A= 1 : A = 0
            S0: next_state = A ? S0 : S1;
            S1: next_state = A ? S2 : S1;
            S2: next_state = A ? S0 : S3;
            S3: next_state = A ? S2 : S4;
            S4: next_state = A ? S5 : S1;
            S5: next_state = A ? S0 : S1;
            default: next_state = S0;
        endcase
        
    end
    always_comb  begin
        //output as function of current state
            case(state)
                S5: B = 1'b1;
                default: B = 1'b0;
            endcase
    end
    
endmodule