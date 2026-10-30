`timescale 1ns/1ns // bu komut fouadta çalışmamaktadır normalde kullanılması gerekmektedir
module tb_lab2_g5_p2();
    logic x3,x2,x1,x0;
    logic A,B,C,D,E,F,G;
    lab2_g5_p2 dut1(x3,x2,x1,x0,A,B,C,D,E,F,G);
    initial begin
        
        $dumpfile("lab2_g5_p2.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_lab2_g5_p2);
        x3=0; x2=0; x1=0; x0=0; #10;
        x3=0; x2=0; x1=0; x0=1; #10;
        x3=0; x2=0; x1=1; x0=0; #10;
        x3=0; x2=0; x1=1; x0=1; #10;
        x3=0; x2=1; x1=0; x0=0; #10;
        x3=0; x2=1; x1=0; x0=1; #10;
        x3=0; x2=1; x1=1; x0=0; #10;
        x3=0; x2=1; x1=1; x0=1; #10;
        x3=1; x2=0; x1=0; x0=0; #10;
        x3=1; x2=0; x1=0; x0=1; #10;
        x3=1; x2=0; x1=1; x0=0; #10;
        x3=1; x2=0; x1=1; x0=1; #10;
        x3=1; x2=1; x1=0; x0=0; #10;
        x3=1; x2=1; x1=0; x0=1; #10;
        x3=1; x2=1; x1=1; x0=0; #10;
        x3=1; x2=1; x1=1; x0=1; #10;

        $finish;


    end

endmodule