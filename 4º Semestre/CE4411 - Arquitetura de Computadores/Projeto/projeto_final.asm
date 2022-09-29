;--------- SISTEMA DE DESBLOQUEIO DE AUTOMÓVEIS ---------;
;------- Vitor martins oliveira / R.A:22.120.067-8 ------;
;------ João Pedro Rosa Cezarino / R.A: 22.120.021-5 ----;
;--------------------------------------------------------;


;------------ MAPEAMENTO DE HARDWARE -------------;
RS EQU P1.3
E  EQU P1.2
;-------------------------------------------------;

ORG 0000H
MAIN:		
	CLR RS		   		

	CALL SETAR		
	
	CALL CONEXAO		
			
	CALL MODOENTRADA		

	SETB RS				
			
	MOV DPTR,#INPUT		

DENOVO:
	CLR A
	MOVC A,@A+DPTR		
	JZ PROXIMA				
	CALL ENVIA		
	INC DPTR			
	JMP DENOVO	
			
PROXIMA:
	MOV R4,#00H			
	MOV R5,#00H			
	MOV DPTR,#PASSWORD 

REPETIR:	
  	CALL ESCANEIA		
	SETB RS				
	CLR A
	MOV A,#'$'
	CALL ENVIA		

	CLR A
	MOVC A,@A+DPTR		
	CALL VERIFICAENTRADA		
	INC DPTR
	INC R4
	CJNE R4,#04H,REPETIR	
	CJNE R5,#04H,ERRADO	

;------------------------ SENHA CERTA ------------------------------; 	
CERTO:
	CALL CURSORPOS  	
	SETB RS				
	CALL PERMITIDO
	JMP TERMINA
	
;------------------------ SENHA ERRADA ------------------------------; 	
ERRADO:
 	CALL CURSORPOS  	
	SETB RS				
	CALL NEGADO
	
TERMINA:	
	JMP $
	
SETAR:
	CLR  P1.7		
	CLR  P1.6		
	SETB P1.5		
	CLR  P1.4		
	
	CALL PISCA

	CALL DELAY		

	CALL PISCA
							
	SETB P1.7		
	CLR  P1.6
	CLR  P1.5
	CLR  P1.4
			
	CALL PISCA
	
	CALL DELAY
	RET

CONEXAO:
	CLR P1.7		
	CLR P1.6		
	CLR P1.5		
	CLR P1.4		

	CALL PISCA

	SETB P1.7		
	SETB P1.6		
	SETB P1.5		
	SETB P1.4		
	CALL PISCA

	CALL DELAY		
	RET

MODOENTRADA:
	CLR P1.7		
	CLR P1.6		
	CLR P1.5		
	CLR P1.4		

	CALL PISCA

	CLR  P1.7		
	SETB P1.6		
	SETB P1.5		
	CLR  P1.4		
 
	CALL PISCA

	CALL DELAY		
	RET

PISCA:
	SETB E		
	CLR  E		
	RET

ENVIA:
	MOV C, ACC.7		
	MOV P1.7, C			
	MOV C, ACC.6		
	MOV P1.6, C			
	MOV C, ACC.5		
	MOV P1.5, C			
	MOV C, ACC.4		
	MOV P1.4, C			
			
	CALL PISCA

	MOV C, ACC.3		
	MOV P1.7, C			
	MOV C, ACC.2		
	MOV P1.6, C			
	MOV C, ACC.1		
	MOV P1.5, C			
	MOV C, ACC.0		
	MOV P1.4, C			

	CALL PISCA

	CALL DELAY			
			
	MOV R1,#55H
	RET
	
;----------------- MAPEANDO O KEYPAD -------------------------;	
	
