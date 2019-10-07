a = input("Sisestage esimene arv: ")
b = input("Sisestage teine arv: ")
c = input("Sisestage kolmas arv: ")
if a.isdigit() and b.isdigit() and c.isdigit():
    a = int(a)
    b = int(b)
    c = int(c)
    
    if a < b < c:
        print ("Maksimum on: "+ str(c))
    elif a < b > c:
        print ("Maksimum on: "+ str(b))
    else:
        print ("Maksimum on: "+ str(a))
else:
    print("Palun sisestage täisarv")