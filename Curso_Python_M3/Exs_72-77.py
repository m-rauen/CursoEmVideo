#Ex72
# tup = (
# 'zero',
# 'um',
# 'dois',
# 'três',
# 'quatro',
# 'cinco',
# 'seis',
# 'sete',
# 'oito',
# 'nove',
# ' dez',
# ' onze',
# ' doze',
# ' treze',
# ' quatorze ou catorze',
# 'quinze',
# ' dezesseis',
# ' dezessete',
# ' dezoito',
# ' dezenove',
# ' vinte'
# )

# numero = int(input('Digite um número (0-20): '))
# print('Você digitou o número {}'.format(tup[numero]))

#Ex73
# tabela_times = (
# 'Palmeiras',
# 'Fluminense',
# 'Flamengo',
# 'Corinthians',
# 'Athletico',
# 'Internacio',
# 'Atlético',
# 'América',
# 'Red Bull Bragantino',
# 'Santos',
# 'Goiás',
# 'São Paulo',
# 'Botafogo',
# 'Ceará',
# 'Fortaleza',
# 'Cuiabá',
# 'Avaí',
# 'Atlético',
# 'Juventude'
# )

# print('#'*20)
# print('RESULTADO')
# print('#'*20)

# print('Os 5 primeiros times são: {}\n'.format(tabela_times[0:5]))
# print('Os últimos 4 colocados são: {}\n'.format(tabela_times[-4:]))
# print('Os times em ordem alfabética são: {}\n'.format(sorted(tabela_times)))
# print('O Avaí (SC) está na posição: {}\n'.format(tabela_times.index('Avaí')))

#Ex74 
# from random import randint 

# randtup = (randint(1,15), randint(1,15), randint(1,15), randint(1,15), randint(1,15))
# maior_val = 0
# menor_valor = 15

# for maior in randtup:
#     if maior > maior_val:
#         maior_val = maior
    
# for menor in randtup:
#     if menor < menor_valor:
#         menor_valor = menor

# print('Valores gerados: {}'.format(randtup))
# print('Maior valor dos gerados: {}'.format(maior_val))
# print('Menor valor dos gerados: {}'.format(menor_valor))

#Ex75
# valores_lidos = (
#     int(input('Primeiro valor: ')), int(input('Segundo valor: ')), int(input('Terceiro valor: ')), int(input('Quarto valor: '))
#     )
        
# print('Vezes que apareceram o número 9: {}\n'.format(valores_lidos.count(9)))
# print('Primeira posição digitado o número 3: {}\n'.format((valores_lidos.index(3)+1)))
# print('Números pares: ', end='')

# for valor in valores_lidos:
#     if (valor % 2 == 0):
#         print(valor, end=' ')

#Ex76 
# item_e_precos = (
#     'Lápis',
#     1.50,
#     'Borracha',
#     2.50, 
#     'Caneta',
#     8.90,
#     'Caderno',
#     22.90
# )

# header = """
# \n
# ============================
# LISTAGEM DE PREÇOS FINAL: 
# ============================
# \n
# """
# print(header.center(50))
# for valor in range(0, len(item_e_precos)):
#         if (valor % 2 == 0):
#             print('{:.<30}'.format(item_e_precos[valor]), end='')
#         else:
#             print('R$ {:>3.2f}'.format(item_e_precos[valor]))

#Ex77 
palavras = (
    'adesao',
    'carro',
    'taquicardia',
    'computador',
    'python'
)

msg = "Na palavra '{}' temos as vogais: {}"

for palavra in palavras:
    for letras in palavras:
        if letras == 'aeiou':
            print(msg.format(palavra, letras), end=' ')