ESCANEIA:
	CLR P0.3			
	CALL IDTECLA0		
	SETB P0.3			
	JB F0,FEITO  		
								
	CLR P0.2			
	CALL IDTECLA1		
	SETB P0.2			
	JB F0,FEITO		 	
		
	CLR P0.1			
	CALL IDTECLA2		
	SETB P0.1			
	JB F0,FEITO			
		
	CLR P0.0			
	CALL IDTECLA3		
	SETB P0.0			
	JB F0,FEITO			
														
	JMP ESCANEIA		
							
FEITO:
	CLR F0		        
	RET

IDTECLA0:
	JNB P0.4, TECLA03	
	JNB P0.5, TECLA02	
	JNB P0.6, TECLA01	
	RET					

TECLA03:	
  	SETB F0			
	MOV R7,#'3'		
	RET				

TECLA02:
	SETB F0			
	MOV R7,#'2'		
	RET			
TECLA01:
	SETB F0			
	MOV R7,#'1'		
	RET				

IDTECLA1:
	JNB P0.4, TECLA06	
	JNB P0.5, TECLA05	
	JNB P0.6, TECLA04	
	RET			
	
TECLA06:
	SETB F0			
	MOV R7,#'6'	
	RET				

TECLA05:
	SETB F0			
	MOV R7,#'5'		
	RET				

TECLA04:
	SETB F0			
	MOV R7,#'4'		
	RET				

IDTECLA2:
	JNB P0.4, TECLA09	
	JNB P0.5, TECLA08	
	JNB P0.6, TECLA07	
	RET					

TECLA09:
	SETB F0			
	MOV R7,#'9'		
	RET				

TECLA08:
	SETB F0			
	MOV R7,#'8'		
	RET				

TECLA07:
	SETB F0			
	MOV R7,#'7'		
	RET				

IDTECLA3:
	JNB P0.4, TECLAHASHTAG	
	JNB P0.5, TECLA00	
	JNB P0.6, TECLAAST	
	RET					

TECLAHASHTAG:
	SETB F0			
	MOV R7,#'#'		
	RET				

TECLA00:
	SETB F0			
	MOV R7,#'0'		
	RET				

TECLAAST:
	SETB F0			
	MOV R7,#'*'	   	
	RET	
;-------------------------------------------------------------;	
	
VERIFICAENTRADA:	
	CJNE A,07H,SAIDA	
	INC R5

SAIDA:					
	RET

CURSORPOS:
	CLR RS
	SETB P1.7		
	SETB P1.6		
	CLR P1.5		
	CLR P1.4		
							
	CALL PISCA

	CLR P1.7		
	CLR P1.6		
	CLR P1.5		
	CLR P1.4		
							
	CALL PISCA

	CALL DELAY		
	RET		


DELAY:
	MOV R0, #50
	DJNZ R0, $
	RET

PERMITIDO:
	MOV DPTR,#ACSLDO
	CLR P3.0
				
VOLTAR:		
	CLR A
	MOVC A,@A+DPTR
	JZ COMECO
	CALL ENVIA
	INC DPTR
	JMP VOLTAR	
		
COMECO:		
	RET	
	
NEGADO:
	MOV DPTR,#ACSNDO	
	CLR P1.0
	
OUTRAVEZ:	
	CLR A
	MOVC A,@A+DPTR
	JZ VOLTACOMECO
	CALL ENVIA
	INC DPTR	
	JMP OUTRAVEZ
	
VOLTACOMECO:	
	RET					

;-------------------------- ARMAZENANDO AS STRINGS -----------------------------------;
ORG 0200H
INPUT: DB 'S', 'E', 'N', 'H', 'A', ':',0
ACSLDO: DB 'A', 'C', 'E', 'S', 'S', 'O', ' ', 'L', 'I', 'B', 'E', 'R', 'A', 'D', 'O', 0
ACSNDO:	DB 'A', 'C', 'E', 'S', 'S', 'O', ' ', 'N', 'E', 'G', 'A', 'D', 'O', 0

;--------------------------- SENHA ---------------------------------------------------;
ORG 0240H		
PASSWORD: DB '9', '8', '7', '6',0

PARA:
	JMP $	

END

