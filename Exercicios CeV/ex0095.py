jogadores = []
soma = 0
while True:
    print('--'*15)
    dicionario = {'nome':str(input('Nome do jogador: '))}
    dicionario['partidas'] = int(input(f'Quantas partidas {dicionario["nome"]} jogou? '))
    lista = []
    for partida in range(0, dicionario['partidas']):
        lista.append(int(input(f'   Quantos gols na partida {partida+1}? ')))
    dicionario['gols'] = lista.copy()
    dicionario['total'] = sum(lista)
    jogadores.append(dicionario.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Digite: [S/N]')
    if continuar == 'N':
        break
print('=-'*30)

print(f'{"cod":<6}{"nome":<18}{"gols":<15}{"total":>10}')
print('--'*27)
# Forma de retorno para os valores
# for i, v in enumerate(jogadores):
#     print(i)
#     for valor in v.values():
#         print(valor)
for jogador in range(0,len(jogadores)):
    print(f'{jogador:<6}{jogadores[jogador]["nome"]:<18}{str(jogadores[jogador]["gols"]):<15}{jogadores[jogador]["total"]:>10}')
while True:
    print('--'*20)
    while True:
        dados = int(input('Mostrar dados de qual jogador?'))
        if dados == 999:
            break
        if dados > len(jogadores) - 1:
            print('Jogador invalido. Digite novamente.')
        else:
            break
    if dados == 999:
            break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[dados]["nome"]} --')
    #for i,g in enumarate(jogadores[dados]["gols"]:
    #   print(f'    No jogo {i+1} fez {g} gols.')
    for jogo in range(0,len(jogadores[dados]['gols'])):
        print(f'    No jogo {jogo+1} fez {jogadores[dados]["gols"][jogo]}')
print('<< ENCERRRANDO >>')
