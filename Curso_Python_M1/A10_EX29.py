velocidade = float(input('Informe a sua velocidade (em km/h): '))
if velocidade > 80:
    multa = (velocidade-80)*7
    print('Infelizmente, você foi multado! Limite da via de: 80 km/h \n'
          'Sua multa é de: R${:.2f}'.format(multa))
else:
    print('Você não foi multado!')