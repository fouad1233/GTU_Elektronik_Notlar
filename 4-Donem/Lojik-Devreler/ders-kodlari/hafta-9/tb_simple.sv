/* tb_lab2_g5_p1.sv */
/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o tb_simple tb_simple.sv sillyfunction.sv
vvp tb_simple

*/
`timescale 1ns/1ns 
module tb_simple();
    logic a,b,c;
    logic y;
    sillyfunction dut0(.a(a),.b(b),.c(c),.y(y));//device under test
    initial begin 
        $dumpfile("tb_simple.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_simple); 
        a=0;b=0;c=0; #10;
        a=0;b=0;c=1; #10;
        a=0;b=1;c=0; #10;
        a=0;b=1;c=1; #10;
        a=1;b=0;c=0; #10;
        
        $finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez

    end
endmodule
