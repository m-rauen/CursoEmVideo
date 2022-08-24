#Ex84
maior_peso = 0
menor_peso = 0
temporaria = []
princip = [] 

while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if (len(princip) == 0):
        maior_peso = menor_peso = temporaria[1]
    else:
        if (temporaria[1] > maior_peso):
            maior_peso = temporaria[1]
        elif (temporaria[1] < menor_peso):
            menor_peso = temporaria[1]
    
    princip.append(temporaria[:])
    temporaria.clear()
    
    resposta = str(input('Quer continuar (S/N): ')).upper()
    if (resposta != 'S'):
        break 
    
print('\n## RESULTADO FINAL ##', end='\n')
print('Foram cadastrados: {} pessoas'.format(len(princip)), end='\n')
print('O maior peso foi de: {}kg do(a) '.format(maior_peso), end='')
for dados in princip:
    if (maior_peso == dados[1]):
        print('{}'.format(dados[0]), end='\n')
print('O menor peso foi de: {}kg do(a) '.format(menor_peso), end='')
for dados in princip:
    if (menor_peso == dados[1]):
        print('{}'.format(dados[0]))
    
#Ex85 
valores_num = []
val_par = []
val_impar = []

for v in range(0, 7):
    valores_num.append(int(input('Digite algum valor: ')))
    if (valores_num[v] % 2 == 0):
        val_par.append(valores_num[v])
    else:
        val_impar.append(valores_num[v])

print('\n## RESULTADO FINAL ##', end='\n')
print('Valores pares: {}'.format(sorted(val_par)), end='\n')
print('Valores ímpares: {}'.format(sorted(val_impar)))

#Ex86
matrix = []

for linha in range(3):
    inp = []
    for coluna in range(3):
        inp.append(int(input('Valor - posição [{},{}]: '.format(linha, coluna))))
    matrix.append(inp)
    
print('\n ## RESULTADO FINAL', end='\n')
for i in range(3):
    for j in range(3):
        print('[{:^3}]'.format(matrix[i][j]), end=' ')
    print()    
    
#Ex87
matrix = [[0,0,0], [0,0,0], [0,0,0]]
conta_par = 0
conta_coluna = 0
maior_val_linha = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matrix[linha][coluna] = int(input('Digite o valor: '))
    
print('\n ## RESULTADO FINAL ##', end='\n')
print('='*20)
for i in range(0,3):
    for j in range(0,3):
        print('[{:^3}]'.format(matrix[i][j]), end=' ')
        if (matrix[i][j] % 2 == 0):
            conta_par += matrix[i][j]
    print()
print('='*20)

print('A soma dos valores pares é: {}'.format(conta_par), end='\n')

for l in range(0,3):
    conta_coluna += matrix[l][2]
print('A soma dos valores da 3a coluna é: {}'.format(conta_coluna), end='\n')

for c in range(0,3):
    if (matrix[2][c] > maior_val_linha):
        maior_val_linha = matrix[1][c]
print('O maior valor da 2a linha é: {}'.format(maior_val_linha), end='\n')

#Ex88 
from pygame import time as t
from random import randint as rit
jogo_megasena = []

limite = int(input('Quantos jogos quer sortear: '))

for c in range(limite):
    for i in range(6):
        valor = rit(1,60)
        if (valor not in jogo_megasena):
            jogo_megasena.append(valor)
    if (len(jogo_megasena) == 6):
        print(jogo_megasena)
        jogo_megasena.clear()
        t.delay(910)

print('Boa sorte!')

#Ex89 
dados = []

while True:
    nome = str(input('Nome: '))
    p1 = float(input('P1: '))
    p2 = float(input('P2: '))
    media = (p1 + p2) / 2
    dados.append([nome,[p1,p2],media])
    resposta = str(input('Quer continuar? (S/N): ')).upper()
    if (resposta != 'S'):
        break 
    
print('\n ## RESULTADO FINAL ##', end='\n')
print('{:<4}{:<10}{:>8}'.format('NÚMERO', 'NOME', 'MÉDIA'))
for i,aluno in enumerate(dados):
    print('{:<4}{:<10}{:>8.1f}'.format(i,aluno[0], aluno[2]))

while True:
    continua_notas = int(input('\nDeseja ver as notas de qual aluno? (999 interrompe): '))
    if (continua_notas != 999):
        if (continua_notas <= len(dados) - 1):
            print('Notas de {}:'.format(dados[continua_notas][0]), end='\n')
            print('{}'.format(dados[continua_notas][1]), end='\n')
    else:
        break
        

    
        
    