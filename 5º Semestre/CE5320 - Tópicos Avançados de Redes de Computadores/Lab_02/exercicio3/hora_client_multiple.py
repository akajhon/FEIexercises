from socket import *

#Protocolo
#Mensagem HELLO: usada pelo cliente para se identificar ao servidor
#Mensagem HELLOBACK: resposta do servidor para o HELLO
#Mensagem HOUR-PLEASE: usada pelo cliente para solicitar a hora
#Mensagem HOUR <date>: resposta do servidor para a HOUR-PLEASE, onde date é um objeto contendo a hora

serverIP = "127.0.0.1" #IP de localhost
serverPort = 8080

clientSocket = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM = "TCP"
clientSocket.connect((serverIP, serverPort))

message = "HELLO"
clientSocket.send(message.encode())
print("Conectado ao Servidor")

while True:
    #recebe a resposta do servidor
    response = clientSocket.recv(1024).decode()
    split_response = response.split()

    #verifico qual mensagem foi recebida como resposta
    if split_response and split_response[0] == "HELLOBACK":
        message = "HOUR-PLEASE"
        clientSocket.send(message.encode())
    elif split_response and split_response[0] == "HOUR":
        print("The hour is {}".format(split_response[1]))
        break
print("Cliente Desconectado do Servidor!")
