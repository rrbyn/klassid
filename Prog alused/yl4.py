a = int(input("Sisestage esimene arv: "))
b = int(input("Sisestage teine arv: "))
c = int(input("Sisestage kolmas arv: "))
if a < b < c:
    print ("Maksimum on: "+ str(c))
elif a < b > c:
    print ("Maksimum on: "+ str(b))
else:
    print ("Maksimum on: "+ str(a))
    