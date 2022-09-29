org 0000h
LJMP MAIN
 
org 0080h
MAIN:
LCALL ALOCA

org 0020h
ALOCA:
mov 20h, #002h
mov 21h, #002h
mov 22h, #001h
mov 23h, #002h
mov 24h, #000h
mov 25h, #000h
mov 26h, #002h
mov 27h, #001h
mov r0, #20h
mov r1, #8
mov r2, #0000h

SOMA:
mov a, @r0
add a, r2
mov r2 ,a
inc r0
djnz r1, SOMA

mov r2, a
mov 30h, a