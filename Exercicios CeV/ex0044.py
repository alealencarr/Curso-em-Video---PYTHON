prod = float(input("Qual foi o valor das compras no total? R$"))
a = prod - (prod*0.1)
b = prod - (prod*0.05)
c = prod
d = prod * 1.2
pgto = str(input('''Qual a condição de pagamento?
[1] - Dinheiro/Cheque.
[2] - À vista no cartão.
[3] - Em 2x no cartão.
[4] - 3x ou mais no cartaõ.
Selecione: '''))
if pgto == "4":
    p = int(input("Serão em quantas vezes? "))
    z = d/p
    print("O valor total, com juros de 20% pelo parcelamento, ficará {:.2f}. Como você parcelou em {} vezes, cada parcela será no valor de R${:.2f}".format(d,p,z))
elif pgto == "2":
    print("Como você escolheu o pagamento à vista no cartão, ganhou um desconto de 5%. O valor total ficará R${:.2f}.".format(b))
elif pgto == "1":
    print("Como você escolheu pagar à vista no dinheiro/cheque, ganhou um desconto de 10%. O valor total será de R${:.2f}.".format(a))
elif pgto == "3":
    print("Para o pagamento em 2x o preço é o mesmo, R${:.2f}. Cada parcela ficará no valor de R${:.2f}.".format(c,c/2))
else:
    print("Opção invalida! Tente novamente. As opções disponiveis são:\n[1] - Dinheiro/Cheque\n[2] - À vista no cartão.\n[3] - Em 2x no cartão.\n[4] - 3x ou mais no cartaõ.")
