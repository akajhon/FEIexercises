from socket import *
import sys

try:
    s = socket(AF_INET, SOCK_STREAM)
    print("Socket criado")
except socket.error as err:
    print("Falha na criação do socket")

port = 80

try:
    host_ip = gethostbyname("www.google.com")
except socket.gaierror:
    print("Nome do domínio não foi resolvido")
    sys.exit()

s.connect((host_ip, port))
print("Socket se conectou com o Google no IP {}".format(host_ip))
