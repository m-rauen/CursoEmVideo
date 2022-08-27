def aumentar(preco = 0, taxa = 0):
    valor_final = preco + (preco * taxa/100)
    return valor_final

def diminuir(preco = 0, taxa = 0):
    valor_final = preco - (preco * taxa/100)
    return valor_final

def dobro(preco = 0):
    valor_final = preco * 2
    return valor_final

def metade(preco = 0):
    valor_final = preco / 2
    return valor_final

def moeda(preco = 0, moeda = 'R$'):
    return ('{}{}'.replace('.', ',').format(moeda, preco))