/*iverilog kodu çalıştırma komutu 
iverilog -g2012 -o tb_alu tb_alu.sv alu.sv
vvp tb_alu

*/
module tb_alu();
  logic signed [15:0] operandA, operandB;
  logic [3:0] operation;
  logic N, Z, V, C;
  logic signed [15:0] result;
  logic unsigned HS, LS , HI ,LO;
  logic signed [15:0] A ,B;
  ALU uut (
    .operandA(operandA),
    .operandB(operandB),
    .operation(operation),
    .N(N),
    .Z(Z),
    .V(V),
    .C(C),
    .result(result),
    .HS(HS),
    .LS(LS),
    .HI(HI),
    .LO(LO)

  );

  initial begin
    $dumpfile("tb_alu.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
    $dumpvars(0, tb_alu); 
    // Test case A
    operandA = 16'h1F32;
    operandB = 16'hFF02;
    A = operandA;
    B = operandB;
    operation = 4'b0000; // Subtract
    #10; // Wait for ALU computation
    $display("Test case A:");
    $display("Result: %h", result);
    $display("N: %b, Z: %b, V: %b, C: %b", N, Z, V, C);
    $display("HS: %b, LS: %b, HI: %b, LO: %b", HS, LS, HI, LO);
    $display("operandA: %h, operandB: %h", operandA, operandB);
    $display("A: %h, B: %h", A, B);
    $display("expected HS: %b, LS: %b, HI: %b, LO: %b", (A>B ) , (A<B  ), (A>B & A!=B) , (A<B& A!=B) );

    // Test case B
    operandA = 16'hF801;
    operandB = 16'h7000;
    A = operandA;
    B = operandB;
    operation = 4'b0000; // Subtract
    #10; // Wait for ALU computation
    $display("Test case B:");
    $display("Result: %b", result);
    $display("N: %b, Z: %b, V: %b, C: %b", N, Z, V, C);
    $display("HS: %b, LS: %b, HI: %b, LO: %b", HS, LS, HI, LO);
    $display("expected HS: %b, LS: %b, HI: %b, LO: %b",  A>B | A==B , A<B | B==A , A>B & A!=B , A<B & A!=B);
    // Test case C
    operandA = 16'hFE02;
    operandB = 16'h00DF;
    A = operandA;
    B = operandB;
    operation = 4'b0000; // Subtract
    #10; // Wait for ALU computation
    $display("Test case C:");
    $display("Result: %h", result);
    $display("N: %b, Z: %b, V: %b, C: %b", N, Z, V, C);
    $display("HS: %b, LS: %b, HI: %b, LO: %b", HS, LS, HI, LO);
    $display("expected HS: %b, LS: %b, HI: %b, LO: %b", A>B | A==B , A<B | B==A , A>B & A!=B , A<B& A!=B);
    $finish;
  end
endmodule