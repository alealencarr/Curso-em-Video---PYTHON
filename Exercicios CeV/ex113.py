def leiaInt(msg):
    vermelho = '\033[0;31m'
    fimcor = '\033[m'
    while True:
        try:
            entrada = int(input(msg))
        except (ValueError,TypeError):
            print(f"{vermelho}Erro: por favor, digite um número inteiro válido.{fimcor}")
            continue
        except KeyboardInterrupt:
            print(f'\n{vermelho}Entrada de dados foi interrompida pelo usuario.{fimcor}')
            return 0
        else:
            return entrada


def leiaFloat(msg):
    vermelho = '\033[0;31m'
    fimcor = '\033[m'
    while True:
        try:
            entrada = float(input(msg))
        except (TypeError,ValueError):
            print(f"{vermelho}Erro: por favor, digite um número real válido.{fimcor}")
            continue
        except KeyboardInterrupt:
            print (f'\n{vermelho}Entrada de dados foi interrompida pelo usuario.{fimcor}')
            return 0
        else:
            return entrada


b = leiaInt('Digite um Inteiro: ')
a = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi o {b} e o real foi {a}.')