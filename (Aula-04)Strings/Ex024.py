# Verificando a primeira palavra
print('SUA CIDADE É SANTA?:\n')

cidade = input('Qual o nome da sua cidade: ').strip()

print('\nResultado:')
print(f'Sua cidade começa com "SANTO"?: {cidade[:5].upper() == 'SANTO'}') # Isso e Sacanagem
