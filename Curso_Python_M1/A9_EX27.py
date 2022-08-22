nome_completo = str(input('Informe seu nome completo: ')).upper().strip()
nome_formatado = nome_completo.split()
print('-/'*20)
print('Prazer em te conhecer!')
print('Seu primeiro nome é: {}\n'
      'Seu último nome é: {} '.format(nome_formatado[0],nome_formatado[-1]))
print('-/'*20)