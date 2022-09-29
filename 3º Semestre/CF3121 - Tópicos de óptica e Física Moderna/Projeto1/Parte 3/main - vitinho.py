
# coding: utf-8

# In[ ]:

# funcoes de calculo se a entrada foi com o comprimento
def calc_freq(comp_onda,c):
    freq = c / comp_onda
    return freq

def calc_tipo_onda1(freq):
    tipo_onda1 = ""
    if(freq < 1e+09):
        tipo_onda1 = "radio"
    elif(freq >= 1e+09 and freq <= 3e+11):
        tipo_onda1 = "microondas"
    elif(freq > 3e+11 and freq <= 4.29e+14):
        tipo_onda1 = "infravermelho"
    elif(freq > 4.29e+14 and freq <= 7.5e+14):
        tipo_onda1 = "luz visivel"
    elif(freq > 7.5e+14 and freq <= 1e+16):
        tipo_onda1 = "ultravioleta"
    elif(freq > 1e+16 and freq <= 1e+19):
        tipo_onda1 = "raio-x"
    elif(freq > 1e+19):
        tipo_onda1 = "raio gama"
    return tipo_onda1

def calc_k1(comp_onda,pi):
    k1 = (2 * pi) / comp_onda
    return k1

def calc_w1(freq,pi):
    w1 = 2 * pi * freq
    return w1

# funcoes de calculo se a entrada foi com a frequencia
def calc_comp(frequencia,c):
    comp = c / frequencia
    return comp

def calc_tipo_onda2(comp):
    tipo_onda2 = ""
    if(comp < 3e-11):
        tipo_onda2 = "raio gama"
    elif(comp >= 3e-11 and comp <= 3e-08):
        tipo_onda2 = "raio-x"
    elif(comp > 3e-08 and comp <= 4e-07):
        tipo_onda2 = "ultravioleta"
    elif(comp > 4e-07 and comp <= 7e-07):
        tipo_onda2 = "luz visivel"
    elif(comp > 7e-07 and comp <= 1e-03):
        tipo_onda2 = "infravermelho"
    elif(comp > 1e-03 and comp <= 3e-01):
        tipo_onda2 = "microondas"
    elif(comp > 3e-01):
        tipo_onda2 = "radio"
    return tipo_onda2

def calc_k2(pi,comp):
    k2 = (2 * pi) / comp 
    return k2

def unidade_comp(comp,tipo_onda2):
    uni_comp = 0
    unidade = ""
    if(tipo_onda2 == "radio"):
        uni_comp = comp
        unidade = "m"
    elif(tipo_onda2 == "microondas"):
        uni_comp = comp * 1000
        unidade = "mm"
    elif(tipo_onda2 == "infravermelho"):
        uni_comp = comp * 1e+06
        unidade = "um"
    else:
        uni_comp = comp * 1e+09
        unidade = "nm"
    return uni_comp,unidade

# funções para quando o usuário entrou com a frequência angular
def calc_freq2(freq_ang,pi):
    frequencia = 0
    frequencia = freq_ang / (2*pi)
    return frequencia
# funções para quando o usuário entrou com o número de onda
def calc_comp2(ondaN,pi):
    comp = 2 * pi / ondaN
    return comp
#Função para calcular o Campo Elétrico
def calc_em(Bm,c):
      Em = c * Bm
      return Em
#Função para calcular o Campo Elétrico
def calc_bm(Em,c):
    Bm = Em / c
    return Bm

