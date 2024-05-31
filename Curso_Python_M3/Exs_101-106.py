#Ex101
from datetime import date as dt

def votar(ano):
    idade = 2024 - ano
    #idade = dt.today().year - ano
    if (idade >= 70):
        print('Com {} anos: VOTO FACULTATIVO'.format(idade))
    elif (18 <= idade < 70):
        print('Com {} anos: VOTO OBRIGATÓRIO'.format(idade))
    else:
        print('Com {} anos: VOTO FACULTATIVO'.format(idade))
        
ano_nascimento = int(input('Ano de nascimento: '))
votar(ano_nascimento)

#Ex102
def fatorial(valor, mostrar=False):
    contador = 1
    if (mostrar == True):
        for v in range(valor,0,-1):
            contador *= v
            if (v > 0):
                print('{} * '.format(v), end='')
        print('= {}'.format(contador), end='\n')
    else:
        for v in range(valor, 0, -1):
            contador *= v
            print(contador)
        return contador

print(fatorial(5, mostrar=True))
    
#Ex103
def ficha_jogador(gols, jogador='<desconhecido>'):
        print('O jogador {} fez {} gol(s) no campeonato'.format(jogador, gols))
        
nome_jogador = input('Nome do jogador: ')
gols_jogador = int(input('Número de gols: '))
if (nome_jogador.strip() == ''):
    ficha_jogador(gols=gols_jogador)
else:
    ficha_jogador(gols_jogador, nome_jogador)

#Ex104 
def leiaInt(valor):
    if valor == None:
        pass
    elif valor.isnumeric() == True:
        valor = int(valor)
        return valor
    else:
        print('Erro! Digite um número inteiro válido!')
        numero = leiaInt(input('Digite um número: '))
        
numero = leiaInt(input('Digite um número: '))
print('Você acabou de digitar o número {}'.format(numero))

#Ex105
from time import sleep
def notas(*notas, situ=False):
    dados = {} 
    maior_nota = int(0)
    somatorio_notas = int(0)
    media = int(0)
    
    dados['total'] = len(notas)
    
    for vals in notas:
        if vals > maior_nota:
            maior_nota = vals
            dados['maior'] = maior_nota
        else:
            somatorio_notas +=  vals
    
    media = round((somatorio_notas / 3), 2)
    dados['media'] = media
    
    if (situ != False):
        if (media >= 7):
            dados['situacao'] = 'BOM'
        elif (5 < media < 7):
            dados['situacao'] = 'MEDIANA'
        elif (media < 5):
            dados['situacao'] = 'RUIM'
    else:
        pass
    
    return dados
    

resposta = notas(5.5,2.5,1.5, situ=True)
print(resposta)