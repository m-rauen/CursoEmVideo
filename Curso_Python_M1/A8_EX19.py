import random
n1=str(input('Digite o nome do primeiro aluno: '))
n2=str(input('Digite o nome do segundo aluno: '))
n3=str(input('Digite o nome do terceiro aluno: '))
n4=str(input('Digite o nome do quarto aluno: '))
l=[n1,n2,n3,n4]
sort=random.choice(l)
print('A pessoa sorteada foi: {}'.format(sort))
