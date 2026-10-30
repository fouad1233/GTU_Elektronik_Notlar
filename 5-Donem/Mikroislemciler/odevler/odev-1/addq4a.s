.global _start
_start:
	MOVS R1,#0x01
	ADDS R6,R1,#0xEA @Add to R1 0xEA and write it to R6
	MOVS R0,R6 @Write the content of R6 to R0