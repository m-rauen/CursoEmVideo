#Ex96
def area(larg, comp):
    return (larg * comp)

largura = float(input('Largura (m): '))
comprimento = float(input('Altura (m): '))
resultado_area = area(largura, comprimento)
print('\nÁrea de um terreno de {:.2f}x{:.2f} é {:.2f}m²'.format(largura, comprimento, resultado_area))

#Ex97
def escreva(msg):
    print('~' * 20, end='\n')
    print('{:<5}'.format(msg), end='\n')
    print('~' * 20, end='\n')
    
nome = str(input('Digite seu nome completo: ')). capitalize()
escreva(nome)

#Ex98
from time import sleep
def crescente():
    print('~' * 40, end='\n')
    for c in range(1,11):
        print(c, end=' ')
        sleep(0.5)
    print()
    
def decrescente():
    print('~' * 40, end='\n')
    for i in range(10,-1,-2):
        print(i, end=' ')
        sleep(0.5)
    print()    
    
def personalizar(ini,final,step):
    print('~' * 40, end='\n')
    for j in range(ini,final,step):
        print(j, end=' ')
        sleep(0.5)
    print()
    
crescente()
decrescente()
print('~' * 40, end='\n')
print('Agora é sua vez de personalizar a contagem!', end='\n')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
personalizar(inicio, fim, passo)

#Ex99
from time import sleep

def maior(*valores):
    maior = contador = 0
    print('~' * 30)
    print('Analisando valores recebidos...', end='\n')
    for val in valores:
        print('{}'.format(val), end=' ', flush=True)
        sleep(0.5)
        if (contador == 0):
            maior = val
        else:
            if (val > maior):
                maior = val
        contador += 1
    print('\nForam informados {} valores ao todo'.format(contador), end='\n')
    print('O maior valor informado foi: {}'.format(maior), end='\n')
    
maior(2,9,4,5,1)
maior(4,7,12)
maior(99,100)
maior()

#Ex100 
from random import randint as rit
from time import sleep

def sortear():
    vals = []
    print('Sorteando os 5 valores da lista:', end='\n')
    for c in range(5):
        valor = rit(1,10)
        print(valor, end=' ')
        vals.append(valor)
        sleep(0.5)

    return vals

def somar(arr_vals):
    valores_par = 0
    print('\nSomando os valores pares de {} temos '.format(arr_vals), end='')
    for v in arr_vals:
        if (v % 2 == 0):
            valores_par += v
    print(valores_par, end='\n')
    
valores = sortear()
somar(valores)
        
        