# Aprovando Emprestimo
print('EMPRESTIMO:\n')

valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salario: '))
anos = int(input('Informe em quantos anos ira pagar: '))

prestacao = valor_casa / (anos * 12)

print('\nResultado:')
print(f'A prestação será de {prestacao:.2f}')


if prestacao >= (salario * 0.3):
    print(f'Com o seu salario de R${salario:.2f} se torna inviavel pagar essa prestação!!')
    print('EMPRESTIMO NEGADO!!')

else: 
    print('EMPRESTIMO CONCEDIDO!!')

# E no fim nem usei ELIF kkkk