def leiaDinheiro(msg):
    vermelho = '\033[0;31m'
    fimcor = '\033[m'
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'{vermelho}ERRO! \"{entrada}\" é um preço inválido.{fimcor}')
        else:
            valido = True
            return float(entrada)