def main():
    c = 299792458
    pi = 3.14159265358979323846
    while True:
        entrada = int(input("\n==================================\nEscolha uma das opções:\n 0 - Sair\n 1 - Entrar com comprimento de onda\n 2 - Entrar com frequência\n 3 - Entrar com frequência angular\n 4 - Entrar com número de onda\n 5 - Entrar com o campo elétrico \n 6 - Entrar com o campo magnético \n==================================\n"))
        if(entrada == 1):
            unidade = int(input("Escolha uma das opções de unidade\n 1 - nm\n 2 - um\n 3 - mm\n 4 - m\n 5 - km\n:"))
            if(unidade == 1):
                comp_onda = float(input("Entre com o comprimento de onda (em nm): "))
                comp_onda = comp_onda / 1e+09
            elif(unidade == 2):
                comp_onda = float(input("Entre com o comprimento de onda (em um): "))
                comp_onda = comp_onda / 1e+06
            elif(unidade == 3):
                comp_onda = float(input("Entre com o comprimento de onda (em mm): "))
                comp_onda = comp_onda / 1000
            elif(unidade == 4):
                comp_onda = float(input("Entre com o comprimento de onda (em m): "))
            elif(unidade == 5):
                comp_onda = float(input("Entre com o comprimento de onda (em km): "))
                comp_onda = comp_onda * 1000
            else:
                print("\nErro, escolha uma das opções de unidade válidas (1-5)")
                continue
                
            # executando os calculos    
            freq = calc_freq(comp_onda,c)
            tipo_onda1 = calc_tipo_onda1(freq)
            k1 = calc_k1(comp_onda,pi)
            w1 = calc_w1(freq,pi)
            # mostrando os resultados
            print("\n====Resultados exibidos abaixo====")
            print("Frequencia:", end=" ")
            print(f'{freq:.2e}', end=" Hz\n")
            print("k:" , end=" ")
            print(f'{k1:.2e}', end=" rad/m\n")
            print("w:", end=" ")
            print(f'{w1:.2e}', end=" rad/s\n")
            print("Tipo de onda: %s" % tipo_onda1)
            print("==================================")      
        elif(entrada == 2):
            frequencia = float(input("Insira a frequência (em Hz): "))
            # ----------------executando os calculos----------------
            comp = calc_comp(frequencia,c)
            tipo_onda2 = calc_tipo_onda2(comp)
            uni_comp,unidade = unidade_comp(comp,tipo_onda2)
            k2 = calc_k2(pi,comp)
            w2 = calc_w1(frequencia,pi)
            #---------------- mostrando os resultados----------------
            print("\n====Resultados exibidos abaixo====")
            print("Comprimento da onda: %.2f %s" % (uni_comp,unidade))
            print("k:" , end=" ")
            print(f'{k2:.2e}', end=" rad/m\n")
            print("w:", end=" ")
            print(f'{w2:.2e}', end=" rad/s\n")
            print("Tipo de onda: %s" % tipo_onda2)
            print("==================================")

        elif(entrada == 3):
            freq_ang = float(input("Insira a frequência angular (rad/s): "))
            #----------------Chamando as funções----------------
            freq = calc_freq2(freq_ang,pi)
            comp = calc_comp(freq,c)
            tp_onda = calc_tipo_onda1(freq)
            uni_comp,unidade = unidade_comp(comp,tp_onda)
            k3 = calc_k2(pi,comp)
            w1 = calc_w1(freq,pi)
            print("\n=====Resultados exibidos abaixo====")
            print("Frequencia:", f'{freq:.2e}', end=" Hz\n")

            print("Comprimento da onda: %.2f %s" % (uni_comp,unidade))
            print("k:" , f'{k3:.2e}', end=" rad/m\n")
            print("w:" , f'{w1:.2e}', end=" rad/s\n")
            
            print("Tipo de onda: %s" % tp_onda)
            print("==================================")
            
        elif(entrada == 4):
            ondaN = float(input("Insira o número de onda desejado (rad/m): "))
            #----------------Chamando as funções----------------
            comp = calc_comp2(ondaN,pi)
            freq = calc_freq(comp,c)
            w1 = calc_w1(freq,pi)
            tp_onda = calc_tipo_onda1(freq)
            uni_comp,unidade = unidade_comp(comp,tp_onda)
            #----------------Print Na Tela----------------
            print("\n=====Resultados exibidos abaixo====")
            print("Frequencia:", f'{freq:.2e}', end=" Hz\n")

            print("Comprimento da onda: %.2f %s" % (uni_comp,unidade))
            print("k:" , f'{ondaN:.2e}', end=" rad/m\n")
            print("w:" , f'{w1:.2e}', end=" rad/s\n")
           
            print("Tipo de onda: %s" % tp_onda)
            print("==================================")

        elif(entrada == 5):
            #----------------campo elétrico máximo----------------
            campEm = float(input("Insira o valor do campo elétrico máximo (V/m): "))
            #----------------Chamando as funções----------------
            campBm = calc_bm(campEm,c)
            #----------------Print Na Tela----------------
            print("\n=====Resultados exibidos abaixo====")
            print("Campo Magnético Máximo:" , f'{campBm:.2e}', end=" T\n")
            print("==================================")

        elif(entrada == 6):
            #----------------campo magnético máximo----------------
            campBm = float(input("Insira o valor do campo magnético máximo (T): "))
            #----------------Chamando as funções----------------
            campEm = calc_em(campBm,c)
            #----------------Print Na Tela----------------
            print("\n=====Resultados exibidos abaixo====")
            print("Campo Magnético Máximo:" , f'{campEm:.2e}', end=" V/m\n")
            print("==================================")    
           
        elif(entrada == 0):
            print("\nPrograma encerrado")
            break

        else:
            print("\nErro, escolha uma das opções válidas (1-6)")
            continue
        
main()

