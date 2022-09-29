
'''
Exemplo de um Servidor TCP Concorrente (Multithread)
 
Artigo: https://www.linkedin.com/pulse/python-sockets-criando-um-servidor-tcp-concorrente-diego/
 
Diego Mendes Rodrigues
'''
 
import socket
import _thread
 
HOST = '127.0.0.1'      # Endereco IP do Servidor
PORT = 5000             # Porta que o Servidor está
 
# Função chamada quando uma nova thread for iniciada
def conectado(con, cliente):
    print('\nCliente conectado:', cliente)
 
    while True:
        # Recebendo as mensagens através da conexão
        msg = con.recv(1024)
        if not msg:
            break
 
        print('\nCliente..:', cliente)
        print('Mensagem.:', msg)
 
    print('\nFinalizando conexao do cliente', cliente)
    con.close()
    _thread.exit()
 
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
 
# Colocando um endereço IP e uma porta no Socket
tcp.bind(orig)
 
# Colocando o Socket em modo passivo
tcp.listen(1)
print('\nServidor TCP concorrente iniciado no IP', HOST, 'na porta', PORT)
 
while True:
    # Aceitando uma nova conexão
    con, cliente = tcp.accept()
    print('\nNova thread iniciada para essa conexão')
 
    # Abrindo uma thread para a conexão
    _thread.start_new_thread(conectado, tuple([con, cliente]))
 
# Fechando a conexão com o Socket
tcp.close()