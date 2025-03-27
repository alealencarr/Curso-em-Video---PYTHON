import datetime
ano = datetime.date.today().year
ano2 = int(input("Qual é o ano do seu nascimento? "))
sub = ano - ano2
hora = 18
print (f"Você tem {sub} anos.")
if sub == 18:
    print("Está na hora de você se alistar!")
elif sub > 18:
    print(f"Já passou o tempo de alistamento! Já se passaram {(sub-hora)} anos. O seu alistamento deveria ter ocorrido no de {ano-(sub-hora)}")
elif sub < 18:
    print(f"Ainda não está na hora de você se alistar para serviço militar. Faltam {(sub-hora)*(-1)} anos. O seu alistamento será no ano de {ano+((sub-hora)*(-1))}")


