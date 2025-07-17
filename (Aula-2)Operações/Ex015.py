# Culculando o Preço de um carro alugado

print('CALCULO DE PREÇO DO ALUGUEL: \n|Dia = R$60 \n|Km = R$0.15\n')

dias = int(input('Informe quantos dias o veiculo foi alugado: '))
km = float(input('Informe quantos Km o carro percorrreu: '))

valor_dias = dias * 60
valor_km = km * 0.15
valor_final = valor_dias + valor_km

print('\nResultado:')
print(f'Preço po dias alugados: R${valor_dias:.2f}')
print(f'Preço por Km percorrido: R${valor_km:.2f}')
print(f'Preço Final do Alugeul: R${valor_final:.2f}')