from socket import *

serverIP = "127.0.0.1" #IP de localhost
serverPort = 8080

serverSocket = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM = "TCP"
serverSocket.bind((serverIP, serverPort))

serverSocket.listen(1)
print("...SERVIDOR DE ARMAZENAMENTO DE STRINGS...")

#Lista das strings enviados pelo cliente
strings = []

while True:
    connectionSocket, addr = serverSocket.accept()
    print("\nCliente {} conectado".format(addr))

    while True:
        #Recebe a mensagem do cliente
        message = connectionSocket.recv(1024).decode()
        split_message = message.split()
        print("\nRecebi a mensagem {} do cliente".format(message))

        #Analisa a mensagem recebida e gera a resposta adequada
        if split_message[0] == "HELLO":
            response = "HELLOBACK"
            connectionSocket.send(response.encode())
            print("\nEnviei {} para o cliente".format(response))
        elif split_message[0] == "SENDSTRING":
            #Salva a string enviada pelo cliente
            strings.append(" ".join(split_message[1:]))
            response = "SENDOK"
            connectionSocket.send(response.encode())
            print("\nEnviei {} para o cliente".format(response))
        elif split_message[0] == "GETSTRINGS":
            #Envia para o cliente a lista de todas as strings salvas
            response = "STRINGSBACK {}".format(", ".join(strings))
            connectionSocket.send(response.encode())
            print("\nEnviei {} para o cliente".format(response))
            break
    connectionSocket.close()
