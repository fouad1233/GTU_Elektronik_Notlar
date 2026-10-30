.global _start
_start:
	MOV R1,#0x44
	MOV R2,#0x06
	STR R2,[R1]
	MOV R2,#0XFC
	STR R2,[R1,#4]
	MOV R2,#0X03
	STR R2,[R1,#8]
	MOV R2,#0XFF
	STR R2,[R1,#12]
	MOV R2,#0
	LDRSB R2, [R1]