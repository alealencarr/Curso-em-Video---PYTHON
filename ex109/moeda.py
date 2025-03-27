def aumentar(preço=0,taxa=0,form=False):
    aum = preço * (1+(taxa/100))
    if form:
        return moeda(aum)
    else:
        return aum

def diminuir(preço=0,taxa=0,form=False):
    dim = preço * (1-(taxa/100))
    if form:
        return moeda(dim)
    else:
        return dim

def dobro(preço=0,form=False):
    mult = preço*2
    if form:
        return moeda(mult)
    else:
        return mult

def metade(preço=0,form=False):
    meio = preço/2
    if form:
        return moeda(meio)
    else:
        return meio

def moeda(preço=0,moeda="R$"):
    return f'{moeda}{preço:.2f}'.replace('.',',')
