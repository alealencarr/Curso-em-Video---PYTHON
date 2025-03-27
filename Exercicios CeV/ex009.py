alt = float(input("Digite sua altura em metros:"))
km = alt/1000
hm = alt/100
dam = alt/10
dm = alt*10
cm = alt*100
mil = cm*10
print("Você tem:{} metros, {} centimetros, {} milímetros. Se transformarmos em KM: {}, HM {}, DAM {}, DM {}".format(alt, cm, mil, km, hm, dam, dm))
