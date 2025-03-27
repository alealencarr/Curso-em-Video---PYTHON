def leiaDinheiro(dinheiro):
    dinheiro = input(dinheiro).strip()
    while True:
        if dinheiro.isnumeric():
            if ',' in dinheiro:
                dinheiro = dinheiro.replace(',','.')
                return dinheiro
            else:
                return dinheiro
        else:
            return f'Erro! \"{dinheiro}\" é um preço inválido!'