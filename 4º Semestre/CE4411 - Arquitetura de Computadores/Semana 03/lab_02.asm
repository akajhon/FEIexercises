number EQU 40h
MOV number, #40h

MOV 0050h, number
MOV A, #0FFh

XCH A,number
MOV R2, #number

END
