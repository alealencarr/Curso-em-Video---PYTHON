from random import randint
import time
print('-'*40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-'*40)
pergunta = int(input('Quantos jogos você quer que eu sorteie? '))
megasena = []
temporaria = []
for bilhete in range(0,pergunta):
    for numero in range(0,6):
        while len(temporaria) <= 5:
            valor = randint(1, 60)
            if valor not in temporaria:
                temporaria.append(valor)
            temporaria.sort()
    megasena.append(temporaria[:])
    temporaria.clear()
print('=-'*5,f' SORTEANDO {pergunta} JOGOS ','=-'*5)
for ind, jogo in enumerate(megasena):
    print(f'JOGO {ind+1}: {jogo}')
    time.sleep(1)
print('-='*5,'< BOA SORTE >','=-'*5)

