import urllib.request
from urllib.parse import urlparse

try:
    from time import sleep

    url = urllib.request.urlopen('http://www.pudim.com.br')
    nome_site = urlparse('http://www.pudim.com.br').netloc
    print(f'Tentando conexão com o site {nome_site}...')
    sleep(1)
except urllib.error.URLError:
    print('Não foi possível conectar-se ao site no momento!')
else:
    print('Conexão realizada com sucesso!')
