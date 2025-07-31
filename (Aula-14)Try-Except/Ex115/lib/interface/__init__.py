def linha():
    print('=' * 42)

def titulo(msg):
    linha()
    print(msg.center(42))
    linha()

def leiaInt(msg):
    while True:
        try: 
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO!! Tente novamente com um valor inteiro!\033[m\n')
            continue
        else:
            return n

def menu(lista):
    titulo('SISTEMA DE CADASTRO')
    for i, v in enumerate(lista):
        print(f'{i + 1} -- {v}')
    linha()

    opcao = leiaInt('Opção: ')
    return opcao