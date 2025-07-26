# Situação aluno
print('SITUAÇÃO DO ALUNO:\n')

aluno = {}

aluno["Nome"] = input('Qual o nome do aluno: ')
aluno["Media"] = float(input(f'Infome a media de {aluno["Nome"]}: '))

if aluno["Media"] > 7:
    aluno["Situação"] = 'Aprovado'

else:
    aluno["Situação"] = 'Reprovado'

print('\nResultado:')
for k , v in aluno.items():
    print(f'{k}: {v}')