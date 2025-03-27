t1 = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze',
      'treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    perg = int(input("Digite um número entre 0 e 20: "))
    while perg < 0 or perg > 20:
        perg = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    print(f"Você digitou o número {t1[perg]}.")
    perg1 = ' '
    while perg1 not in 'SN':
        perg1 = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    if perg1 == 'N':
        break
print('Obrigado!!')
