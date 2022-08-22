#Exercício 46:
import time
for contador in range(10,-1,-1):
    print(contador)
    time.sleep(1)

#Exercício 47:
import time as tm
for contador in range(0,51,2):
    print(contador)
    tm.sleep(1)

#Exercício 48:
soma = int(0)

for numero in range(1,501,2):
    if (numero % 3 == 0):
        soma += numero

print(soma)

#Exercício 49:
import time as tm
escolha = int(input('Informe número da tabuada: '))

for contador in range(1,11):
    resultado = escolha*contador
    print('{} x {} = {}'.format(escolha,contador,resultado))
    tm.sleep(1)

#Exercício 50:
somatoria_par = 0
for contador in range(1,7):
    numero = int(input('Informe número escolhido: '))
    if (numero % 2 == 0):
        somatoria_par += numero

print('A soma dos números pares foi {}'.format(somatoria_par))

#Exercício 51:
inicio = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a progressão da PA: '))

for c in range(inicio, inicio+10):
    resultado = inicio+razao
    print(resultado)
    inicio = resultado

#Exercício 52:
num = int(input('Informe o número: '))
total = 0

for c in range(1, num+1):
    if num % c ==0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m',end='')
    print('{}'.format(c), end='')
    
print('\n\033[m0 número {} foi divisível {} vezes'.format(num, total))

if total == 2:
    print('Portanto, é número PRIMO')
else:
    print('Sendo assim, NÃO é número PRIMO')
    
#Exercício 53:
frase_entrada = input('Informe a frase: ').upper().replace(' ','')

frase_reverso = frase_entrada[::-1]

if frase_entrada == frase_reverso:
      print('Invertido temos: {}'.format(frase_reverso))
      print('É um palíndromo!')
else:
      print('Invertido temos: {}'.format(frase_reverso))  
      print('Não é um palíndromo!')

#Exercício 54:
contador_18 = 0

for contador in range(1,8):
    idade = int(input('Informe sua idade: '))
    if (idade > 18):
        contador_18 += 1

print('Existem {} pessoas +18 no grupo'.format(contador_18))

#Exercício 55:
maior_peso = 0

for contador in range(1,6):
    peso = float(input('Informe seu peso (kg): '))
    menor_peso = peso
    if (peso > maior_peso):
        maior_peso = peso
    elif (peso < menor_peso):
        menor_peso = peso

print('MAIOR PESO: {}kg \n'
      'MENOR PESO: {}kg'.format(maior_peso,menor_peso))

#Exercício 56:
somatorio_idade = 0
homem_idade = 0
contador_mulheres = 0

print('-'*25)
for contador in range(1,5):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    somatorio_idade += idade
    sexo = str(input('Sexo (M/F): ')).upper()
    print('-'*25)
    if (sexo == 'M') and (idade > homem_idade):
        homem_idade = idade
        nome_homem = nome
    if (sexo == 'F') and (idade < 20):
        contador_mulheres += 1
        
media = somatorio_idade / contador    

print('MÉDIA DE IDADE: {:.2f}\n'
      'NOME DO HOMEM MAIS VELHO: {}\n '
      'EXISTE(M) {} MULHERE(S) COM -20 ANOS'.format(media,nome_homem,contador_mulheres))
