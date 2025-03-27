from random import *
computador = randint(0,10)
print("""Sou seu computador... Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?""")
acertou = False
contador = 0
while not acertou:
    jogador = int(input("O computador pensou em um número tente adivinhar qual número foi:"))
    contador += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        if jogador > computador:
            print('Menos... tente mais uma vez.')
print('Acertou! Mas para acertar você teve que tentar {} vezes.'.format(contador))

'''from random import *
computador = randint(0,10)
print('Oi! Sou seu computador e vou pensar em um número...')
jogador = int(input('Tente adivinhar o número que o computador pensou: '))
contador = 1
if jogador != computador:
    if jogador > computador:
        print ('Muito alto. Tente outra vez. ')
    if jogador < computador:
        print('Muito baixo. Tente outra vez. ')
    jogador = int(input('Tente adivinhar o número outra vez: '))
    contador += 1
print('Parabéns. Você acertou, porém, para acertar precisou de {} chances.'.format(contador))'''

