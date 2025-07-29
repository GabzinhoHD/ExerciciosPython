# Formatando Valor parte 6
# Validando a entrada de dados
from utilidades.moeda import moeda
from utilidades.dados import dado
print('ANALISE DE VALOR:\n')

preco = dado.leiaDinheiro('Digite um preço: R$')

print('\nResultado:')
moeda.resumo(preco, 80, 35)