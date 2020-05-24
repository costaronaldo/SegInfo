# retirado de https://pt.stackoverflow.com/questions/329748/python-cifra-de-c%C3%A9sar-strings

def recebeModo():
    while True:
        option = input("Deseja criptografar ou descriptografar?[c/d] ")
        option = option.lower()
        if option == 'c' or option == 'criptografar' or option == 'descriptografar' or option == 'd':
            return option
        print("Entrada inválida. Escolha entre ('criptografar', 'c') ou ('descriptografar', 'd')")


def recebeChave():
    chave = 1
    entrada_valida = False
    while not entrada_valida:
        chave = int(input("Digite o valor da chave: "))
        if 1 <= chave <= 26:
            entrada_valida = True
        else:
            print("ERRO: Entrada inválida para a chave (1 a 26)")
    return chave


def encripta(modo, mensagem, chave):
    cripto = ''
    for i in mensagem:
        if 'A' <= i <= 'Z':
            if ord(i) + chave > ord('Z'):
                cripto += chr((ord('A') + chave - (ord('Z') + 1 - ord(i))))
            else:
                cripto += chr(ord(i) + chave)
        elif 'a' <= i <= 'z':
            if ord(i) + chave > ord('z'):
                cripto += chr((ord('a') + chave - (ord('z') + 1 - ord(i))))
            else:
                cripto += chr(ord(i) + chave)
        else:
            cripto += i
    return cripto


def decripta(modo, mensagem, chave):
    cripto = ''
    for i in mensagem:
        if 'A' <= i <= 'Z':
            if ord(i) - chave < ord('A'):
                cripto += chr(ord('Z') - (chave - (ord(i) + 1 - ord('A'))))
            else:
                cripto += chr(ord(i) - chave)
        elif 'a' <= i <= 'z':
            if ord(i) - chave < ord('a'):
                cripto += chr(ord('z') - (chave - (ord(i) + 1 - ord('a'))))
            else:
                cripto += chr(ord(i) - chave)
        else:
            cripto += i
    return cripto


def geraMsgTraduzida(modo, mensagem, chave):
    nova_mensagem = ''
    if modo == 'c' or modo == 'criptografar':
        nova_mensagem = encripta(modo, mensagem, chave)
    elif modo == 'd' or modo == 'descriptografar':
        nova_mensagem = decripta(modo, mensagem, chave)
    return nova_mensagem


def main():
    modo = recebeModo()
    chave = recebeChave()
    mensagem = input("Digite a mensagem: ")
    print(geraMsgTraduzida(modo, mensagem, chave))


main()