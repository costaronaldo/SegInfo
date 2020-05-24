import socket

HOST = input(str("Insira o endereço IP do servidor: "))  # Endereço IP do servidor
PORT = 5000                                              # Porta que o servidor está

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print ('\nPara sair use CTRL+X e Enter\n')

mensagem = input("Digite sua mensagem: ")

while mensagem != "\x18":
    tcp.sendall(bytes(mensagem, 'utf-8'))
    mensagem = input("Digite sua mensagem: ")
tcp.close()