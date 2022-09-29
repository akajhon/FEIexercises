from time import sleep

# Definindo Constantes:
c = 3 * (10**8) #Velocidade da luz no vácuo
pi = 3.14159265358979323846 #Valor de pi
verifica = True

#Interação com o usuário:
print("* Bem-Vindo *")
sleep(1)
print("* Calculadora de Ondas Eletromagnéticas *")
sleep(1)
op = input("Para Comprimento de onda digite 'c' e para Frequência digite 'f':  \n")

#Conversão das Unidades:
if op == "c" or op == "C":
    
    print("*** Unidades ***")
    print("1-Nânometro")
    print("2-Micrometro")
    print("3-Milimetro")
    print("4-Metro")
    print("5-Kilômetro")
    op2 = int(input("Digite a opção da unidade desejada: \n"))
    sleep(1)
    comp = int(input("Digite o valor do comprimento da onda: \n"))
    while verifica == True:
    
        if op2 >= 1 or op2 <= 5:
            if op2 == 1:
                unidade ="Nanometros(nm)"
                comp = comp*10**-9
                verifica = False
            elif op2 == 2:
                unidade ="Micrometros(um)"
                comp = comp*10**-6
                verifica = False
            elif op2 == 3:
                unidade ="Milimetro(mm)"
                comp = comp*10**-3
                verifica = False
            elif op2 == 4:
                unidade = "Metros(m)"
                comp = comp
                verifica = False
            elif op2 == 5:
                unidade = "Kilômetros(Km)"
                comp = comp*10**3
                verifica = False
        else:
            print("Opção inválida digite novamente os dados!")
            print("1-Nânometro")
            print("2-Micrometro")
            print("3-Milimetro")
            print("4-Metro")
            print("5-Kilômetro")
            op2 = int(input("Digite a opção da unidade desejada: \n"))
            sleep(1)
            comp = float(input("Digite o valor do comprimento da onda: \n"))
            

elif op == "f" or "F":
    freq = int(input("Digite o valor da frequência da onda: \n"))

if op =='c' or op == 'C':
    #Fórmulas do Comprimento:
    f = c/comp
    k = 2*pi/comp
    t = 1/f
    w = 2*pi/t
    

    print("Com seu comprimento de:", comp,unidade)
    print("Sua frequência é:" , f ,"Hz")
    print("Seu k é:" , k ,"rad/m")
    print("Seu w é:" , w ,"rad/s")
    

    


elif op == 'f' or op == 'F':
    #Fórmulas da Frequência:
    compf = freq/c
    k = 2*pi/compf
    w = 2*pi*freq

    print("Com sua frequência de: " , freq ,"Hz")
    print("Seu comprimento é de: ", compf, unidade)
    print("Seu k é: " , k ,"rad/m")
    print("Seu w é: " , w ,"rad/s")