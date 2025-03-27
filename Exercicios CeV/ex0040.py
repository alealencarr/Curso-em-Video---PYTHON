n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
m = (n1+n2)/2
if m >= 7.0:
    print (f"\033[32mParabéns! Sua média é {m}, você está aprovado.\033[m")
elif m <= 5.0:
    print (f'\033[31mEstude mais! Sua média foi {m}, você está reprovado!\033[m')
elif m >= 5.0 and m <= 6.9:
    print (f'Sua média é {m}. Você está de recuperação.')
