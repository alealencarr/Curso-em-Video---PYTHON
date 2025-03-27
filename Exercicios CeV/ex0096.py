azul = "\033[34m"
vermelho = "\033[31m"
fimcor = "\033[m"
def area(l,c):
    print(f'{vermelho}A área de um terreno {l} x {c} é de {l*c}m²{fimcor}')


print(f'{azul}{"CONTROLE DE TERRENOS":^20}{fimcor}')
print('-'*20)
area(l = float(input('LARGURA (m): ')),
    c = float(input('COMPRIMENTO (m): ')))