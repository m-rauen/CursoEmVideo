#Ex107
from Ex107 import moeda

preco = float(input('Digite o preço: R$'))
print('Metade de R${:.2f} é R${:.2f}'.format(preco, moeda.metade(preco)), end='\n')
print('O dobro de R${:.2f} é R${:.2f}'.format(preco, moeda.dobro(preco)), end='\n')
print('Aumentando 10% temos R${:.2f}'.format(moeda.aumentar(preco,10)), end='\n')
print('Diminuindo 10% temos R${:.2f}'.format(moeda.diminuir(preco,10)), end='\n')

#Ex108
from Ex108 import moeda

preco = float(input('Digite o preço: R$'))
print('Metade de R${} é R${}'.format(preco, moeda.moeda(moeda.metade(preco))), end='\n')
print('O dobro de R${} é R${}'.format(preco, moeda.moeda(moeda.dobro(preco))), end='\n')
print('Aumentando 10% temos R${}'.format(moeda.moeda(moeda.aumentar(preco,10))), end='\n')
print('Diminuindo 10% temos R${}'.format(moeda.moeda(moeda.diminuir(preco,10))), end='\n')

#Ex113
def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Por favor, digite um valor válido')
            continue
        except (KeyboardInterrupt):
            print('Erro! Entrada de dados interompida')
            return 0
        else:
            return numero

def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print('Erro! Por favor, digite um valor válido')
            continue
        except (KeyboardInterrupt):
            print('Erro! Entrada de dados interompida')
            return 0 
        else:
            return numero

num = leiaInt('Digite um valor: ')
print('O valor digitado foi {}'.format(num))

#Ex114
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except (urllib.error.URLErro):
    print("Desculpe! O site 'pudim' não está acessível no momento!")
else:
    print('Conseguimos e acessamos!')

