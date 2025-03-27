'''ano = int(input("Digite um ano:"))
div1 = ano/4
div2 = ano/100
div = ano/400
rest = div1%2
if rest == 0:
    if div1 == int(div1):
        print("Ano bissexto!")
    else:
        if div2 == float(div2):
            print("O ano é bissexto")
        else:
            if div == int(div):
                print("O ano é bissexto")
        print("O ano não é bissexto!")
else:
    print("Não é bissexto.")'''

import datetime
ano = int(input("Qual ano você quer analisar? Coloque 0 para o ano atual:"))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print("O ANO {} É BISSEXTO.".format(ano))
else:
    print("O ANO {} NÃO É BISSEXTO.".format(ano))
    



