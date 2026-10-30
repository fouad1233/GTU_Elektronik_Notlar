/* tb_lab3_g5_p1.sv */
/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o tb_lab3_g5_p4 tb_lab3_g5_p4.sv lab3_g5_p4.sv
vvp tb_lab3_g5_p4

*/
`timescale 1ns/1ns
module tb_lab3_g5_p4();
    logic [3:0] A;
    logic [15:0] D4x16;
    logic E;
    //decoder3x8 dut0(A,E,D3x8);//device under test 0
    lab3_g5_p4 dut1(A,E,D4x16);//device under test 1 //decoder 4x16
    integer i;
    initial begin 
        $dumpfile("lab3_g5_p4.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_lab3_g5_p4); 
        
        E = 0;
        for (i = 0; i < 16; i = i + 1) begin
            A = i;
            #10;//burada 10ns bekliyoruz
        end
        E = 1;
        for (i = 0; i < 16; i = i + 1) begin
            A = i;
            #10;//burada 10ns bekliyoruz
        end
        
        $finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez

    end
endmodule