module tb_lab1_g5_p1();

logic G,T,U,E;
logic Y;

lab1_g5_p1 dut0(G,T,U,E,Y);
initial begin
    $dumpfile("lab1_g5_p1.vcd");
    $dumpvars(0, tb_lab1_g5_p1);
    //`timescale 10ns/1ps //this code makes the simulation run 10 ns per 1 ps
	G = 0 ; T = 0 ;  U = 0 ; E = 0;	        #10
	E = 1; #10
	U = 1; E = 0; #10
	E = 1 ; #10
	T = 1; U = 0; E = 0; #10
	E = 1; #10
	U= 1; E = 0; #10
	E = 1; #10
	G = 1; T = 0; U =0; E = 0; #10
	E = 1;	#10
	U = 1; E = 0; #10
	E = 1; #10
	T = 1; U =0 ; E = 0; #10
	E = 1; #10
	U = 1; E = 0; #10
	E = 1; #10
	$stop;
end
endmodule