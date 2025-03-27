def aumentar(preço=0,taxa=0):
    aum = preço * (1+(taxa/100))
    return aum

def diminuir(preço=0,taxa=0):
    dim = preço * (1-(taxa/100))
    return dim

def dobro(preço=0):
    mult = preço*2
    return mult

def metade(preço=0):
    meio = preço/2
    return meio

def moeda(preço=0,moeda="R$"):
    return f'{moeda}{preço:.2f}'.replace('.',',')
