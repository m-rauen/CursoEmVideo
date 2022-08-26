#Ex90
dados = {}

dados.update({str(input('Nome: ')):float(input('Media: '))})

print('\nNome é igual a ', end='')
for nome in dados.keys():
    print(nome + '\n')

print('Média é igual a: ', end='')
for media in dados.values():
    print(str(media) + '\n')
    if (media >= 7):
        print('Situação final: Aprovado!')
    elif (media > 5.5) and (media <= 6.5):
        print('Situação final: Em Recuperação!')
    else:
        print('Situação final: Reprovado!')
        
#Ex91 
from random import randint as rit
from pygame import time as t

controle_jogadas = {}
maior_val = int(0)
posicao = int(1)

for round in range(1,5):
    jogada = rit(1,6)
    print('Jogador' + str(round), 'tirou {} no dado'.format(jogada))
    controle_jogadas.update({'Jogador' + str(round) : jogada})
    t.delay(910)
    
print('\n ## RESULTADO FINAL ##', end='\n')
print('='*25)
controle_jogadas_final = sorted(controle_jogadas.items(), key=lambda item:item[1])
for jogador,valor in reversed(controle_jogadas_final):
        print('{}o lugar: {} com {}'.format(posicao, jogador, valor))
        t.delay(910)
        posicao += 1
            
#Ex92 
from datetime import datetime
dados = {}

while True:
    dados['nome'] = str(input('Nome: ')) 
    dados['idade'] = datetime.now().year - (int(input('Ano nascimento: ')))
    carteira_trab = int(input('Carteira de trabalho (0 se não tem): '))
    dados['CTPS'] = carteira_trab
    if carteira_trab == 0:
        print("## RESULTADO FINAL ##", end='\n')
        for k,v in dados.items():
            print('-> {} tem o valor: {} '.format(k,v), end='\n')
        break
    else:
        dados['ano_contratacao'] = int(input('Ano de contratação: '))
        dados['salario'] = float(input('Salário: R$'))
        break

print("## RESULTADO FINAL ##", end='\n')
print('='*25, end='\n')
for k,v in dados.items():
    print('-> {} tem o valor: {} '.format(k,v), end='\n')
    
#Ex93 
dados = {}
partidas = []
total_gols = int(0)

nome_jogador = str(input('Nome: '))
dados['nome'] = nome_jogador

total_partidas = int(input('Quantas partidas {} jogou? '.format(nome_jogador)))
for c in range(total_partidas):
    gols = int(input('Quantos gols na partida {}? '.format(c)))
    partidas.append(gols)
    total_gols += gols
    
dados['gols'] = partidas
dados['total'] = total_gols

print('## RESULTADO FINAL ##', end='\n')
print('='*25, end='\n')
print(dados)
print('='*25, end='\n')
for k,v in dados.items():
    print('O campo {} tem o valor {}'.format(k,v), end='\n')
print('='*25, end='\n')
print('O jogador {} jogou {} partidas'.format(nome_jogador, len(partidas)), end='\n')
for i,g in enumerate(dados['gols']):
    print('-> Na partida {}, fez {} gol(s)'.format(i,g), end='\n')
print('Foi um total de {} gol(s)'.format(total_gols), end='\n')

#Ex94 
grupo = []
pessoa = {}
somatorio = int(0)
media = float(0)

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo (M/F): ')).upper()[0]
        if (pessoa['sexo'] in 'MF'):
            break
        print('Erro! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    somatorio += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        continua = str(input('Quer continuar? (S/N): ')).upper()[0]
        if (continua in 'SN'):
            break
        print('Erro! Por favor, digite apenas S ou N')
    if (continua == 'N'):
        break
    
print('## RESULTADO FINAL ##', end='\n')
print('='*25, end='\n')
print('Ao todo temos {} pessoas cadastradas'.format(len(grupo)), end='\n')
media = somatorio / len(grupo)
print('A média de idade é de {.2f} anos'.format(media), end='\n')

print('As mulheres cadastradas foram: ', end='')
for person in grupo:
    if (person['sexo'] in 'Ff'):
        print('{}'.format(person['nome']), end='')
print()

print('Lista das pessoas que estão acima da média: ')
for p in grupo:
    if (p['idade'] >= media):
        print('   ', end='|')
        for k,v in p.items():
            print('{} = {}; '.format(k,v), end='')
        print()
        
#Ex95 



        
            