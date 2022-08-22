lado_1, lado_2, lado_3 = input('Informe, separado por espaço, a medida de cada um dos lados (em metros): ').split()

lado_1 = float(lado_1)
lado_2 = float(lado_2)
lado_3 = float(lado_3)

if (lado_2+lado_3) > lado_1 and (lado_1+lado_3) > lado_2 and (lado_1+lado_2) > lado_3 :
    print('Parabéns, você conseguiu formar um triângulo!')
else:
    print('Infelizmente, essas medidas não formarão um triângulo!')