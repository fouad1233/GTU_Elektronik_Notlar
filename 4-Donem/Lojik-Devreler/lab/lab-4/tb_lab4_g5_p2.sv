/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o tb_lab4_g5_p2 tb_lab4_g5_p2.sv lab4_g5_p2.sv
vvp tb_lab4_g5_p2

*/
`timescale 1ns/1ns 
module tb_lab4_g5_p2();
    logic A,B,S,Cout,Cin,Sfull,Coutfull,Cout5bit;
    logic [4:0] A5bit,B5bit,S5bit;
    halfadder DUT1(A,B,S,Cout);
    fulladder DUT2(A,B,Cin,Sfull,Coutfull);
    RippleCarryAdder DUT3(A5bit,B5bit,S5bit,Cout5bit);

    
    initial begin 
        $dumpfile("lab4_g5_p2.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_lab4_g5_p2); 
        /*
        Cin = 0;A = 0; B = 0; #10;
        $display("A=%b B=%b  Cout=%b S=%b Coutexpected=%b Sexpected=%b ",A,B,Cout,S,1'b0,1'b0);
        Cin = 0; A = 0; B = 1; #10;
        $display("A=%b B=%b  Cout=%b S=%b Coutexpected=%b Sexpected=%b",A,B,Cout,S,1'b0,1'b1);
        Cin = 0; A = 1; B = 0; #10;
        $display("A=%b B=%b  Cout=%b S=%b Coutexpected=%b Sexpected=%b",A,B,Cout,S,1'b0,1'b1);
        Cin = 0; A = 1; B = 1; #10;
        $display("A=%b B=%b  Cout=%b S=%b Coutexpected=%b Sexpected=%b",A,B,Cout,S,1'b1,1'b0);
        
        Cin = 1;A = 0; B = 0; #10;
        $display("A=%b B=%b  Cout=%b S=%b Coutexpected=%b Sexpected=%b ",A,B,Cout,S,1'b0,1'b0);
        Cin = 1; A = 0; B = 1; #10;
        $display("A=%b B=%b  Cout=%b S=%b Coutexpected=%b Sexpected=%b",A,B,Cout,S,1'b0,1'b1);
        Cin = 1; A = 1; B = 0; #10;
        $display("A=%b B=%b  Cout=%b S=%b Coutexpected=%b Sexpected=%b",A,B,Cout,S,1'b0,1'b1);
        Cin = 1; A = 1; B = 1; #10;
        $display("A=%b B=%b  Cout=%b S=%b Coutexpected=%b Sexpected=%b",A,B,Cout,S,1'b1,1'b0);
        */
        repeat (16) begin
            A5bit = $random;
            B5bit = $random;
            
            #10;
        end
        
        $finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez

    end
endmodule


