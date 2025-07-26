# Cadastro de um CLT
from datetime import date
print('CADASTRO:\n')
cadastro = {}

cadastro["Nome"] = input('Nome: ')
cadastro["Idade"] =  date.today().year - int(input('Ano de Nascimento: '))
cadastro["CTPS"] = int(input('CTPS(digite 0 caso não tenha): '))

if cadastro["CTPS"] != 0:
    cadastro["Contratação"] = int(input('Ano de Contratação: '))
    cadastro["Salario"] = float(input('Salario: R$'))
    cadastro["Anos para aposentar"] = 35 - (date.today().year - cadastro["Contratação"])

print('\nResultado:')
for k, v in cadastro.items():
    print(f'| {k}: {v}')