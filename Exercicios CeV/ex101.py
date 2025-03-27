def vota(anodenasc):
    from datetime import date
    anoatual = date.today().year
    anovoto = anoatual - anodenasc
    if anovoto >= 18 and anovoto < 65:
        return f'Com {anovoto} anos: VOTO OBRIGATORIO.'
    if anovoto == 16 or anovoto == 17 or anovoto > 65:
        return f'Com {anovoto} anos: VOTO OPCIONAL.'
    else:
        return f'Com {anovoto} anos: NÃO VOTA.'


print('-'*25)
print(vota(2001))
