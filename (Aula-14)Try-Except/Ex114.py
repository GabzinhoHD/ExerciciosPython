# Acessando uma pagina web
import requests
print('PUDIM ESTA ACESSIVEL?:\n')

url = 'https://www.pudim.com.br/'

try:
    resposta = requests.get(url)

except (requests.ConnectionError):
    print('\033[1;31mERRO!! Não foi posssivel acessar o site do Pudim!!')
else:
    print('\033[1;33mO Site do Pudim esta Acessivel!!')
    print(f'\033[mLINK: \033[1;34m{url}')