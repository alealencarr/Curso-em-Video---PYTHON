import random
import time


lista = ["Pedra","Papel","Tesoura"]
computador = random.randint(0,2)
print('''Escolha uma das opções abaixo:
[0] - Pedra.
[1] - Papel.
[2] - Tesoura.''')
jogador = int(input("Digite a opção escolhida: "))
print('\033[1;31m¬-.'*6)
print("\033[1;31mJO\033[m")
time.sleep(1)
print("\033[1;31mKEN")
time.sleep(1)
print("\033[1;31mPÔ")
print('\033[1;31m¬-.'*6)
time.sleep(1)
print("\033[1;30mO COMPUTADOR ESCOLHEU: {}.\033[m\n\033[1;97mO JOGADOR ESCOLHEU: {}\033[m".format(lista[computador],lista[jogador]))
print('\033[1;36m¬-.'*6)
if jogador == 0: #pedra
    if computador == 1:
        print("O COMPUTADOR GANHOU!")
    elif computador == 2:
        print("O JOGADOR GANHOU!")
    elif computador == 0:
        print("EMPATE!")
if jogador == 1: #papel
    if computador == 0:
        print("O COMPUTADOR GANHOU!")
    elif computador == 2:
        print("O JOGADOR GANHOU!")
    elif computador == 1:
        print("EMPATE!")
if jogador == 2: #tesoura
    if computador == 0:
        print("O COMPUTADOR GANHOU!")
    elif computador == 1:
        print("O JOGADOR GANHOU!")
    elif computador == 2:
        print("EMPATE!")


