num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)}', 'vez' if num.count(9) == 1 else 'vezes' )
if 3 in num:
       print(f'O valor 3 apareceu na {num.index(3)+1}a posição.' )
else:
       print('O valor 3 não foi digitado.')
print('Os valores pares digitados: ',end='')
for div in num:
       if div % 2 == 0:
              print(f'{div} ', end='')

