#Exercício 36
salario = float(input('Informe seu salário: '))
valor_casa = float(input('Informe o valor da casa: '))
tempo_parcela = int(input('Quanto anos para o pagamento: '))

prestacao_mensal = valor_casa / (tempo_parcela*12)

if prestacao_mensal > (0.30*salario):
    print('Empréstimo negado!')
else:
    print('Empréstimo aceito. Parabéns!!')

#Exercício 37:
algarismo = int(input('Informe qualquer algarismo inteiro: '))

print('-'*20)
print('MENU DE OPÇÕES: ')
print(' - (1): CONVERTER PARA BINÁRIO \n'
' - (2): CONVERTER PARA OCTAL \n'
' - (3): CONVERTER PARA HEXADECIMAL')
print('-'*20)

escolha = int(input('Escolhe qual tipo de conversão (1, 2 ou 3): '))

if escolha == 1:
    binario_alg = bin(algarismo)
    print('{} em binário é igual a {}'.format(algarismo, binario_alg))
elif escolha == 2:
    oct_alg = oct(algarismo)
    print('{} em octal é igual a {}'.format(algarismo, oct_alg))
elif escolha == 3:
    hexa_alg = hex(algarismo)
    print('{} em hexadecimal é igual a {}'.format(algarismo, hexa_alg))

#Exercício 38:
algarismo_1 = int(input('Informe qualquer algarismo inteiro: '))
algarismo_2 = int(input('Informe qualquer algarismo inteiro: '))

if algarismo_1 > algarismo_2:
    print('{} é maior que {}!'.format(algarismo_1, algarismo_2))
elif algarismo_2 > algarismo_1:
    print('{} é maior que {}!'.format(algarismo_2, algarismo_1))
else:
    print('{} é igual a {}!'.format(algarismo_1, algarismo_2))

#Exercício 39:
from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Informe seu ano de nascimento: '))
idade = ano_atual - ano_nascimento

if idade > 18:
    tempo_alistamento = idade - 18
    print('Passaram-se {} anos do seu tempo de alistamento!'.format(tempo_alistamento))
elif idade == 18:
    print('Esse é o ano do seu alistamento!')
else:
    tempo_alistamento = 18 - idade
    print('Ainda faltam {} anos para seu alistamento'.format(tempo_alistamento))

#Exercício 40:
prova_1 = float(input('Informe nota da P1: '))
prova_2 = float(input('Informe nota da P2: '))

media = (prova_1 + prova_2)/2

if media > 7.0:
    print('APROVADO!\n'
    'MÉDIA {:.2f}'.format(media))
elif media > 5.0 or media <= 6.9:
    print('RECUPERAÇÃO\n'
    'MÉDIA {:.2f}'.format(media))
elif media < 5.0:
    print('REPROVADO! \n'
    'MÉDIA {:.2f}'.format(media))

#Exercício 41:
from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Informe seu ano de nascimento: '))

idade = ano_atual - ano_nascimento

if idade > 25:
    print('CATEGORIA MASTER')
elif idade > 19 or idade <= 25:
    print('CATEGORIA SÊNIOR')
elif idade > 14 or idade <= 19:
    print('CATEGORIA JÚNIOR')
elif idade > 9 or idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <= 9:
    print('CATEGORIA MIRIM')

#Exercício 42:
lado_1 = float(input('Informe o valor de um dos lados: '))
lado_2 = float(input('Informe o valor de um dos lados: '))
lado_3 = float(input('Informe o valor de um dos lados: '))

if (lado_1 - lado_2) < lado_3:
    Triangulo = True
elif (lado_3 - lado_2) < lado_1:
    Triangulo = True
elif (lado_3 - lado_1) < lado_2:
    Triangulo = True
else: 
    print('NÃO FORMA UM TRIÂNGULO!')

if Triangulo == True:
    if (lado_3 == lado_2) and (lado_2 == lado_1):
        print('TRIÂNGULO EQUILÁTERO!')
    elif (lado_1 == lado_2) or (lado_2 == lado_3) or (lado_1 == lado_3):
        print('TRIÂNGULO ISÓSCELES!')
    elif (lado_1 != lado_2) and (lado_2 != lado_3) and (lado_1 != lado_3):
        print('TRIẦNGULO ESCALENO!')

