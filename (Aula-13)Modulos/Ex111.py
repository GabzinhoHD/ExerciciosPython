# Formatando Valor parte 5
# Importando um modulo dentro de um pacote
from utilidades.moeda import moeda
print('ANALISE DE VALOR:\n')

preco = float(input('Digite o preço: R$'))

print('\nResultado:')
moeda.resumo(preco, 80, 35)