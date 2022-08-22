import math
from math import pow
from math import sqrt

co=float(input('Digite o comprimento do cateto oposto: '))
ca=float(input('Digite o comprimento do cateto adjacente: '))
h=sqrt(pow(co,2)+pow(ca,2))
print('A hipotenusa desse triângulo tem {} de comprimento'.format(math.ceil(h)))

#hip=math.hypot(co,ca)
