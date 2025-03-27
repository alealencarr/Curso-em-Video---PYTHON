from random import randint
from time import sleep
from operator import itemgetter
dicionario = {}
for valor in range(1,5):
    dicionario[f'jogador{valor}'] = randint(1,6)
print(f'{"Valores Sorteados:"}')
for chave, valores in dicionario.items():
    print(f'    O {chave} tirou {valores} no dado.')
    sleep(1)
ranking = []
ranking = sorted(dicionario.items(),key=itemgetter(1),reverse=True)
print('Ranking dos jogadores:')
for indice,jog in enumerate(ranking):
    print(f'    {indice+1}° lugar: {jog[0]} com {jog[1]}')
    sleep(1)
