ano_teste = int(input('Informe um ano qualquer a ser analisado: '))
if ano_teste % 4 == 0 and ano_teste % 100 != 0:
    print('{} é ano bissexto! '.format(ano_teste))
else:
    print('{} não é ano bissexto!'.format(ano_teste))