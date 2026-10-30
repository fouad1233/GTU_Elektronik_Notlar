.global _start
_start:
	LDR r0,=#0x20000024
	MOVS r1,#15
	STR r1,[r0]
	
	MOVS r1,#18
	STR r1,[r0,#4]
	
	MOVS r1,#17
	STR r1,[r0,#8]
	
	MOVS r1,#16
	STR r1,[r0,#12]
	
	LDR r1, [r0]
	LDR r2, [r0,#4]
	LDR r3, [r0,#8]
	LDR r4, [r0,#12]
	
	ADDS r5 , r1 ,r2
	ADDS r5 , r3
	ADDS r5 , r4
	STR r6, [r0,#16]