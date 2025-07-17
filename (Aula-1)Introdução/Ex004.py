#"Dissecando" uma variavel
print('DISSECANDO VARIAVEL\n')
coisa = input('Digite algo: ')

print('\nResultado:') 
print(f'O tipo primitivo desse valor é: {type(coisa)}')
print(f'Só tem espaços?: {coisa.isspace()}')
print(f'É um numero?: {coisa.isnumeric()}')
print(f'É alfabetico?: {coisa.isalpha()}')
print(f'É alfanumerico?: {coisa.isalnum()}')
print(f'Está em maiusculas?: {coisa.isupper()}')
print(f'Está em minusculas?: {coisa.islower()}')
print(f'Está capitalizada?: {coisa.istitle()}')

# Exerciciozinho chatoo!!
