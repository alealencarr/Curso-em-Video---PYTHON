def notas(*n,sit=False):
    dicionario = {"total":len(n),"maior":max(n),"menor":min(n),"média":sum(n)/len(n)}
    if sit:
        if dicionario["média"] > 7:
            dicionario["situação"] = 'BOA'
        elif dicionario["média"] < 5:
            dicionario["situação"] = 'RUIM'
        else:
            dicionario["situação"] = 'RAZOÁVEL'
    return dicionario


resp = notas(2.5,1.5,10,1.5,sit=True)
print(resp)