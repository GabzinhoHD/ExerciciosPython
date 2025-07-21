# Gerenciador de Pagamentos
print('PAGAMENTO:\n')

preco = float(input('Qual o preço do produto: '))
print('\n' + ('=' * 49))
print('Forma de Pagamento:')
print('| [1] pagar á vista no dinheiro: 10% de deconto')
print('| [2] pagar á vista no cartão: 5% de desconto')
print('| [3] pagar em 2x no cartão: preço normal')
print('| [4] pagar em 3x ou mais no cartão: 20% de juros')
print('=' * 49)

opcao = int(input('Digite a opção de pagamento: '))

if opcao == 1:
    preco = preco * 0.9

elif opcao == 2:
    preco = preco * 0.95

elif opcao == 4:
    preco = preco * 1.2

print('\nResultado:')
print(f'O valor final do produto será: R${preco:.2f}')
