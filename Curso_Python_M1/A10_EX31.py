distancia = float(input('Informe a distância da viagem (em km): '))
if distancia <= 200:
    passagem = 0.50*distancia
    print('O preço da passagem é de R${:.2f}'.format(passagem))
else:
    passagem = 0.45*distancia
    print('O preço da passagem é de R${:.2f}'.format(passagem))