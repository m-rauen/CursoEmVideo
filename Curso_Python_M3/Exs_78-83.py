#Ex78
valores = []
maior_valor = 0

valores.append(int(input('Primeiro valor: ')))
valores.append(int(input('Segundo valor: ')))
valores.append(int(input('Terceiro valor: ')))
valores.append(int(input('Quarto valor: ')))
valores.append(int(input('Quinto valor: ')))

for valor in valores:
    if (valor > maior_valor):
        maior_valor = valor
    elif (valor ):
        menor_valor = valor
    

print('Lista completa: {}'.format(valores), end='\n')
print('Maior valor da lista: {}'.format(maior_valor), end='\n')
print('Menor valor da lista: {}'.format(menor_valor), end='\n')
