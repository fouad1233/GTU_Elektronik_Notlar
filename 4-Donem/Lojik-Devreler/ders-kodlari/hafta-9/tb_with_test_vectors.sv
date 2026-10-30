//tb_with_test_vectors.sv

/* tb_lab2_g5_p1.sv */
/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o tb_with_test_vectors tb_with_test_vectors.sv sillyfunction.sv
vvp tb_with_test_vectors

*/
`timescale 1ns/1ns 
module tb_with_test_vectors();
    logic clk,reset;//cloack ve reset are internal
    logic a,b,c,yexpected;
    logic y;
    logic [31:0] vectornum, errors;
    logic [3:0] testvectors[10000:0];
    sillyfunction dut1(.a(a),.b(b),.c(c),.y(y));//device under test
    // generate clock
    always begin 
        
        clk=1; #5; clk=0; #5; //10 ns period
        
        //$finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez

    end
    //at start of test ,load vectors
    //and pulse reset
    initial     //Will execute at the beginning of simulation
        begin
            $dumpfile("tb_with_test_vectors.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
            $dumpvars(0, tb_with_test_vectors); 
            $readmemb("example.txt",testvectors);//Read vectors
            vectornum=0; errors=0;//Initialize
            reset=1; #27; reset=0;// Apply reset wait
            
        end
    //Note : $readmemh reads testvectors files written in hexadecimal
    //apply test vectors on rising edge of clock
    always @(posedge clk)
        begin
            #1; {a,b,c,yexpected}=testvectors[vectornum];
            //vectornum=vectornum+1;
            //if (vectornum==10000) $finish;
        end
    //check results on falling edge of clock
    always @(negedge clk)
    if (~reset)
        begin
            if (y!=yexpected) 
                begin
                    $display("Error: inputs %b",{a,b,c});
                    $display("Output = %b (%b exp)",y,yexpected);
                    errors=errors+1;
                end
            //İncrement array index and read next testvector
            vectornum=vectornum+1;
            if (testvectors[vectornum]=== 4'bx) 
            begin
                $display("%d tests completed with %d errors",vectornum,errors);
                $finish;
            end
            //Note: === and !== can compare values that are x or z
        end
        //Note : to print in hexadecimal use %h instead of %b
    
    
            
endmodule
