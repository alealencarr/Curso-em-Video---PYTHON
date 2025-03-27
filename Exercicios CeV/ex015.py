aluguelcarro=float(input("Quantos KM você percorreu? "))
diasaluguel=int(input("Quantos dias você alugou? "))
custodia= 60*diasaluguel
custokm= 0.15*aluguelcarro
totalcusto = custodia+custokm
print("Você utilizou o veiculo por {} dias e percorreu {:.2f}KM. Isso te custou R${} pelo aluguel do carro e R${:.2f} pelo total de KM rodados.\nUm custo total de R${:.2f}.".format(diasaluguel,aluguelcarro,custodia,custokm,totalcusto))
