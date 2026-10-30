/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o tb_lab5_g5_p3 tb_lab5_g5_p3.sv lab5_g5_p3.sv
vvp tb_lab5_g5_p3
*/
`timescale 1ns/1ns
module tb_lab5_g5_p3();
    
    // İsimlendirme ve zamanlama parametreleri
    parameter CLK_PERIOD = 10;
    integer i;
    // Sinyal tanımları
    logic A,clk,reset,Y;
    // Modül örneği
    lab5_g5_p3 dut3 (
        .A(A),
        .clk(clk),
        .reset(reset),
        .Y(Y)
    );
    
    
    // Clock sinyali oluşturma
    initial begin 
        clk=0;
            forever #(CLK_PERIOD/2) clk=~clk;
    end
    
    
    // Test senaryosu
    initial begin
        $dumpfile("lab5_g5_p3.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_lab5_g5_p3); 
        reset = 1;
        #10 
        reset = 0;
        #10
        for( i = 0; i < 2000; i= i + 1)
            begin
                //A = ! A; #1200;
                A = $random; #10;
                
            end


        $finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez
    end

endmodule


