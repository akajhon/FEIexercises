MOV R0, #02
MOV R1, #02
MOV R2, #01
MOV R3, #02
MOV R4, #00
MOV R5, #00
MOV R6, #02
MOV R7, #01

MOV PSW, #00010000
MOV R0, #02
MOV R1, #02
MOV R2, #01
MOV R3, #02
MOV R4, #00
MOV R5, #00
MOV R6, #02
MOV R7, #01
CLR A
ADD A, R0
ADD A, R1
ADD A, R2
ADD A, R3
ADD A, R4
ADD A, R5
ADD A, R6
ADD A, R7

MOV PSW, #00011000
MOV R0, A