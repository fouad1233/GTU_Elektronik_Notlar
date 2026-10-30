/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o tb_lab4_g5_p1 tb_lab4_g5_p1.sv lab4_g5_p1.sv
vvp tb_lab4_g5_p1

*/
`timescale 1ns/1ns 
module tb_lab4_g5_p1();
    logic clk,rst,d,qrisingedge,qfallingedge,l;
    DFlipFlopRisingEdge DUT1(clk,rst,d,qrisingedge);
    DFlipFlopFallingEdge DUT2(clk,rst,d,qfallingedge);
    latch DUT3(clk,d,l);
    initial begin 
        clk=0;
            forever #5 clk=~clk;
    end
    initial begin 
        $dumpfile("lab4_g5_p1.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_lab4_g5_p1); 
        /*
        rst=1;
        d<=1;
        #50
        rst = 0 ;
        d<=0;#50
        d<=1;#50
        d<=0;#50
        d<=1;#50
        */
        rst= 0;
        d<=0;   #7
        d<=1;   #9
        d<=0;   #2
        d<=1;   #3
        d<=0;   #1
        
        $finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez

    end
endmodule


