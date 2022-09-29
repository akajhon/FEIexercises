from socket import *
from datetime import datetime
import os
import sys

serverIP = "127.0.0.1"
serverPort = 8080

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))

serverSocket.listen(1)
print("...SERVIDOR DE HORA...")

while True:
    
    connectionSocket, addr = serverSocket.accept()
    pid = os.fork()
    if pid == 0:
        print("Novo Cliente {} conectado".format(addr))
        while True:
            #recebe a mensagem do cliente
            message = connectionSocket.recv(1024).decode()
            split_message = message.split()
            
            #analisa a mensagem recebida e gera a resposta adequada
            if split_message[0] == "HELLO":
                print("Recebi uma mensagem HELLO do cliente {}".format(addr))
                response = "HELLOBACK"
                connectionSocket.send(response.encode())
                print("Enviei HELLOBACK para o cliente")
            elif split_message[0] == "HOUR-PLEASE":
                print("Recebi uma solicitação HOUR-PLEASE")
                date = datetime.now()
                response = "HOUR " + date.strftime("%H:%M:%S")
                connectionSocket.send(response.encode())
                break
        connectionSocket.close()
        print("Encerrando a conexão com o cliente {}".format(addr))
        sys.exit(0)
