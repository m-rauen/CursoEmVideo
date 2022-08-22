frase = str(input('Informe uma frase qualquer: ')).strip().upper()
print('RESULTADO: \n'
      'A letra A aparece: {} vezes \n'
      'A primeira ocorrência da letra A é na posição {} \n'
      'A última ocorrência da letra A é na posição {}'.format(frase.count('A'),(frase.find('A')+1),(frase.rfind('A')+1)))