#Exercício 43:
altura = float(input('Informe sua altura (m): '))
peso = float(input('Informe seu peso (kg): '))

imc = peso / altura**2

if imc > 40:
    print('OBESIDADE MÓRBIDA!')
    print('SEU IMC CORRESPONDE À {:.2f}'.format(imc))
elif (imc > 30) and (imc < 40):
    print('OBESIDADE!')
    print('SEU IMC CORRESPONDE À {:.2f}'.format(imc))
elif (imc > 25) and (imc < 30):
    print('SOBREPESO!')
    print('SEU IMC CORRESPONDE À {:.2f}'.format(imc))
elif (imc > 18.5) and (imc < 25):
    print('PESO IDEAL!')
    print('SEU IMC CORRESPONDE À {:.2f}'.format(imc))
else: 
    print('ABAIXO DO PESO!')
    print('SEU IMC CORRESPONDE À {:.2f}'.format(imc))

#Exercício 44:
valor_inicial = float(input('Valor total das compras: '))

print('=-'*20)
print('(1) - À VISTA NO DINHEIRO OU CHEQUE')
print('(2) - À VISTA NO CARTÃO')
print(('(3) - 2x NO CARTÃO'))
print('(4) - 3x (OU MAIS) NO CARTÃO:')
print('=-'*20)

escolha_pagamento = int(input('Escolha a forma de pagamento: '))
if escolha_pagamento == 4:
    parcelamento = int(input('INFORME QUANTAS VEZES DESEJA PARCELAR: '))

if escolha_pagamento == 1:
    valor_final = valor_inicial - (valor_inicial*0.10) 
    print('Valor final das compras: R${:.2f}'.format(valor_final))
elif escolha_pagamento == 2:
    valor_final = valor_inicial - (valor_inicial*0.05)
    print('Valor final das compras: R${:.2f}'.format(valor_final))
elif escolha_pagamento == 3:
    valor_final = valor_inicial / 2
    print('Valor final das parcelas: R${:.2f}'.format(valor_final))
elif escolha_pagamento == 4:
    valor_juros = valor_inicial + (valor_inicial*0.20)
    valor_final = valor_juros / parcelamento
    print('Valor final das parcelas: R${:.2f}'.format(valor_final))

#Exercício 45:
import random

print('=-'*15)
print('OPÇÕES DE JOGADA:')
print('(1) - PEDRA')
print('(2) - PAPEL')
print('(3) - TESOURA')
print('=-'*15)

jogada_player = int(input('Informe sua jogada: '))
if (jogada_player != 1) and (jogada_player != 2) and (jogada_player != 3):
    print('Jogada inválida. Tente novamente!')
    jogada_player = int(input('Informe sua jogada: '))

jogada_bot = random.randint(1,3)

if jogada_player == 1 and jogada_bot == 2:
    print('JOGADOR: PEDRA \n'
        'BOT: PAPEL ')
    print('O JOGADOR GANHOU!') 
elif jogada_player == 1 and jogada_bot == 3:
    print('JOGADOR: PEDRA \n'
        'BOT: TESOURA ')
    print('O JOGADOR GANHOU!')
elif jogada_player == 2 and jogada_bot == 1:
    print('JOGADOR: PAPEL \n'
        'BOT: PEDRA ')
    print('O BOT GANHOU!')
elif jogada_player == 2 and jogada_bot == 3:
    print('JOGADOR: PAPEL \n'
        'BOT: TESOURA ')
    print('O BOT GANHOU!')
elif jogada_player == 3 and jogada_bot == 1:
    print('JOGADOR: TESOURA \n'
        'BOT: PEDRA ')
    print('O BOT GANHOU!')
elif jogada_player == 3 and jogada_bot == 2:
    print('JOGADOR: TESOURA \n'
        'BOT: PAPEL ')
    print('O JOGADOR GANHOU!')
elif jogada_player == jogada_bot:
    print('JOGADAS IGUAIS')
    print('EMPATE!!')
    




