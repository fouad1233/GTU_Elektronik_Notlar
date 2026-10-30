/* tb_lab3_g5_p1.sv */
/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o tb_lab3_g5_p2 tb_lab3_g5_p2.sv lab3_g5_p2.sv
vvp tb_lab3_g5_p2

*/
`timescale 1ns/1ns 
module tb_lab3_g5_p2();
    
    logic A,B,Yand,Yor,YnotA,Ynand,Ynor, Y4bitmux,Y8bitmux, Y16bitmux;
    logic [15:0] Aarray;
    logic [4:0] S;
    AND_MUX dut1(A,B,Yand);//device under test 1
    OR_MUX dut2(A,B,Yor);//device under test 2
    NOT_MUX dut3(A,YnotA);//device under test 3
    NAND_MUX dut4(A,B,Ynand);//device under test 4
    NOR_MUX dut5(A,B,Ynor);//device under test 5
    MUX4x1 dut6(Aarray[3:0], S[1:0],Y4bitmux);//device under test 6
    MUX8x1 dut7(Aarray[7:0], S[2:0],Y8bitmux);//device under test 7
    MUX16x1 dut8(Aarray[15:0], S[3:0],Y16bitmux);//device under test 8
    

    initial begin
        $dumpfile("lab3_g5_p2.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_lab3_g5_p2); 
        A=0;B=0;#10;
        if ( Yand!=0) $display("For A=%b B=%b yexpected = 0 but Yand=%d FAIL",A,B,Yand);
        if ( Yor!=0) $display("For A=%b B=%b yexpected = 0 but Yor=%d FAIL",A,B,Yor);
        if ( YnotA!=1) $display("For A=%b yexpected = 1 but YnotA=%d FAIL",A,YnotA);
        if (Ynand!=1) $display("For A=%b B=%b yexpected = 1 but Ynand=%d FAIL",A,B,Ynand);
        if (Ynor!=1) $display("For A=%b B=%b yexpected = 1 but Ynor=%d FAIL",A,B,Ynor);
        A=0;B=1;#10;
        if ( Yand!=0) $display("For A=%b B=%b yexpected = 0 but Yand=%d FAIL",A,B,Yand);
        if ( Yor!=1) $display("For A=%b B=%b yexpected = 1 but Yor=%d FAIL",A,B,Yor);
        if ( YnotA!=1) $display("For A=%b yexpected = 1 but YnotA=%d FAIL",A,YnotA);
        if (Ynand!=1) $display("For A=%b B=%b yexpected = 1 but Ynand=%d FAIL",A,B,Ynand);
        if (Ynor!=0) $display("For A=%b B=%b yexpected = 0 but Ynor=%d FAIL",A,B,Ynor);
        A=1;B=0;#10;
        if ( Yand!=0) $display("For A=%b B=%b yexpected = 0 but Yand=%d FAIL",A,B,Yand);
        if ( Yor!=1) $display("For A=%b B=%b yexpected = 1 but Yor=%d FAIL",A,B,Yor);
        if ( YnotA!=0) $display("For A=%b yexpected = 0 but YnotA=%d FAIL",A,YnotA);
        if (Ynand!=1) $display("For A=%b B=%b yexpected = 1 but Ynand=%d FAIL",A,B,Ynand);
        if (Ynor!=0) $display("For A=%b B=%b yexpected = 0 but Ynor=%d FAIL",A,B,Ynor);
        A=1;B=1;#10;
        if ( Yand!=1) $display("For A=%b B=%b yexpected = 1 but Yand=%d FAIL",A,B,Yand);
        if ( Yor!=1) $display("For A=%b B=%b yexpected = 1 but Yor=%d FAIL",A,B,Yor);
        if ( YnotA!=0) $display("For A=%b yexpected = 0 but YnotA=%d FAIL",A,YnotA);
        if (Ynand!=0) $display("For A=%b B=%b yexpected = 0 but Ynand=%d FAIL",A,B,Ynand);
        if (Ynor!=0) $display("For A=%b B=%b yexpected = 0 but Ynor=%d FAIL",A,B,Ynor);
        
        //$finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez

    end
    integer i,j;
    initial begin
        for (i = 0; i < 16; i = i + 1) begin
            for (j = 0; j < 65536 ; j = j + 1) begin
                S = i;
                Aarray = j;
                #10;//burada 10ns bekliyoruz
            end
        end
        $finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez
    end

endmodule
