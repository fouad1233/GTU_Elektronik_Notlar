.global _start
_start:
	
	    // Initialize the first 128-bit number
    // Let's say the number is 0x11111111222222223333333344444444
    LDR     R7, =0x11111111
    LDR     R6, =0x22222222
    LDR     R5, =0x33333333
    LDR     R4, =0x44444444

    // Initialize the second 128-bit number
    // Let's say the number is 0x00000000000000001111111111111111
    LDR     R11, =0x00000000
    LDR     R10, =0x00000000
    LDR     R9,  =0x11111111
    LDR     R8,  =0x11111111

    // Perform the subtraction
    SUBS    R0, R4, R8
    SBCS    R1, R5, R9
    SBCS    R2, R6, R10
    SBC     R3, R7, R11

    // Now R3:R2:R1:R0 contains the result
    // Expected result: 0x11111111222222212222222233333333

    // Test the result
    // Load expected values into another set of registers for comparison
    LDR     R12, =0x11111111
    LDR     R13, =0x22222221
    LDR     R14, =0x22222222
    LDR     R15, =0x33333333

    // Compare results
    CMP     R0, R15
    CMPNE   R1, R14
    CMPNE   R2, R13
    CMPNE   R3, R12
    // Add code here to handle the comparison results

	b .
