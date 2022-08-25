#Ex90
# dados = {}

# dados.update({str(input('Nome: ')):float(input('Media: '))})

# print('\nNome é igual a ', end='')
# for nome in dados.keys():
#     print(nome + '\n')

# print('Média é igual a: ', end='')
# for media in dados.values():
#     print(str(media) + '\n')
#     if (media >= 7):
#         print('Situação final: Aprovado!')
#     elif (media > 5.5) and (media <= 6.5):
#         print('Situação final: Em Recuperação!')
#     else:
#         print('Situação final: Reprovado!')
        
#Ex91 
# from random import randint as rit
# from pygame import time as t

# controle_jogadas = {}
# maior_val = int(0)
# posicao = int(1)

# for round in range(1,5):
#     jogada = rit(1,6)
#     print('Jogador' + str(round), 'tirou {} no dado'.format(jogada))
#     controle_jogadas.update({'Jogador' + str(round) : jogada})
#     t.delay(910)
    
# print('\n ## RESULTADO FINAL ##', end='\n')
# print('='*25)
# controle_jogadas_final = sorted(controle_jogadas.items(), key=lambda item:item[1])
# for jogador,valor in reversed(controle_jogadas_final):
#         print('{}o lugar: {} com {}'.format(posicao, jogador, valor))
#         t.delay(910)
#         posicao += 1
            
#Ex92 
# from datetime import datetime
# dados = {}

# while True:
#     dados['nome'] = str(input('Nome: ')) 
#     dados['idade'] = datetime.now().year - (int(input('Ano nascimento: ')))
#     carteira_trab = int(input('Carteira de trabalho (0 se não tem): '))
#     dados['CTPS'] = carteira_trab
#     if carteira_trab == 0:
#         print("## RESULTADO FINAL ##", end='\n')
#         for k,v in dados.items():
#             print('-> {} tem o valor: {} '.format(k,v), end='\n')
#         break
#     else:
#         dados['ano_contratacao'] = int(input('Ano de contratação: '))
#         dados['salario'] = float(input('Salário: R$'))
#         break

# print("## RESULTADO FINAL ##", end='\n')
# print('='*25, end='\n')
# for k,v in dados.items():
#     print('-> {} tem o valor: {} '.format(k,v), end='\n')
    
#Ex93 
       
