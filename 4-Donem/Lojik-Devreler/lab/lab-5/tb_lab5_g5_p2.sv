/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o tb_lab5_g5_p2 tb_lab5_g5_p2.sv lab5_g5_p2.sv
vvp tb_lab5_g5_p2

*/
`timescale 1ns/1ns 
module tb_lab5_g5_p2();

    // İsimlendirme ve zamanlama parametreleri
    parameter CLK_PERIOD = 10;

    // Sinyal tanımları
    logic clk, reset, en,bitti;
    logic [4:0] psc;
    logic [15:0] reload , cnt;
    

    // Modül örneği
    lab5_g5_p2 dut1 (
        .clk(clk),
        .reset(reset),
        .en(en),
        .psc(psc),
        .reload(reload),
        .cnt(cnt),
        .bitti(bitti)
    );
    
    
    // Clock sinyali oluşturma
    initial begin 
        clk=0;
            forever #(CLK_PERIOD/2) clk=~clk;
    end
    
    
    // Test senaryosu
    initial begin
        $dumpfile("lab5_g5_p2.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_lab5_g5_p2); 
        
        psc = 5'b00101;
        reload = 16'b0000000000010000;
        // Reset sinyali aktif hale getiriliyor
        reset = 1'b0;
        en = 1'b0;

        
        #10;

        // Reset sinyali pasif hale getiriliyor
        reset = 1'b1;
        en = 1'b1;
        #2000;


        $finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez
    end

endmodule


