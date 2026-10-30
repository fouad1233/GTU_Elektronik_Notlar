/* tb_lab3_g5_p1.sv */
/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o tb_lab3_g5_p1 tb_lab3_g5_p1.sv lab3_g5_p1.sv
vvp tb_lab3_g5_p1

*/
`timescale 1ns/1ns 
module tb_lab3_g5_p1();
    logic [1:0] A;
    logic S,Y;
    lab3_g5_p1 dut1(A,S,Y);//device under test
    initial begin 
        $dumpfile("lab3_g5_p1.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_lab3_g5_p1); 
        A[1]=0;A[0]=0;S=0 ;#10;
        if ( Y!=0) $display("For A=%b S=%d, yexpected = 0 but Y=%d FAIL",A,S,Y);
        A[1]=0;A[0]=0;S=1 ;#10;
        if ( Y!=0) $display("For A=%b S=%d, yexpected = 0 but Y=%d FAIL",A,S,Y);
        A[1]=0;A[0]=1;S=0 ;#10;
        if ( Y!=1) $display("For A=%b S=%d, yexpected = 1 but Y=%d FAIL",A,S,Y);
        A[1]=0;A[0]=1;S=1 ;#10;
        if ( Y!=0) $display("For A=%b S=%d, yexpected = 0 but Y=%d FAIL",A,S,Y);
        A[1]=1;A[0]=0;S=0 ;#10;
        if ( Y!=0) $display("For A=%b S=%d, yexpected = 0 but Y=%d FAIL",A,S,Y);
        A[1]=1;A[0]=0;S=1 ;#10;
        if ( Y!=1) $display("For A=%b S=%d, yexpected = 1 but Y=%d FAIL",A,S,Y);
        A[1]=1;A[0]=1;S=0 ;#10;
        if ( Y!=1) $display("For A=%b S=%d, yexpected = 1 but Y=%d FAIL",A,S,Y);
        A[1]=1;A[0]=1;S=1 ;#10;
        if ( Y!=1) $display("For A=%b S=%d, yexpected = 1 but Y=%d FAIL",A,S,Y);
        $finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez

    end
endmodule
