def leiaInt(msg):
    vermelho = '\033[0;31m'
    fimcor = '\033[m'
    msg = input(msg)
    while True:
        if msg.isdigit():
            return msg
        else:
            print(f"{vermelho}Erro digite um número.{fimcor}")
            msg = input('Digite um número: ')


a = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {a}')

