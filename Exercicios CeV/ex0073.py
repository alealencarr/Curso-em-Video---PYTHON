tabelabrasileirao = ('Santos','Atletico-MG','Corinthians', 'Cuiabá', 'Internacional', 'Avaí','Bragantino','Palmeiras','Flamengo','Coritiba',
                     'São Paulo','Botafogo','Fluminense','América-MG','Ceará','Athletico-PR','Atletico-PR','Atlético-GO','Goiás','Juventude','Fortaleza')
print('-='*30)
print(f'Lista de timess do Brasileirão: {tabelabrasileirao}')
print('-='*30)
print(f'Os cinco primeiros são {tabelabrasileirao[0:5]}')
print('-='*30)
print(f'Os quatro ultimos são {tabelabrasileirao[-4:]}')
print('-='*30)
print(f'Em ordem alfabética os times ficam assim: {sorted(tabelabrasileirao)}')
print('-='*30)
print(f'O Palmeiras está na {tabelabrasileirao.index("Palmeiras")+1}a posição.')


