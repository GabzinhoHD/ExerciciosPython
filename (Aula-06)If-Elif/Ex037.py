# Conversão de bases
print('CONVERTOR DE BASES:\n')

num = int(input('Digite um numero para converter: '))

print('='*36)
print('Menu:')
print('| [1] para converter para binario')
print('| [2] para converter para octal')
print('| [3] para converte para hexadecimal')
print('='*36)

opcao = int(input('Digite para qual quer converter: '))

print('\nResultado:')
if opcao == 1:
    binario = bin(num) [2:] # Remove o prefixo(0b)
    print(f'{num} em binario é: {binario}')

elif opcao == 2:
    octal = oct(num) [2:] # Remove o prefixo(0o)
    print(f'{num} em octal é: {octal}')

elif opcao == 3:
    hex = hex(num) [2:] # Remove o prefixo(0x)
    print(f'{num} em hexadecimal é: {hex}')

else:
    print('Sua escolha e invalida!!')