# Validação de expressão
print('VALIDA EXPRESSÃO:\n')

expressao = input('Digite uma expressão matematica: ')
validacao = []
cont_aberto = 0
cont_fechado = 0

for char in expressao: # Quebra a string armazenando cada char em expressao
    validacao.append(char)

for char in expressao: # Verifica a quantidade de parenteses abertos e fechados
    if char == '(':
        cont_aberto += 1
    elif char == ')':
        cont_fechado += 1

if cont_aberto == cont_fechado: # Se todos os parenteses abertos forem fechados a expressao e valida
    status = 'A expressão é valida!!'
else:
    status = 'A expressão é invalida!!'

print('\nResultado:')
print(status)