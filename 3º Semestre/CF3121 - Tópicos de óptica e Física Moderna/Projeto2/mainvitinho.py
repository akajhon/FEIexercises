#Constantes
hEV = 4.136e-15
hJ = 6.626E-34
c = 2998e+05
cElementar = 1.602e-19
cR = 1.0974e7
massaEletron = 9.11e-31
e0 = 8.85e-12

#*****Zona de Funções*****
def calculaEnergiaComp(comp):
    energia = (hEV*c)/comp #Calcula o Valor da energia com o comprimento
    return energia #Retorna a conta executada na função

def calculaEnergiaFreq(freq):
    energia = hEV * freq #Calcula o Valor da energia com a Frequência
    return energia #Retorna a conta executada na função

def calculaRaio(n):
    raio = (pow(n,2)) * 5.29e-11 #Calcula o Valor do Raio com a n
    raio *= 1e9
    return raio #Retorna a conta executada na função

def calculaVel(n):
  # 1/e0 * (cargaElementar^2 / (2*n*hEV))
    vel = (1/e0) * ((pow(cElementar,2)) / (2*n*hJ))
  #vel = (1/e0) * (pow(cElementar,2) / (2*n*hEV)) #Calcula o Valor do Raio com base no n
    return vel #Retorna a conta executada na função

def calculaEnergiaCinetica(n):
    energiaCinetica = (13.6) / pow(n,2) #Calcula o Valor da energia Cinetica com base no valor de n
    return energiaCinetica #Retorna a conta executada na função

def calculaEnergiaPotencial(n):
    energiaPotencial = (-27.2) / pow(n,2) #Calcula o Valor da energia Potencial com base no valor de n
    return energiaPotencial #Retorna a conta executada na função

def calculaEnergiaTotal(n):
    energiaTotal = (calculaEnergiaPotencial(n) + calculaEnergiaCinetica(n)) #Calcula o Valor da energia Total com base no valor de n
    return energiaTotal #Retorna a conta executada na função

def calculaCompOnda(n):
    velocidade = calculaVel(n)
    compOnda = hJ / (massaEletron * velocidade)
    compOnda *= 1e+9
    return compOnda # Retorna a conta executada na função

#Função para calcular Energia de N final e inicial, Energia do foton, Comprimento do foton,
#frequência do foton e comprimento do foton.
def calculaFoton(nInicial,nFinal): 
    energiaNInicial = (-13.6) / pow(nInicial,2) 
    energiaNFinal = (-13.6) / pow(nFinal,2)
    energiaFoton = abs(energiaNFinal - energiaNInicial)
    compFoton = (hEV * c) / energiaFoton
    freqFoton = energiaFoton / hEV
    compFoton *= 1e+9
    return compFoton, freqFoton

# calcular tipo de onda utilizando frequência
def calc_tipo_onda(freq):
    tipo_onda = ""
    if(freq < 1e+09):
        tipo_onda = "radio"
    elif(freq >= 1e+09 and freq <= 3e+11):
        tipo_onda = "microondas"
    elif(freq > 3e+11 and freq <= 4.29e+14):
        tipo_onda = "infravermelho"
    elif(freq > 4.29e+14 and freq <= 7.5e+14):
        tipo_onda = "luz visivel"
    elif(freq > 7.5e+14 and freq <= 1e+16):
        tipo_onda = "ultravioleta"
    elif(freq > 1e+16 and freq <= 1e+19):
        tipo_onda = "raio-x"
    elif(freq > 1e+19):
        tipo_onda = "raio gama"
    return tipo_onda

#Analisa a cor partindo da comparação do Comprimento do Foton
def calculaBalmer(compFoton):
    corLuz = ""
    if(compFoton >= 410.2 and compFoton < 434.1):
        corLuz = "violeta"
    elif(compFoton >= 434.1 and compFoton < 486.1):
        corLuz = "azul"
    elif(compFoton >= 486.1 and compFoton < 656.3):
        corLuz = "verde"
    elif(compFoton > 656.3):
        corLuz = "vermelha"
    return corLuz

