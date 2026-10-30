`timescale 1ns/1ns
module lab4_g5_p3(
    input  logic [31:0] A, B,
    input  logic [ 3:0] op,
    output logic [31:0] Y,
    output logic n, z, v, c,
    output logic error
);
    logic signed [31:0] signed_A, signed_B;
    assign signed_A = A;
    assign signed_B = B;
    always @(A,B,op)
        begin
            case(op)
                4'b0000: begin // Addition
                    
                    {c , Y} = A + B ; 
                    n = Y[31];
                    v = (A[31] == B[31]) && (A[31] != Y[31]);//overflow : same sign in input and different sign in output
                    z = (Y == 0);
                    error = 0;
                end
                4'b1000: begin// Subtraction
                    {c,Y} = A - B ;
                    n = Y[31];
                    v = (A[31] == B[31]) && (A[31] != Y[31]);//overflow : same sign in input and different sign in output
                    z = (Y == 0);
                    error = 0;
                end
                4'b0001: begin// Logical shift left
                    c = 0 ;
                    Y = A<<B[4:0] ;
                    c = (A != Y>>B[4:0]);
                    /*
                    // Perform bitwise OR on all bits
                    
                    for (integer  i = 0; i < B; i = i + 1) begin
                        c = c | A[31-i];
                    end
                    */
                    {v , n, z} = {1'bx, 1'bx, 1'bx};
                    error = 0;
                end 
                4'b0010: begin // s comparison
                    Y = signed_A > signed_B ;
                    
                    {v , n, z,c} = {1'bx, 1'bx, 1'bx,1'bx};
                    error = 0;
                end 
                4'b0011: begin // u comparison
                    Y = A > B ; 
                    {v , n, z,c} = {1'bx, 1'bx, 1'bx,1'bx};
                    error = 0;
                end    
                4'b0100: begin //xor
                    Y = A ^ B ;
                    {v , n, z,c} = {1'bx, 1'bx, 1'bx,1'bx};
                    error = 0;
                end
                4'b0101: begin // Logical shift right
                    c = 0 ;
                    Y = A>>B[4:0] ;
                    c = (A != Y<<B[4:0]);
                    /*
                    // Perform bitwise OR on all bits
                    c = 0 ;
                    for (integer  i = 0; i < B; i = i + 1) begin
                        c = c | A[i];
                    end
                    */
                    {v , n, z} = {1'bx, 1'bx, 1'bx};
                    error = 0;
                end
                4'b1101: begin // Arithmetic shift right
                    c = 0 ;
                    Y = signed_A>>>signed_B[4:0] ;
                    // Perform bitwise OR on all bits
                    
                    c = (A != Y<<B[4:0]);
                    /*
                    for (integer  i = 0; i < B; i = i + 1) begin
                        c = c | A[i];
                    end
                    */
                    {v , n, z} = {1'bx, 1'bx, 1'bx};
                    error = 0;
                end
                4'b0110: begin // or
                    Y = A | B ;
                    {v , n, z,c} = {1'bx, 1'bx, 1'bx,1'bx};
                    error = 0;
                end
                4'b0111: begin // and
                    Y = A & B ;
                    {v , n, z,c} = {1'bx, 1'bx, 1'bx,1'bx};
                    error = 0;
                end
                default :begin 
                    error = 1;  
                end  
            endcase
        end
endmodule