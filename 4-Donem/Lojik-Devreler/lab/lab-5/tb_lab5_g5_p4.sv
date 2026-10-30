/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o tb_lab5_g5_p4 tb_lab5_g5_p4.sv lab5_g5_p4.sv
vvp tb_lab5_g5_p4
*/
`timescale 1ns/1ns
module tb_lab5_g5_p4();
    
    // İsimlendirme ve zamanlama parametreleri
    parameter CLK_PERIOD = 10;
    integer i;
    // Sinyal tanımları
    logic [4:0] D;
    logic baslat,clk,reset,Y,mesgul;
    // Modül örneği
    lab5_g5_p4 dut3 (
        .baslat(baslat),
        .clk(clk),
        .reset(reset),
        .D(D),
        .Y(Y),
        .mesgul(mesgul)
    );
    
    
    // Clock sinyali oluşturma
    initial begin 
        clk=0;
            forever #(CLK_PERIOD/2) clk=~clk;
    end
    
    
    // Test senaryosu
    initial begin
        $dumpfile("lab5_g5_p4.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_lab5_g5_p4); 
        D = 5'b10100;
        baslat=1;
        reset = 1;
        #20
        reset = 0;
        #11
        baslat=1;
        #11
        baslat=0;
        #300


        $finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez
    end

endmodule


