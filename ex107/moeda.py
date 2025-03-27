def aumentar(preço,taxa):
    aum = preço * (1+(taxa/100))
    return aum

def diminuir(preço,taxa):
    dim = preço * (1-(taxa/100))
    return dim

def dobro(preço):
    mult = preço*2
    return mult

def metade(preço):
    meio = preço/2
    return meio