`timescale 1ns/1ns
module lab5_g5_p3(
    input logic A,clk,reset,
    output logic Y
    );
    logic [3:0] state,next_state;
    parameter S0= 4'b0000, S1= 4'b0001, S2= 4'b0010, S3= 4'b0011, S4= 4'b0100, S5= 4'b0101, S6= 4'b0110, S7= 4'b0111, S8= 4'b1000;
    //sencronized reset is used
    always_ff @(posedge clk )
    begin
        if(reset) state <= S0;
        else state <= next_state;
    end
    //Next state as function of current state and inputs
    always_comb  begin
        case(state)          //A= 1 : A = 0
            S0: next_state = A ? S5 : S1;
            S1: next_state = A ? S5 : S2;
            S2: next_state = A ? S5 : S3;
            S3: next_state = A ? S5 : S4;
            S4: next_state = A ? S5 : S4;
            S5: next_state = A ? S6 : S1;
            S6: next_state = A ? S7 : S1;
            S7: next_state = A ? S8 : S1;
            S8: next_state = A ? S8 : S1;
            default: next_state = S0;
        endcase
        
    end
    always_comb  begin
        //output as function of current state
            case(state)
                               //A= 1 : A = 0
                S0: Y = A ? 0 : 0;
                S1: Y = A ? 0 : 0;
                S2: Y = A ? 0 : 0;
                S3: Y = A ? 0 : 0;
                S4: Y = A ? 0 : 1;
                S5: Y = A ? 0 : 1;
                S6: Y = A ? 0 : 0;
                S7: Y = A ? 1 : 0;
                S8: Y = A ? 1 : 0;
                default: Y = 0;
            endcase
    end
endmodule
