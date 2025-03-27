print("\033[1;97;40m*-*\033[m"*12)
print("\033[1;32;40mVENHA SIMULAR SEU EMPRESTIMO CONOSCO\033[m")
print("\033[1;97;40m*-*\033[m"*12)
print(" ")
print(" ")
vc = float(input("Qual é o valor da casa?\nR$ "))
sal = float(input("Qual é o seu salário?\nR$ "))
anos = int(input("Em quantos anos você deseja pagar?\nR: "))
mes = anos*12
prest = vc/mes
exc = sal*0.3
min = (prest/3) * 10
print("O valor da parcela é {:.2f}.".format(prest))
if prest <= exc:
    print("\033[1;32mEMPRÉSTIMO APROVADO! O VALOR DA PARCELA MENSAL É DE R$ {:.2f}.\033[m".format(prest))
else:
    print("\033[1;31mEMPRÉSTIMO NEGADO! PARA QUE VOCÊ CONSIGA COMPRAR A CASA, DEVE TER UM SALÁRIO DE NO MINIMO R$ {:.2f}.\033[m".format(min+0.10))


