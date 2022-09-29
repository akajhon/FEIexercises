from socket import *

#Protocolo
#Mensagem HELLO: usada pelo cliente para se identificar ao servidor
#Mensagem HELLOBACK: resposta do servidor para o HELLO

#Mensagem ADDITION <number1> <number2>: usada pelo cliente para solicitar a soma de dois números
#Mensagem SUBTRACTION <number1> <number2>: usada pelo cliente para solicitar a subtração de dois números
#Mensagem MULTIPLICATION <number1> <number2>: usada pelo cliente para solicitar a multiplicação de dois números
#Mensagem DIVISION <number1> <number2>: usada pelo cliente para solicitar a divisão de dois números
#Mensagem RESULT <value>: resposta do servidor para as requisições de operação aritmética, retorna o resultado da operação

serverIP = "127.0.0.1" #IP de localhost
serverPort = 8080

clientSocket = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM = "TCP"
clientSocket.connect((serverIP, serverPort))

message = "HELLO"
clientSocket.send(message.encode())
print("Mensagem enviada ao servidor: {}".format(message))

while True:
    #Recebe a resposta do servidor
    response = clientSocket.recv(1024).decode()
    split_response = response.split()

    #Analisa a resposta recebida e faz uma solicitação ou exibe o resultado da operação
    if split_response and split_response[0] == "HELLOBACK":
        print("Recebi a mensagem {} do servidor\n".format(response))
        operation = int(input("Escolha uma operação:\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n"))
        number1 = int(input("Digite um número: "))
        number2 = int(input("Digite outro número: "))

        #Define a mensagem de solicitação de acordo com a operação escolhida
        if operation == 1:
            message = "ADDITION"
        elif operation == 2:
            message = "SUBTRACTION"
        elif operation == 3:
            message = "MULTIPLICATION"
        elif operation == 4:
            message = "DIVISION"

        message += " {} {}".format(number1, number2)
        print("\nMensagem enviada ao servidor: {}".format(message))
        clientSocket.send(message.encode())
    elif split_response and split_response[0] == "RESULT":
        print("Recebi a mensagem {} do servidor\n".format(response))
        print("Resultado: {}".format(split_response[1]))
        break
