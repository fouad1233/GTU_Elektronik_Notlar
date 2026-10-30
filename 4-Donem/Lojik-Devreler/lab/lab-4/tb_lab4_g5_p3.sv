/* tb_lab3_g5_p1.sv */
/*fouad için kodu çalıştırma komutu 
iverilog -g2012 -o tb_lab4_g5_p3 tb_lab4_g5_p3.sv lab4_g5_p3.sv
vvp tb_lab4_g5_p3

*/
`timescale 1ns/1ns 
module tb_lab4_g5_p3();
    logic [31:0] A, B;
    logic signed [31:0] signed_A, signed_B;
    logic [ 3:0] op;
    logic [31:0] Y;
    logic n, z, v, c;
    logic error;
    lab4_g5_p3 dut1(A,B,op,Y,n,z,v,c,error);//device under test
    initial begin 
        $dumpfile("lab4_g5_p3.vcd");//modelsim ile çalışırken bu  ve sonraki satır silenebilir
        $dumpvars(0, tb_lab4_g5_p3); 
        A = 32'b11111111111111111111111111110010;
        B = 32'b00000000000000001111111111111101;
        op = 4'b0000;
        //toplama için deneme
        #10;
        $display("sum");
        $display("A = %b, B = %b, op = %b", A, B, op);
        $display("Y = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);
        //çıkarma için deneme
        op = 4'b1000;
        #10;
        $display("sub");
        $display("A = %b, B = %b, op = %b", A, B, op);
        $display("Y = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);
        //signed compare
        A = 32'b10000000000000000000000000000001;
        B = 32'b00000000000000000000000000000001;
        assign signed_A = A;
        assign signed_B = B;
        op = 4'b0010;
        #10;
        $display("signed compare");
        $display("A = %b, B = %b, op = %b", signed_A, signed_B, op);
        $display("A = %d, B = %d, op = %d", signed_A, signed_B, op);
        $display("Y = A>B = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);
        //unsigned compare
        A = 32'b10000000000000000000000000000001;
        B = 32'b00000000000000000000000000000001;
        op = 4'b0011;
        #10;
        $display("unsigned compare");
        $display("A = %b, B = %b, op = %b", A, B, op);
        $display("A = %d, B = %d, op = %d", A, B, op);
        $display("Y = A>B = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);
        //left shift
        A = 32'b10000000000000000000000000000001;
        B = 32'b00000000000000000000000000000001;
        op = 4'b0001;
        #10;
        $display("left shift");
        $display("A = %b, B = %b, op = %b", A, B, op);
        $display("A = %d, B = %d, op = %d", A, B, op);
        $display("Y = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);
        
        A = 32'b00000000000000100010000000000001;
        B = 32'b00000000000000000000000000000001;
        op = 4'b0001;
        #10;
        $display("A = %b, B = %b, op = %b", A, B, op);
        $display("A = %d, B = %d, op = %d", A, B, op);
        $display("Y = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);
        // logical shift right 
        A = 32'b0000000000000000010000000000001;
        B = 32'b000000000000000000000000000000011;
        op = 4'b0101;
        #10;
        $display("logical shift right");
        $display("A = %b, B = %b, op = %b", A, B, op);
        $display("A = %d, B = %d, op = %d", A, B, op);
        $display("Y = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);
        
        A = 32'b00000000000000100010000000000000;
        B = 32'b00000000000000000000000000000001;
        op = 4'b0101;
        #10;
        $display("A = %b, B = %b, op = %b", A, B, op);
        $display("A = %d, B = %d, op = %d", A, B, op);
        $display("Y = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);
        //xor test code
        A = 32'b10000000000000000000000000000001;
        B = 32'b00000000000000000000000000000001;
        op = 4'b0100;
        #10;
        $display("xor");
        $display("A = %b, B = %b, op = %b", A, B, op);
        $display("A = %d, B = %d, op = %d", A, B, op);
        $display("Y = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);
        
        A = 32'b00000000000000100010000000000001;
        B = 32'b00000000000000000000000000000001;
        op = 4'b0100;
        #10;
        $display("A = %b, B = %b, op = %b", A, B, op);
        $display("A = %d, B = %d, op = %d", A, B, op);
        $display("Y = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);
        //arithmatic shift right
        A = 32'b10000000000000000000000000000001;
        B = 32'b00000000000000000000000000010001;
        op = 4'b1101;
        #10;
        $display("Arithmetic shift right");
        $display("A = %b, B = %b, op = %b", A, B, op);
        $display("A = %d, B = %d, op = %d", A, B, op);
        $display("Y = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);
        
        A = 32'b00000000000000100010000000000001;
        B = 32'b00000000000000000000000000000001;
        op = 4'b1101;
        #10;
        $display("A = %b, B = %b, op = %b", A, B, op);
        $display("A = %d, B = %d, op = %d", A, B, op);
        $display("Y = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);

        //or test code
        A = 32'b10000000000000000000000000000001;
        B = 32'b00000000000000000000000000000001;
        op = 4'b0110;
        #10;
        $display("or");
        $display("A = %b, B = %b, op = %b", A, B, op);
        $display("A = %d, B = %d, op = %d", A, B, op);
        $display("Y = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);
        
        A = 32'b00000000000000100010000000000001;
        B = 32'b00000000000000000000000000000001;
        op = 4'b0110;
        #10;
        $display("A = %b, B = %b, op = %b", A, B, op);
        $display("A = %d, B = %d, op = %d", A, B, op);
        $display("Y = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);
        //and test code
        A = 32'b10000000000000000000000000000001;
        B = 32'b00000000000000000000000000000001;
        op = 4'b0111;
        #10;
        $display("and");
        $display("A = %b, B = %b, op = %b", A, B, op);
        $display("A = %d, B = %d, op = %d", A, B, op);
        $display("Y = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);
        
        A = 32'b00000000000000100010000000000001;
        B = 32'b00000000000000000000000000000001;
        op = 4'b0111;
        #10;
        $display("A = %b, B = %b, op = %b", A, B, op);
        $display("A = %d, B = %d, op = %d", A, B, op);
        $display("Y = %b, error = ", Y, error);
        $display("n = %b, z = %b, v = %b, c = %b\n", n, z, v, c);
        
        $finish;//$stop;//model sim ile çalışıken bunu silip stop koymak gerekir yoksa wave form gözükmez

    end
endmodule
