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

def resumo(p=0,aum=10,dim=5):
    print('-'*33)
    print(f'{"RESUMO DO VALOR":^33}')
    print('-'*33)
    print(f'{"Preço analisado:":<20}{moeda(p):>10}')
    print(f"{'Dobro do preço:':<20}{dobro(p,True):>10}")
    print(f"{'Metade do preço:':<20}{metade(p,True):>10}")
    print(f"{f'{aum}%'' de aumento:':<20}{aumentar(p,aum,True):>10}")
    print(f"{f'{dim}%'' de redução:':<20}{diminuir(p,dim,True):>10}")
    print('-' * 33)
