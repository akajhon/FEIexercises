from time import sleep

# Definindo Constantes:
c = 3 * 10**8 #Velocidade da luz no vácuo
pi = 3.14159265358979323846 #Valor de pi
verifica = True
unidade = 0
#Interação com o usuário:
print("*********************************************************")
print("***      .-``'.     Calculadora de Ondas    .'''-. ******")
print("***     .`   .`~       Eletromagnéticas      ~`.   '.****")
print("*** _.-'     '._            CF3121           _.'     '-.*")
print("*********************************************************")
sleep(1)
op = input("[+] Para Comprimento de onda digite 'c' e para Frequência digite 'f':  \n")

#Conversão das Unidades:
if op == "c" or op == "C":
    
    print("* Unidades *")
    print("1-Nânometro")
    print("2-Micrometro")
    print("3-Milimetro")
    print("4-Metro")
    print("5-Kilômetro")
    op2 = int(input("[+] Digite a opção da unidade desejada: \n"))
    sleep(1)
    comp = float(input("[+] Digite o valor do comprimento da onda: \n"))
    while verifica == True:
    
        if op2 >= 1 or op2 <= 5:
            if op2 == 1:
                unidade ="Nanometros(nm)"
                comp = comp*10**-9
                comp2 = comp*10**9
                verifica = False
            elif op2 == 2:
                unidade ="Micrometros(um)"
                comp = comp*10**-6
                comp2 = comp*10**6
                verifica = False
            elif op2 == 3:
                unidade ="Milimetro(mm)"
                comp = comp*10**-3
                comp2 = comp*10**3
                verifica = False
            elif op2 == 4:
                unidade = "Metros(m)"
                comp = comp
                comp2 = comp
                verifica = False
            elif op2 == 5:
                unidade = "Kilômetros(Km)"
                comp = comp*10**3
                comp2 = comp*10**-3
                verifica = False
        else:
            print("[!] Opção inválida digite novamente os dados!")
            print("1-Nânometro")
            print("2-Micrometro")
            print("3-Milimetro")
            print("4-Metro")
            print("5-Kilômetro")
            op2 = int(input("[+] Digite a opção da unidade desejada: \n"))
            sleep(1)
            comp = float(input("[+] Digite o valor do comprimento da onda: \n"))
            

elif op == "f" or "F":
    freq = float(input("[+] Digite o valor da frequência da onda: \n"))
    #Fórmulas da Frequência:
    compf = c/freq
    k = 2*pi/compf
    w = 2*pi*freq
    compf2 = compf
    if compf > 10**-1:
        print("Tipo de onda: Ondas de rádio")
        print(f"Com sua frequência de: {freq:0.2e} Hz")
        print(f"Seu comprimento é de: {compf:0.2f} m")
        print(f"Seu k é: {k:0.2e} rad/m")
        print(f"Seu w é: {w:0.2e} rad/s")
    elif compf <= 10*-1 and compf >= 1*10*-3:
        compf2 = compf*10**3
        print("Tipo de onda: Microondas")
        print(f"Com sua frequência de: {freq:0.2e} Hz")
        print(f"Seu comprimento é de: {compf2:0.2f} mm")
        print(f"Seu k é: {k:0.2e} rad/m")
        print(f"Seu w é: {w:0.2e} rad/s")
    elif compf < 1*10*-3 and compf >= 1*10*-6:
        compf2 = compf*10**6
        print("Tipo de onda: Infravermelho")
        print(f"Com sua frequência de: {freq:0.2e} Hz")
        print(f"Seu comprimento é de: {compf2:0.2f} um")
        print(f"Seu k é: {k:0.2e} rad/m")
        print(f"Seu w é: {w:0.2e} rad/s")
    elif compf < 10*-6 and compf >= 10*-8:
        compf2 = compf*10**9
        print("Tipo de onda: Visível e Ultra-violeta")
        print(f"Com sua frequência de: {freq:0.2e} Hz")
        print(f"Seu comprimento é de: {compf2:0.2f} nm")
        print(f"Seu k é: {k:0.2e} rad/m")
        print(f"Seu w é: {w:0.2e} rad/s")
    elif compf <10*-9 and compf >= 10*-11:
        compf2 = compf*10**9
        print("Tipo de onda: Raio-X")
        print(f"Com sua frequência de: {freq:0.2e} Hz")
        print(f"Seu comprimento é de: {compf2:0.2f} nm")
        print(f"Seu k é: {k:0.2e} rad/m")
        print(f"Seu w é: {w:0.2e} rad/s")
    elif compf < 10**-11:
        compf2 = compf*10**6
        print("Tipo de onda: Raio Gama")
        print(f"Com sua frequência de: {freq:0.2e} Hz")
        print(f"Seu comprimento é de: {compf2:0.2f} nm")
        print(f"Seu k é: {k:0.2e} rad/m")
        print(f"Seu w é: {w:0.2e} rad/s")



if op =='c' or op == 'C':
    #Fórmulas do Comprimento:
    f = c/comp
    k = 2*pi/comp
    t = 1/f
    w = 2*pi/t
    
    if f > 0 and f <= 1*10**9:
        print("Tipo de onda: Ondas de rádio")
        print(f"Com seu comprimento de: {comp2:0.2f} {unidade}")
        print(f"Sua frequência é: {f:0.2e}")
        print(f"Seu k é: {k:0.2e} rad/m")
        print(f"Seu w é: {w:0.2e} rad/s")
    elif f>10*9 and f <= 10*11:
        print("Tipo de onda: Microondas")
        print(f"Com seu comprimento de: {comp2:0.2f} {unidade}")
        print(f"Sua frequência é: {f:0.2e}")
        print(f"Seu k é: {k:0.2e} rad/m")
        print(f"Seu w é: {w:0.2e} rad/s")
    elif f>10*11 and f <= 10*14:
        print("Tipo de onda: infravermelho")
        print(f"Com seu comprimento de: {comp2:0.2f} {unidade}")
        print(f"Sua frequência é: {f:0.2e}")
        print(f"Seu k é: {k:0.2e} rad/m")
        print(f"Seu w é: {w:0.2e} rad/s")
    elif f>10*14 and f<= 10*15:
        print("Tipo de onda: Visível")
        print(f"Com seu comprimento de: {comp2:0.2f} {unidade}")
        print(f"Sua frequência é: {f:0.2e}")
        print(f"Seu k é: {k:0.2e} rad/m")
        print(f"Seu w é: {w:0.2e} rad/s")
    elif f>10*15 and f<= 10*16:
        print("Tipo de onda: Ultravioleta")
        print(f"Com seu comprimento de: {comp2:0.2f} {unidade}")
        print(f"Sua frequência é: {f:0.2e}")
        print(f"Seu k é: {k:0.2e} rad/m")
        print(f"Seu w é: {w:0.2e} rad/s")
    elif f>10*16 and f<= 10*19:
        print("Tipo de onda: Raixo-X")
        print(f"Com seu comprimento de: {comp2:0.2f} {unidade}")
        print(f"Sua frequência é: {f:0.2e}")
        print(f"Seu k é: {k:0.2e} rad/m")
        print(f"Seu w é: {w:0.2e} rad/s")
    elif f>10**19:
        print("Tipo de onda: Raio Gama")
        print(f"Com seu comprimento de: {comp2:0.2f} {unidade}")
        print(f"Sua frequência é: {f:0.2e}")
        print(f"Seu k é: {k:0.2e} rad/m")
        print(f"Seu w é: {w:0.2e} rad/s")

