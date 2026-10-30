//hw3_p2_moore.sv
/* iverilog kodu çalıştırma komutu 
iverilog -g2012 -o tb_hw3_p2_moore tb_hw3_p2_moore.sv hw3_p2_moore.sv
vvp tb_hw3_p2_moore
*/
`timescale 1ns/1ns 
module tb_hw3_p2_moore();
    logic clk,reset,A,B;
    integer i;
    hm3_p2_moore dut(.clk(clk),.reset(reset),.A(A),.B(B));
    initial begin
        #1 clk = 0;
           forever begin
                      # 300 clk = ! clk;
                   end
            end
    initial begin 
        $dumpfile("hw3_p2_moore.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_hw3_p2_moore); 
        reset= 1; #100;
        reset= 0;
        A= 1; #1200;
        for( i = 0; i < 2000; i= i + 1)
            begin
            
            A = $random; #300; //random sayı üretir
            
            end
        
        $finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez

    end
endmodule


