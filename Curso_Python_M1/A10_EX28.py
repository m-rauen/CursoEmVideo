import random
from time import sleep

print('=-'*20)
print('IREI PENSAR EM UM NÚMERO DE 0 A 5 ...',)
print('=-'*20)

numero_alternativa = int(input('Em que número eu pensei? '))
numero_sorteado = random.randrange(0, 5)

print('PROCESSANDO ... ') # apenas para fazer uma gracinha no jogo
sleep(2)  # sleep de 2 segundos no terminal

if numero_alternativa == numero_sorteado:
    print('Parábens, você venceu!')
    print(numero_sorteado , ' = ', numero_alternativa)
else:
    print('Infelizmente, você perdeu')
    print(numero_alternativa, ' ≠ ', numero_sorteado)