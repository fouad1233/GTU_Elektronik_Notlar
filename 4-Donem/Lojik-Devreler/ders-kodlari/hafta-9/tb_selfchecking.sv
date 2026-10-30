/* tb_lab2_g5_p1.sv */
/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o tb_selfchecking tb_selfchecking.sv sillyfunction.sv
vvp tb_selfchecking

*/
`timescale 1ns/1ns 
module tb_selfchecking();
    logic a,b,c;
    logic y;
    sillyfunction dut1(.a(a),.b(b),.c(c),.y(y));//device under test
    initial begin 
        $dumpfile("tb_selfchecking.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_selfchecking); 
        a=0;b=0;c=0; #10;
        if (y!=1) $display("000 failed");
        a=0;b=0;c=1; #10;
        if (y!=0) $display("001 failed");
        a=0;b=1;c=0; #10;
        if (y!=0) $display("010 failed");
        a=0;b=1;c=1; #10;
        if (y!=1) $display("011 failed");//kasten hatalı yapıldı
        a=1;b=0;c=0; #10;
        if (y!=1) $display("100 failed");
        
        $finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez

    end
endmodule
