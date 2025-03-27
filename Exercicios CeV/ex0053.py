'''fr = str(input("Digite uma frase: ")).strip()
a = fr.replace(' ','')
c = a[::-1]
print('O inverso de {}, é {}.'.format(a,c))
if a == c:
    print('A frase  é um palindromo.')
else:
    print('Não é um palindromo')
print (c)'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''
for letra in range(len(juntar)-1,-1,-1):
    inverso = inverso + juntar[letra]
print(f'O inverso de {juntar} é {inverso}.')
if inverso == juntar:
    print('Temos um palindromo')
else:
    print("A frase não é um palindromo")
