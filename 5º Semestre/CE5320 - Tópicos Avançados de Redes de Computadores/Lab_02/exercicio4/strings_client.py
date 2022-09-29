from socket import *

#Protocolo
#Mensagem HELLO: usada pelo cliente para se identificar ao servidor
#Mensagem HELLOBACK: resposta do servidor para o HELLO

#Mensagem SENDSTRING <STRING>: envia uma string para o servidor salvar
#Mensagem SENDOK: resposta de sucesso do servidor para o SENDSTRING
#Mensagem GETSTRINGS: solicita ao servidor as strings salvas
#Mensagem STRINGSBACK: respota do servidor para o GETSTRINGS

serverIP = "127.0.0.1"  # IP de localhost
serverPort = 8080

connected = False
clientSocket = socket(AF_INET, SOCK_STREAM)  # SOCK_STREAM = "TCP"
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
        print("\nRecebi a mensagem {} do servidor\n".format(response))
        connected = True

    if connected == True:
        if split_response and split_response[0] == "SENDOK":
            print("\nRecebi a mensagem {} do servidor\nA string foi armazenada com sucesso!\n".format(response))

        if split_response and (split_response[0] == "SENDOK" or split_response[0] == "HELLOBACK"):
            operation = int(input("Escolha uma operação:\n1-Enviar uma string\n2-Consultar strings armazenadas\n"))
            #Define a mensagem de solicitação de acordo com a operação escolhida
            if operation == 1:
                input_string = input("Digite a string a ser enviada: ")
                message = "SENDSTRING " + input_string
            elif operation == 2:
                message = "GETSTRINGS"
            clientSocket.send(message.encode())
            print("\nMensagem enviada ao servidor: {}".format(message))
        
        if split_response and split_response[0] == "STRINGSBACK":
            print("\nRecebi a mensagem {} do servidor\n".format(split_response[0]))
            print("\nStrings armazenadas no servidor: {}".format(" ".join(split_response[1:])))
            break
