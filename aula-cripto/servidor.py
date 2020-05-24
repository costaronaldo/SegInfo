import socket

HOST = input(str("Insira o endereço IP: "))  # Endereço IP do servidor
PORT = 5000                                  # Porta que o servidor está

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    print('\nAguardando conexão com o cliente...\n')
    
    con, cliente = tcp.accept()
    print ('Conectado por', cliente, '\n')
    
    while True:
        msg = con.recv(1024).decode("utf-8", "ignore")
        if not msg: break
        print ('Mensagem do cliente', cliente, '->', msg)
    print ('Finalizando conexão do cliente', cliente)
    con.close()