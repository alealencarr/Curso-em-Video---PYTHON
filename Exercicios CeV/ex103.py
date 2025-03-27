def ficha(nome='<desconhecido>', gols =0):
    nome = str(input('Nome do jogador: ')).strip()
    if nome == '':
        nome = '<desconhecido>'
    gols = str(input('Número de Gols: '))
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    frase = print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    return frase


ficha()
