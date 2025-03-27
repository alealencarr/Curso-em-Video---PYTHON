print('-'*30)
print('{:^30}'.format(' LOJA SUPER BARATÃO '))
print('-'*30)
soma = contador = quant = 0
nomemenor = ''
while True:
    nomeprod,preco = str(input('Nome do produto: ')),float(input('Preço: R$'))
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    soma += preco
    quant += 1
    if preco > 1000:
        contador += 1
    if quant == 1:
        menor = preco
        nomemenor = nomeprod
    else:
        if preco < menor:
            menor = preco
            nomemenor = nomeprod
    if continuar == 'N':
        break
print(f"""O total gasto na compra foi R${soma:.2f}
No total {contador} produto(s) custaram mais de R$ 1000.00
E o nome do produto mais barato é {nomemenor} e ele custou R${menor:.2f}.""")

