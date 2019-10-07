first_name = input("Sisestage nimi: ")
print("Tere, " + first_name.capitalize())
elukoht = input("Sisestage elukoht: ")
elukoht = elukoht.strip()
if elukoht.lower() == "saaremaa":
    print("Loodetavasti ei olnud praamijärjekord liiga pikk.")
else:
    print("Ei tunne kohta nimega " + elukoht)
vanus = int(input("Sisestage vanus: "))
if vanus < 18 :
    print("Te olete liiga noor, et autot juhtida")
elif vanus > 18 :
    print("Te võite autot juhtida")
else:
    print("Õnnitlused täisealiseks saamise puhul")