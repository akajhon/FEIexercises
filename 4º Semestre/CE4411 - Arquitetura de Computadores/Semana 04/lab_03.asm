org 0000h
LJMP MAIN
 
org 0080h
MAIN:
LCALL ALOCA

 
org 0020h
ALOCA:
mov 20h, #005h
mov 21h, #007h
mov 22h, #009h
mov 23h, #004h
mov 24h, #002h
mov 25h, #001h
mov 26h, #008h
mov 27h, #006h
mov 28h, #003h
mov r0, #20h
mov r1, #20h
mov r2, #7

COMPARACAO:
mov a, 20h
inc r0
subb a, @r0
jc PROX
djnz r2, COMPARACAO
mov 28h, 20h
sjmp $

PROX:
mov 20h, @r0
mov r2, #7
clr c
djnz r2, COMPARACAO
