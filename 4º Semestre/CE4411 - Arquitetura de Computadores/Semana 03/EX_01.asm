MOV P1, #0FEh
VOLTAR:
MOV A, P1
RR A
MOV P1, A
AJMP VOLTAR