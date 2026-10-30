/* tb_lab3_g5_p1.sv */
/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o tb_lab3_g5_p5 tb_lab3_g5_p5.sv lab3_g5_p5.sv
vvp tb_lab3_g5_p5

*/
`timescale 1ns/1ns
module tb_lab3_g5_p5();
    //logic [3:0] Anarray;
    logic A,B,C,D;
    logic F1, F2;
    
    //decoder3x8 dut0(A,E,D3x8);//device under test 0
    lab3_g5_p5 dut1(A,B,C,D, F1,F2);//device under test 1 //decoder 4x16
    integer i;
    initial begin 
        $dumpfile("lab3_g5_p5.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_lab3_g5_p5); 
        
        for (i = 0; i < 16; i = i + 1) begin
            //A = Anarray;
            {A,B,C,D} = i;
            #10;//burada 10ns bekliyoruz
        end
        
        
        $finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez

    end
endmodule