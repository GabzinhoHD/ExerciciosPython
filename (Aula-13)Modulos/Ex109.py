# Formatando Valor parte 3
import moeda
print('ANALISE DE VALOR:\n')

preco = float(input('Digite o preço: R$'))

print('\nResultado:')
print(f'A metade de {preco} é: {moeda.metade(preco, False)}')
print(f'O dobro de { preco} é : {moeda.dobro(preco, True)}')
print(f'Aumentando 10%: {moeda.aumento(preco, 10)}')
print(f'Diminuindo 13%: {moeda.diminuir(preco, 13, True)}')