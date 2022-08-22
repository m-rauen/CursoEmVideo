import math
ang=float(input('Digite qualquer ângulo em graus: '))
sn=math.sin(math.radians(ang))
cs=math.cos(math.radians(ang))
tg=math.tan(math.radians(ang))
print('='*60)
print('O seno de {} é igual a {:.2f} '.format(ang,sn))
print('O cosseno de {} é igual a {:.2f}'.format(ang,cs))
print('A tangente de {} é igual a {:.2f}'.format(ang,tg))
print('='*60)



