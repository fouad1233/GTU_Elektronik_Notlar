/* tb_lab2_g5_p1.sv */
`timescale 1ns/1ns // bu komut fouadta çalışmamaktadır normalde kullanılması gerekmektedir
module tb_lab2_g5_p1();
    logic A,B,C,D;
    logic Y,X;
    lab2_g5_p1 dut0(A,B,C,D,Y,X);
    initial begin
        $dumpfile("lab2_g5_p1.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_lab2_g5_p1);
        
        
        A=0;B=0;C=0;D=0;#10;
        A=0;B=0;C=0;D=1;#10;
        A=0;B=0;C=1;D=0;#10;
        A=0;B=0;C=1;D=1;#10;
        A=0;B=1;C=0;D=0;#10;
        A=0;B=1;C=0;D=1;#10;
        A=0;B=1;C=1;D=0;#10;
        A=0;B=1;C=1;D=1;#10;
        A=1;B=0;C=0;D=0;#10;
        A=1;B=0;C=0;D=1;#10;
        A=1;B=0;C=1;D=0;#10;
        A=1;B=0;C=1;D=1;#10;
        A=1;B=1;C=0;D=0;#10;
        A=1;B=1;C=0;D=1;#10;
        A=1;B=1;C=1;D=0;#10;
        A=1;B=1;C=1;D=1;#10;

        $finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez

end
endmodule
