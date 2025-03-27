soma = 0
contador = 0
while True:
    valor = int(input('Digite um valor (999 para parar):'))
    if valor == 999:
        break
    soma += valor
    contador += 1
print('Você digitou {} números e a soma entre eles é: {}.'.format(contador,soma))
