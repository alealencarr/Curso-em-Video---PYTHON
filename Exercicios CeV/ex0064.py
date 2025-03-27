numero = int(input('Digite um número [999 para parar]: '))
conte = 1
soma = numero
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero < 999:
        soma += numero
        conte +=1
print('Você digitou {} números e a soma entre eles foi {}.'.format(conte,soma))
