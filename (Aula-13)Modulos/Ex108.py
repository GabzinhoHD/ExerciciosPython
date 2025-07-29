# Formatando Valor parte 2
import moeda
print('ANALISE DE VALOR:\n')

preco = float(input('Digite o preço: R$'))

print('\nResultado:')
print(f'A metade de {preco} é: {moeda.formatar(moeda.metade(preco))}')
print(f'O dobro de { preco} é : {moeda.formatar(moeda.dobro(preco))}')
print(f'Aumentando 10%: {moeda.formatar(moeda.aumento(preco, 10))}')
print(f'Diminuindo 13%: {moeda.formatar(moeda.diminuir(preco, 13))}')