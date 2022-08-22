numero_1, numero_2, numero_3 = input('Informe 3 números inteiros quaisquer, separados por espaço: ').split()

numero_1 = int(numero_1)
numero_2 = int(numero_2)
numero_3 = int(numero_3)

menor = numero_1
maior = numero_3

if numero_2 < menor and numero_2 < numero_3:
    menor = numero_2
elif numero_3 < menor and numero_3 < numero_2:
    menor = numero_2

if numero_2 > maior and numero_2 > 1:
    maior = numero_2
elif numero_1 > maior and numero_1 > numero_2:
    maior = numero_1

print('RESULTADO: \n'
      'O maior número é: {}\n'
      'O menor número é: {} '.format(maior,menor))
