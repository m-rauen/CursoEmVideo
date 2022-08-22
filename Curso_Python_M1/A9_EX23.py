numero = int(input('Informe um número de 0 a 9999: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 100 % 10

print('RESULTADO DO NÚMERO {}: \n'
      'Milhar: {}\n'
      'Centena: {}\n'
      'Dezena: {}\n'
      'Unidade:{}'.format(numero,unidade,dezena,centena,milhar))

