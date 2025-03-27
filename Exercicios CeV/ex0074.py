from random import randint
tup = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('Números da tupla: ',end='')
for num in tup:
    print(f'{num} ',end='')
print(f'\nO maior valor é {max(tup)}')
print(f'O menor valor é {min(tup)}')

# from random import randint
# n = (randint(0, 10), randint(0, 10), randint(0, 10),
#      randint(0, 10), randint(0, 10))
# print(f'Os números sorteados foram: {n}')
# cont = 0
# maior = 0
# menor = 5
# while True:
#     for r in range(0, 5):
#         if maior <= n[r]:
#             maior = n[r]
#         if menor >= n[r]:
#             menor = n[r]
#     cont += 1
#     if cont == 5:
#         break
# print(f'O maior é {maior} e o menor é {menor}')
