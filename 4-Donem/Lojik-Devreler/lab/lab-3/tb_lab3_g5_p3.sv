/* tb_lab3_g5_p1.sv */
/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o tb_lab3_g5_p3 tb_lab3_g5_p3.sv lab3_g5_p3.sv
vvp tb_lab3_g5_p3

*/
`timescale 1ns/1ns 
module tb_lab3_g5_p3();
    logic [1:0] A;
    logic [3:0] D2x4;
    logic E;
    lab3_g5_p3 dut1(A,E,D2x4);//device under test 1
    initial begin 
        $dumpfile("lab3_g5_p3.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_lab3_g5_p3); 
        A[1]=0;A[0]=0;E= 0 ;#10;
        if (D2x4!=4'b0000) $display("D2x4=0000 is expected but D2x4=%b is observed",D2x4);
        A[1]=0;A[0]=1;#10;
        if (D2x4!=4'b0000) $display("D2x4=0000 is expected but D2x4=%b is observed",D2x4);
        A[1]=1;A[0]=0;#10;
        if (D2x4!=4'b0000) $display("D2x4=0000 is expected but D2x4=%b is observed",D2x4);
        A[1]=1;A[0]=1;#10;
        if (D2x4!=4'b0000) $display("D2x4=0000 is expected but D2x4=%b is observed",D2x4);
        E = 1;
        A[1]=0;A[0]=0;#10;
        if (D2x4!=4'b0001) $display("D2x4=0001 is expected but D2x4=%b is observed",D2x4);
        A[1]=0;A[0]=1;#10;
        if (D2x4!=4'b0010) $display("D2x4=0010 is expected but D2x4=%b is observed",D2x4);
        A[1]=1;A[0]=0;#10;
        if (D2x4!=4'b0100) $display("D2x4=0100 is expected but D2x4=%b is observed",D2x4);
        A[1]=1;A[0]=1;#10;
        if (D2x4!=4'b1000) $display("D2x4=1000 is expected but D2x4=%b is observed",D2x4);
        
        $finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez

    end
endmodule