#*****Término da Zona de Funções*****
while True:
    entrada = int(input("\n====================================\nEscolha uma das opções:\n1 - Entrar com o comprimento de onda\n2 - Entrar com a frequência\n3 - Entrar com o número quântico\n4 - Entrar com o número quântico inical e final\n5 - Entrar com o número quântico final\n0 - Sair\n====================================\n:"))# Printa na tela o Menu
    if(entrada == 1):
    #Comprimento
        comp = float(input("\nDigite o comprimento de onda: "))
        result = calculaEnergiaComp(comp)#Salva na variavel result o retorno da função calculaEnergiaComp(comp)
        print("\nValor da energia: %.2f eV\n" % result)#Printa o valor da energia caculado com o comprimento Formatado 

    elif(entrada == 2):
    #Frequência
        freq = -1
        while(freq < 0.0):
            freq = float(input("\nDigite a frequência: "))
            if(freq < 0.0):
                print("\nErro, a freqência não pode ser negativa")
            
        resultado = calculaEnergiaFreq(freq) #Salva na variavel resultado o retorno da função calculaEnergiaFreq(freq)
        print("\nValor da energia: %.2f eV" % resultado) #Printa o valor da energia caculado com a frequência Formatado 

    elif(entrada == 3):
    #Nível Quantico
        n = 0
        while(n < 1):
            n = int(input("\nDigite o n: "))#Espera uma entrada para o valor de N
            if(n < 1):
                print("\nErro, o n não pode ser menor que 1")#Mensagem de erro ao digitar o número 

        resultado = calculaRaio(n) #Salva na variavel resultado o retorno da função calculaRaio(n)
        print("\nValor do Raio: %.2f nm" % resultado)#Printa o valor da Raio Formatado em notação cientifica

        resultadoVel = calculaVel(n) #Salva na variavel resultadoVel o retorno da função calculaVel(n)
        print("Valor da Velocidade:", f'{resultadoVel:.2e}', end=" m/s\n")#Printa o valor da Velocidade Formatado em notação cientifica

        resultadoCinetica = calculaEnergiaCinetica(n) #Salva na variavel resultadoCinetica o retorno da função calculaEnergiaCinetica(n)
        print("Valor da Energia Cinética: %.2f eV" % resultadoCinetica)#Printa o valor da Energia Cinética Formatado em notação cientifica

        resultadoPotencial = calculaEnergiaPotencial(n) #Salva na variavel resultadoPotencial o retorno da função calculaEnergiaPotencial(n)
        print("Valor da Energia Potencial: %.2f eV" % resultadoPotencial)#Printa o valor da Energia Potencial Formatado em notação cientifica

        resultadoTotal = calculaEnergiaTotal(n) #Salva na variavel resultadoTotal o retorno da função calculaEnergiaTotal(n)
        print("Valor da Energia total: %.2f eV" % resultadoTotal) #Printa o valor da energia total Formatado em notação cientifica

        resultadoCompOnda = calculaCompOnda(n) #Salva na variavel resultadoCompOnda o retorno da função calculaCompOnda(n)
        print("Valor do Comprimento de Onda: %.2f nm" % resultadoCompOnda) #Printa o valor do Comprimento de Onda Formatado em notação cientifica
    
    elif(entrada == 4):
        nInicial = 0
        nFinal = 0
        #Verifica o número de nInicial e nFinal
        while(nInicial < 1):
            nInicial = int(input("\nDigite o n inicial: "))
            if(nInicial < 1):
                print("\nErro, o n inicial não pode ser menor que 1")
        while(nFinal < 1):
            nFinal = int(input("\nDigite o n final: "))
            if(nFinal < 1):  
                print("\nErro, o n final não pode ser menor que 1")

        if(nInicial == nFinal):
            print("\nErro, os valores de n inicial e n final não podem ser iguais.")
        # elétron sobe de um nível inferior para um nível superior    
        elif(nInicial < nFinal):
            compFoton, freqFoton = calculaFoton(nInicial,nFinal)
            tipo_onda = calc_tipo_onda(freqFoton)
            print("\nUm fóton do tipo %s foi absorvido" % tipo_onda)#Nas linhas 153 até a 156 elas printam no terminal os devidos resultados
            print("Valor do comprimento de onda do fóton: %.2f nm" % compFoton)
            print("Valor da frequência do fóton", f'{freqFoton:.2e}', end=" Hz\n" )
        # elétron decai de um nível superior para um nível inferior    
        elif(nFinal < nInicial):
            compFoton, freqFoton = calculaFoton(nInicial,nFinal)#Nas linhas 160 e 161 salvam em uma variavel auxiliar o retorno da função
            tipo_onda = calc_tipo_onda(freqFoton)
            print("\nUm fóton do tipo %s foi emitido" % tipo_onda)#Nas linhas 161 até a 163 elas printam no terminal os devidos resultados
            print("Valor do comprimento de onda do fóton: %.2f nm" % compFoton)
            print("Valor da frequência do fóton", f'{freqFoton:.2e}', end=" Hz\n" )

    elif(entrada == 5):
        nInicial = 0
        # n inicial deve ser pelo menos 2, pois nesse caso ele pode decair para n = 1
        while(nInicial < 2):
            nInicial = int(input("\nDigite o n inicial: "))
            if(nInicial < 2):
                print("\nErro, o n inicial deve ser no mínimo 2")
            
        serie = 0
        while True:
            serie = int(input("\nEscolha uma das opções de série abaixo\n1 - Série de Lyman\n2 - Série de Balmer\n3 - Série de Paschen\n4 - Série de Brackett\n5 - Série de Pfund\n:"))
            if(serie != 1 and serie != 2 and serie != 3 and serie != 4 and serie != 5):
                print("\nErro, escolha uma das opções válidas")
            # a série escolhida não pode ser maior ou igual que o n inicial
            elif(serie >= nInicial):
                print("\nErro, a série escolhida não pode ser maior ou igual ao n inicial")
            else:
                break
            
        # caso seja a série de Lyman, Paschen, Brackett ou Pfund   
        if(serie == 1 or serie == 3 or serie == 4 or serie == 5):
            compFoton, freqFoton = calculaFoton(nInicial,serie)#Nas linhas 187 e 188 salvam em uma variavel auxiliar o retorno da função
            tipo_onda = calc_tipo_onda(freqFoton)
            print("\nUm fóton do tipo %s foi emitido" % tipo_onda)#Nas linhas 189 até a 191 elas printam no terminal os devidos resultados
            print("Valor do comprimento de onda do fóton: %.2f nm" % compFoton)
            print("Valor da frequência do fóton", f'{freqFoton:.2e}', end=" Hz\n" )
        # caso seja a série de Balmer
        else:
            compFoton, freqFoton = calculaFoton(nInicial,serie)
            if(compFoton >= 410.2):
                corLuz = calculaBalmer(compFoton)
                print("\nUm fóton do tipo luz visível da cor %s foi emitido" % corLuz)
            # caso o comprimento seja menor que 410.2, não é luz visível
            else:
                tipo_onda = calc_tipo_onda(freqFoton)
                print("\nUm fóton do tipo %s foi emitido" % tipo_onda)
                
            print("Valor do comprimento de onda do fóton: %.2f nm" % compFoton)
            print("Valor da frequência do fóton", f'{freqFoton:.2e}', end=" Hz\n" )

    elif(entrada == 0):
        print("\nPrograma encerrado...")
        break
        
    else:
        print("\nErro, insira uma das opções válidas")
