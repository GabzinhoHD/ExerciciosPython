# Formatando Valor parte 4
# Reduzindo ainda mais o codigo
import moeda
print('ANALISE DE VALOR:\n')

preco = float(input('Digite o preço: R$'))

print('\nResultado:')
moeda.resumo(preco, 80, 35)