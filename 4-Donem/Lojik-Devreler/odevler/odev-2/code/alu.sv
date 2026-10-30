//alu.sv
module ALU (
  input signed  [15:0] operandA,
  input signed [15:0] operandB,
  input signed [3:0] operation,
  output logic N, Z, V, C,
  output  logic signed [15:0] result,
  output logic HS, LS , HI ,LO
);

  always @(*) begin
    case (operation)
      4'b0000: begin  // Operation: Subtract
        result = operandA - operandB;
        N = result[15];
        Z = (result == 0);
        V = (operandA[15] == operandB[15] && operandA[15] != result[15]);
        C = (operandA < operandB);
        HS = ~(N^V);  
        LS = N^V | Z;
        HI = ~LS;
        LO = ~HS;
        
      end

      4'b0001: begin  // Operation: Add
        result = operandA + operandB;
        N = result[15];
        Z = (result == 0);
        V = (operandA[15] == operandB[15] && operandA[15] != result[15]);
        C = (result < operandA);
        
      end

      default: begin
        result = 16'hxxxx;
        N = 1'b0;
        Z = 1'b0;
        V = 1'b0;
        C = 1'b0;
      end
    endcase
  end
endmodule