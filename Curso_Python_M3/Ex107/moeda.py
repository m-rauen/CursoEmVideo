def aumentar(preco, taxa):
    valor_final = preco + (preco * taxa/100)
    return valor_final

def diminuir(preco, taxa):
    valor_final = preco - (preco * taxa/100)
    return valor_final

def dobro(preco):
    valor_final = preco * 2
    return valor_final

def metade(preco):
    valor_final = preco / 2
    return valor_final
    