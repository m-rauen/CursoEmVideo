salario_atual = float(input('Informe seu salário atual (em R$): '))

if salario_atual > 1250:
    salario_atual += (salario_atual*0.10)
    print('Seu salário após reajuste é de R${:.2f}'.format(salario_atual))
else:
    salario_atual += (salario_atual*0.15)
    print('Seu salário após reajuste é de R${:.2f}'.format(salario_atual))