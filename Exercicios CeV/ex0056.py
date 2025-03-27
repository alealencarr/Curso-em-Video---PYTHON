soma = 0
maior = 0
contar = 0
nomehomem = ''
for pessoas in range(1,5):
    print('----- PESSOA {} ----'.format(pessoas))
    p1=str(input('Nome: '))
    p2=int(input('Idade: '))
    p3=str(input('Sexo [M/F]: '))
    soma += p2
    if pessoas == 1 and p3 == 'M' or p3 == 'm':
        maior = p2
        nomehomem = p1
    else:
        if p3 == 'M' or p3 == 'm' and p2>maior:
            maior = p2
            nomehomem = p1
    if p3 == 'F' and p2 <= 20:
        contar = contar +1
print ("A média de idade do grupo é de {:.1f} anos.".format(soma/4))
print ("Ao todo são {} mulheres com menos de 20 anos.".format(contar))
print ('O homem mais velho tem {} anos e se chama {}.'.format(maior,nomehomem))
f