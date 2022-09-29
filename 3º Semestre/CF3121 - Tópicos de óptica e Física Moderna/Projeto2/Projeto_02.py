
#***** Constantes *****#
constantePlanckEV = 4.136e-15 #Constante de Planck em Eletron-Volts
constantePlanckJ = 6.626e-34 #Constante de Plank em Joule
c = 2998e+05  #Velocidade da luz
cargaElementar = 1.602e-19 #Carga Elementar
constanteRydberg = 1.0974e7 #Constante de Rydberg
massaEletron = 9.11e-31 #Massa do Elétron
constanteEletrica = 8.85e-12 #Constante Eletrica

#***** Funções *****#
def energia_comprimento(comp):
    energia = (constantePlanckEV * c)/ comp #Calcula o Valor da energia com o comprimento
    return energia #Retorna a conta executada na função

def energia_frequencia(freq):
    energia = constantePlanckEV * freq #Calcula o Valor da energia com a Frequência
    return energia #Retorna a conta executada na função

def calcula_raio(n):
    raio = (pow(n, 2)) * 5.29e-11 #Calcula o Valor do Raio com a n
    raio *= 1e9
    return raio #Retorna a conta executada na função

def calcula_velocidade(n):
  # 1/constanteEletrica * (cargaElementar^2 / (2*n*constantePlanckEV))
    velocidade = (1 / constanteEletrica) * ((pow(cargaElementar, 2)) / (2 * n * constantePlanckJ))
  #velocidade = (1/constanteEletrica) * (pow(cargaElementar,2) / (2*n*constantePlanckEV)) #Calcula o Valor do Raio com base no n
    return velocidade #Retorna a conta executada na função

def energia_cinetica(n):
    energiaCinetica = (13.6) / pow(n, 2) #Calcula o Valor da energia Cinetica com base no valor de n
    return energiaCinetica #Retorna a conta executada na função

def energia_potencial(n):
    energiaPotencial = (-27.2) / pow(n, 2) #Calcula o Valor da energia Potencial com base no valor de n
    return energiaPotencial #Retorna a conta executada na função

def calcula_energia_total(n):
    energiaTotal = (energia_potencial(n) + energia_cinetica(n)) #Calcula o Valor da energia Total com base no valor de n
    return energiaTotal #Retorna a conta executada na função

def comprimento_onda(n):
    velocidade = calcula_velocidade(n)
    comprimento = (constantePlanckJ) / (massaEletron * velocidade)
    return comprimento # Retorna a conta executada na função
#***** Fim das Funções *****#

#***** Banner *****#
print("""
    ____   __                  _              ______        __              __        __              
   / __ \ / /_   __  __ _____ (_)_____ _____ / ____/____ _ / /_____ __  __ / /____ _ / /_ ____   _____
  / /_/ // __ \ / / / // ___// // ___// ___// /    / __ `// // ___// / / // // __ `// __// __ \ / ___/
 / ____// / / // /_/ /(__  )/ // /__ (__  )/ /___ / /_/ // // /__ / /_/ // // /_/ // /_ / /_/ // /    
/_/    /_/ /_/ \__, //____//_/ \___//____/ \____/ \__,_//_/ \___/ \__,_//_/ \__,_/ \__/ \____//_/     
              /____/                                                                                     
""")
while True:
    entrada = (input("\n====================================\n***** Escolha uma das opções: *****\n[S] - Sair\n[C] - Entrar com Comprimento de onda\n[F] - Entrar com Frequência\n[Q] - Entrar com Número Quântico\n====================================\n->"))
    if(entrada == "C" or entrada == "c"):
    #Comprimento
        print('[*] ATENÇÃO [*] O Comprimento de onda deve ser inserido em notação científica (ex.: XYZe-9)')
        comp = float(input("\n[+] Entre com o Comprimento de onda: "))
        result = energia_comprimento(comp)#Salva na variavel result o retorno da função energia_comprimento(comp)
        print("\n***** RESULTADOS *****")
        print(f"\n[=] Energia do fóton em Ev: {result : .2f} eV")#Printa o valor da energia caculado com o comprimento Formatado 
        print(f"[=] Energia do fóton em J: {(result * cargaElementar): .2e} J")#Printa o valor da energia caculado com o comprimento Formatado 

    elif(entrada == 'F' or entrada == 'f'):
    #Frequência
        freq = -1
        while(freq < 0.0):
            print('[*] ATENÇÃO [*] A Frequência deve ser inserida em notação científica (ex.: XYZe12)')
            freq = float(input("\n[+] Entre com a Frequência: "))
            if(freq < 0.0):
                print("\n [*] ATENÇÃO [*] A frequência não pode ser negativa !!!")
            
        resultado = energia_frequencia(freq) #Salva na variavel resultado o retorno da função energia_frequencia(freq)
        print("\n***** RESULTADOS *****")
        print(f"\n[=] Energia do fóton em Ev: {resultado : .2f} eV") #Printa o valor da energia caculado com a frequência Formatado
        print(f"[=] Energia do fóton em J: {(resultado * cargaElementar): .2e} J")#Printa o valor da energia caculado com o comprimento Formatado 

    elif(entrada == 'q' or entrada == 'Q'):
    #Nível Quantico
        n = 0
        while(n < 1):
            n = int(input("\n[+] Entre com o valor de 'n': "))#Espera uma entrada para o valor de N
            print("\n***** RESULTADOS *****")
            if(n < 1):
                print("\n[*] ATENÇÃO [*] O valor de 'n' não pode ser menor que 1 !!!")#Mensagem de erro ao digitar o número 

        resultado = calcula_raio(n) #Salva na variavel resultado o retorno da função calcula_raio(n)
        print(f"[=] Raio da órbita do elétron da camada {n}: {resultado : .2e}", end=" nm\n")#Printa o valor da Raio Formatado em notação cientifica

        resultado_velocidade = calcula_velocidade(n) #Salva na variavel resultado_velocidade o retorno da função calcula_velocidade(n)
        print(f"[=] Velocidade do elétron:{resultado_velocidade : .2e}", end=" m/s\n")#Printa o valor da Velocidade Formatado em notação cientifica

        resultado_cinetica = energia_cinetica(n) #Salva na variavel resultado_cinetica o retorno da função energia_cinetica(n)
        print(f"[=] Energia Cinética do elétron: {resultado_cinetica : .2f} eV")#Printa o valor da Energia Cinética Formatado em notação cientifica

        resultado_potencial = energia_potencial(n) #Salva na variavel resultado_potencial o retorno da função energia_potencial(n)
        print(f"[=] Energia Potencial do elétron: {resultado_potencial : .2f} eV")#Printa o valor da Energia Potencial Formatado em notação cientifica

        resultado_Total = calcula_energia_total(n) #Salva na variavel resultado_Total o retorno da função calcula_energia_total(n)
        print(f"[=] Energia total do átomo de hidrogênio quando 'n'= {n}: {resultado_Total : .2e} eV") #Printa o valor da energia total Formatado em notação cientifica

        resultado_Comprimento = comprimento_onda(n) #Salva na variavel resultado_Comprimento o retorno da função comprimento_onda(n)
        resultado_Final = (resultado_Comprimento*(1e+9)) #Converte em nm
        print(f"[=] Comprimento de onda de De Broglie: {resultado_Final:.2e}", end=" nm\n") #Printa o valor do Comprimento de Onda Formatado em notação cientifica

    elif(entrada == 'S' or entrada == 's'):
        print("[*] O programa foi encerrado !!!")
        break

    else:
        print("\n[*] ATENÇÃO [*] Insira uma opção válida!!! ")
#***** FIM *****#
