cid = str(input("Qual cidade você mora? ")).strip()
tit = cid.title()
print ("Você mora na cidade de: {}".format(tit))
sep = tit.split()
santo = ("Santo" in sep[0])
print ("Sua cidade começa com Santo: {};".format(santo))


