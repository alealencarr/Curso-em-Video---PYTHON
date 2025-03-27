dicionario = {'nome':str(input('Nome do jogador: '))}
dicionario['partidas'] = int(input(f'Quantas partidas {dicionario["nome"]} jogou?'))
lista = []
soma = 0
for partida in range(0,dicionario['partidas']):
    lista.append(int(input(f'   Quantos gols na partida {partida}? ')))
dicionario['gols'] = lista.copy()
dicionario['total'] = sum(lista)
print('=-'*45)
print(dicionario)
print('=-'*45)
for k,v in dicionario.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-'*45)
print(f'O jogador {dicionario["nome"]} jogou {dicionario["partidas"]} partidas.')
for p in range (0,dicionario['partidas']):
    print(f'    => Na partida {p}, fez {dicionario["gols"][p]} gols.')
print(f'Foi um total de {dicionario["total"]} gols.')