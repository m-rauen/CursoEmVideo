#Ex78
valores = []
maior_valor = 0
menor_valor = 0

for numero in range(0,5):
    valores.append(int(input('Digite algum número: ')))
    if (numero == 0):
        maior_valor = menor_valor = valores[numero]
    
    if (valores[numero] > maior_valor):
        maior_valor = valores[numero]
    elif (valores[numero] < menor_valor):
        menor_valor = valores[numero]
    else: 
        pass

print('Lista completa: {}'.format(valores), end='\n')
print('Maior valor da lista: {}, na posição(ões) '.format(maior_valor), end='')
for posicao, valor in enumerate(valores):
    if (valor == maior_valor):
        print('{} '.format(posicao), end='')
print('\n')
print('Menor valor da lista: {}, na posição(ões) '.format(menor_valor), end='')
for posicao, valor in enumerate(valores):
    if (valor == menor_valor):
        print('{} '.format(posicao), end='')
print('\n')

#Ex79
valores = []
resposta = 'S'

while resposta == 'S':
    numero = int(input('Digite algum valor único: '))
    if (numero not in valores):
        valores.append(numero)
    else: 
        print('Valor duplicado, portanto, não adicionado!', end='\n')
            
    resposta = str(input('Quer continuar? (S/N): ')).upper()
    if (resposta == 'S'):
        numero = int(input('Digite algum valor único: '))
        if (numero not in valores):
            valores.append(numero)
        resposta = str(input('Quer continuar? (S/N): ')).upper()
    elif (resposta != 'S'):
        continua = False
        
print('\n')
print('Resultado Final:')
print('Valores adicionados: {}'.format(sorted(valores)))

#Ex80 
valores_num = []

for c in range(0, 5):
    valor = int(input('Digite algum valor: '))
    if (c == 0) or (valor >valores_num[-1]):
        valores_num.append(valor)
    else:
        posicao = 0 
        while (posicao < len(valores_num)):
            if (valor <= valores_num[posicao]):
                valores_num.insert(posicao, valor)
                break
            posicao += 1

print(valores_num)
    
#Ex81 
valores_num = []
resposta = 'S'

while resposta == 'S':
    valores_num.append(int(input('Digite algum valor: ')))
    resposta = str(input('Quer continuar? (S/N): ')).upper()
    if (resposta != 'S'):
        print('## RESULTADO ##\n')
        print('Foram digitados {} números;'.format(len(valores_num)), end='\n')
        print('Lista ordenada: ', sorted(valores_num), end='\n')
        if (5 in valores_num):
            print('O valor 5 está nessa lista!')
        else:
            print('O valor 5 não está nessa lista!')

#Ex82 
valores_num = []
valores_par = []
valores_impar = []
resposta = 'S'

while (resposta == 'S'):
    valores_num.append(int(input('Digite algum valor: ')))
    resposta = str(input('Quer continuar? (S/N): ')).upper()
    if (resposta != 'S'):
        print('## RESULTADO ##', end='\n')
        print('Lista completa: {}'.format(sorted(valores_num)), end='\n')
        for numero in valores_num:
            if (numero % 2 == 0):
                valores_par.append(numero)
            else:
                valores_impar.append(numero)
        print('Lista dos pares: {}'.format(sorted(valores_par)), end='\n')
        print('Lista dos ímpares: {}'.format(sorted(valores_impar)), end='\n')
        
#Ex83 
lcount = 0
rcount = 0
caracteres = []

exp_mtm = str(input('Expressão matemática: '))
for c in exp_mtm:
    caracteres.append(c)

for parenthesis in caracteres:
    if (parenthesis == '('):
        lcount += 1
    elif (parenthesis == ')'):
        rcount += 1
        
        
if (lcount == rcount):
    print('Parabéns, sua expressão é regular!')
else:
    print('Infelizmente, sua expressão não é regular!')





