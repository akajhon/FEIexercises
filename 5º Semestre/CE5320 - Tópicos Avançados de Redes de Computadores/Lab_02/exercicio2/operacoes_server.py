from socket import *

serverIP = "127.0.0.1" #IP de localhost
serverPort = 8080

serverSocket = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM = "TCP"
serverSocket.bind((serverIP, serverPort))

serverSocket.listen(1)
print("...SERVIDOR DE OPERAÇÕES ARITMÉTICAS...")

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Cliente {} conectado".format(addr))

    while True:
        #Recebe a mensagem do cliente
        message = connectionSocket.recv(1024).decode()
        split_message = message.split()
        print("Recebi a mensagem {} do cliente".format(message))

        #Analisa a mensagem recebida e gera a resposta adequada
        if split_message[0] == "HELLO":
            response = "HELLOBACK"
            connectionSocket.send(response.encode())
            print("Enviei {} para o cliente".format(response))
        elif split_message[0] == "ADDITION":
            result = int(split_message[1]) + int(split_message[2])
            response = "RESULT {}".format(result)
            connectionSocket.send(response.encode())
            print("Enviei {} para o cliente".format(response))
            break
        elif split_message[0] == "SUBTRACTION":
            result = int(split_message[1]) - int(split_message[2])
            response = "RESULT {}".format(result)
            connectionSocket.send(response.encode())
            print("Enviei {} para o cliente".format(response))
            break
        elif split_message[0] == "MULTIPLICATION":
            result = int(split_message[1]) * int(split_message[2])
            response = "RESULT {}".format(result)
            connectionSocket.send(response.encode())
            print("Enviei {} para o cliente".format(response))
            break
        elif split_message[0] == "DIVISION":
            result = int(split_message[1]) / int(split_message[2])
            response = "RESULT {}".format(result)
            connectionSocket.send(response.encode())
            print("Enviei {} para o cliente".format(response))
            break
    connectionSocket.close()
