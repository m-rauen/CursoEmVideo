#Exercício58
# import random as rm

# contador = int(0)
# jogada_bot = rm.randrange(0,10)
# jogada_player = int(input('Informe seu palpite (0-10): ' ))

# if jogada_player == jogada_bot:
#     print('{} = {} '.format(jogada_bot, jogada_player))
#     print('Parabéns, você venceu!')
# elif jogada_player != jogada_bot:
#     print('{} != {} '.format(jogada_bot, jogada_player))
#     print('Infelizmente você errou. Tente novamente!')
#     jogada_bot = rm.randrange(0,10)
#     jogada_player = int(input('Informe seu palpite (0-10): ' ))
#     while jogada_player != jogada_bot:
#         print('{} != {} '.format(jogada_bot, jogada_player))
#         print('Infelizmente você errou. Tente novamente!')
#         jogada_bot = rm.randrange(0,10)
#         jogada_player = int(input('Informe seu palpite (0-10): ' ))
#         if jogada_player == jogada_bot:
#             print('{} = {} '.format(jogada_bot, jogada_player))
#             print('Parabéns, você venceu!')
#             break

#Exercício59
# def maior_menor(a,b):
#     if a > b:
#         return a
#     elif b > a:
#         return b


# valor1 = int(input('Informe qualquer valor inteiro: '))
# valor2 = int(input('Informe qualquer valor inteiro: '))

# opcao = 0
# while opcao != 5:
#     print('=-'*20)
#     print('MENU DE OPÇÕES:\n'
#           '(1) - SOMAR \n'
#           '(2) - MULTIPLIOCAR \n'
#           '(3) - DEFINIR MAIOR \n'
#           '(4) - NOVOS NÚMEROS \n'
#           '(5) - SAIR DO PROGRAMA')
#     print('=-'*20)
#     opcao = input('Escolha: ')
#     if opcao == '1':
#         print(valor1 + valor2)
#     elif opcao == '2':
#         print(valor1 * valor2)
#     elif opcao == '3':
#         print('Maior valor: {}'.format(maior_menor(valor1, valor2)))
#     elif opcao == '4':
#         valor1 = int(input('Informe qualquer valor inteiro: '))
#         valor2 = int(input('Informe qualquer valor inteiro: '))
#     elif opcao == '5':
#         break
#     else: 
#         print('Opção inválida. Tente novamente!')
#         valor1 = int(input('Informe qualquer valor inteiro: '))
#         valor2 = int(input('Informe qualquer valor inteiro: '))

#Exercício60
# valor = int(input('Informe qualquer valor inteiro: '))
# contador = valor 
# resultado = int(1)

# while contador != 0:
#     print('{} '.format(contador), end='')
#     if contador > 1:
#         print(' x ', end='')
#     else:
#         print(' = ', end='')
#     resultado *= contador
#     contador -= 1

# print('{}'.format(resultado))

#Exerício61
# inicio_pa = int(input('Informe início da P.A.: '))
# razao_pa = int(input('Informe a razão: '))

# termos_pa = inicio_pa
# contador = 1

# while contador < 10:
#     print(termos_pa+razao_pa)
#     termos_pa += razao_pa
#     contador += 1

#Exercício62
# import time as tm

# inicio_pa = int(input('Informe início da P.A.: '))
# razao_pa = int(input('Informe a razão: '))

# termos_pa = inicio_pa
# contador = 1
# continua = str('S')


# while continua == 'S':
#     print(termos_pa+razao_pa)
#     termos_pa += razao_pa
#     contador += 1
#     tm.sleep(0.5)
#     if contador > 10:
#         continua = str(input('Deseja continuar? (S/N): ')).upper()
#         if continua == 'S':
#             limite = int(input('Quantos termos: '))
#             while contador < limite:
#                 print(termos_pa+razao_pa)
#                 termos_pa += razao_pa
#                 contador += 1
#                 tm.sleep(0.5) 
#         elif continua == 'N':
#             break
#         else:
#             print('Opção inválida. Abortando!', end='\n')
#             raise ValueError

#Exercício63:
# import time as tm

# limite = int(input('Quantos termos da PA: '))

# termo_init = 0
# proximo_termo = 1
# contador = 0

# while contador < limite:
#     print(termo_init, end='\n')
#     tm.sleep(0.5)
#     termo_lim = termo_init + proximo_termo #define aqui o nésimo termo
#     termo_init = proximo_termo #faz o n1 virar o n2, sucessivamente
#     proximo_termo = termo_lim #faz o n2 virar nésimo, sucessivamente
#     contador += 1

#Exercício64:
# from os import abort

# def abortMode():
#     import time as tm
    
#     print('=-'*20)
#     print('{} ABORTANDO {}'.format(' '*10, ' '*10))
#     print('=-'*20)
#     tm.sleep(1)
#     print('...')
#     tm.sleep(1)
    
    
# somador_numeros = 0
# valor_escolha = int(input('Informe o valor: '))
# somador_numeros += valor_escolha

# while valor_escolha != 999:
#     valor_escolha = int(input('Informe o valor: '))
#     somador_numeros += valor_escolha
#     if valor_escolha == 999:
#         print('SOMATÓRIA FINAL: {}'.format(somador_numeros))
#         abortMode()
        
#Exercício70:
# preco_barato = 1000
# nome_barato = 'abc'
# total = 0
# produtos_caros = 0

# while True:
#     nome = str(input('Nome: '))
#     preco = float(input('Preço: '))
#     total += preco
    
#     if (preco_barato > preco):
#         preco_barato = preco
#         nome_barato = nome
    
#     if (preco > 1000):
#         produtos_caros += 1
        
#     continua = str(input('Quer continuar? (S/N): ')).upper()
#     if (continua == 'N'):
#         break 
    
# print('-'*15)
# print('Nome e preço do produto mais barato: {}, R${}'.format(nome_barato, preco_barato))
# print('Existe(m) {} produto(s) que custa(m) mais de R$1000,00'.format(produtos_caros))
# print('Total gasto: R$ {}'.format(total))
# print('-'*15)

#Exercício71
# valor = int(input('Valor de saque: R$'))
# resultado = valor 
# notas_50 = 0
# notas_20 = 0 
# notas_10 = 0
# notas_1 = 0 

# while True:
#     if (resultado >= 50):
#         resultado -= 50
#         notas_50 += 1
#     elif (resultado < 50 and resultado >= 20):
#         resultado -= 20  
#         notas_20 += 1
#     elif (resultado < 20 and resultado >= 10):
#         resultado -= 10 
#         notas_10 += 1 
#     elif (resultado < 10 and resultado >= 1):
#         resultado -= 1 
#         notas_1 += 1 

#     if (resultado == 0):
#         break 
    
# print('Notas: \n'
#       '50: {} \n'
#       '20: {} \n'
#       '10: {} \n'
#       '1: {} \n'.format(notas_50, notas_20, notas_10, notas_1))







