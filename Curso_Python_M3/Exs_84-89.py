#Ex84
# maior_peso = 0
# menor_peso = 0
# temporaria = []
# princip = [] 

# while True:
#     temporaria.append(str(input('Nome: ')))
#     temporaria.append(float(input('Peso: ')))
#     if (len(princip) == 0):
#         maior_peso = menor_peso = temporaria[1]
#     else:
#         if (temporaria[1] > maior_peso):
#             maior_peso = temporaria[1]
#         elif (temporaria[1] < menor_peso):
#             menor_peso = temporaria[1]
    
#     princip.append(temporaria[:])
#     temporaria.clear()
    
#     resposta = str(input('Quer continuar (S/N): ')).upper()
#     if (resposta != 'S'):
#         break 
    
# print('\n## RESULTADO FINAL ##', end='\n')
# print('Foram cadastrados: {} pessoas'.format(len(princip)), end='\n')
# print('O maior peso foi de: {}kg do(a) '.format(maior_peso), end='')
# for dados in princip:
#     if (maior_peso == dados[1]):
#         print('{}'.format(dados[0]), end='\n')
# print('O menor peso foi de: {}kg do(a) '.format(menor_peso), end='')
# for dados in princip:
#     if (menor_peso == dados[1]):
#         print('{}'.format(dados[0]))
    
#Ex85 
# valores_num = []
# val_par = []
# val_impar = []

# for v in range(0, 7):
#     valores_num.append(int(input('Digite algum valor: ')))
#     if (valores_num[v] % 2 == 0):
#         val_par.append(valores_num[v])
#     else:
#         val_impar.append(valores_num[v])

# print('\n## RESULTADO FINAL ##', end='\n')
# print('Valores pares: {}'.format(sorted(val_par)), end='\n')
# print('Valores ímpares: {}'.format(sorted(val_impar)))

#Ex86
# matrix = []

# for linha in range(3):
#     inp = []
#     for coluna in range(3):
#         inp.append(int(input('Valor - posição [{},{}]: '.format(linha, coluna))))
#     matrix.append(inp)
    
# print('\n ## RESULTADO FINAL', end='\n')
# for i in range(3):
#     for j in range(3):
#         print('[{:^3}]'.format(matrix[i][j]), end=' ')
#     print()    
    
#Ex87

    

    