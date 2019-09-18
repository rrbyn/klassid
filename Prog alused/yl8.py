year = int(input("Sisestage aastaarv: "))
if (year % 4) == 0 and (year % 100) != 0:
    print("Aasta on liigaasta") 
else:
    print("Aasta on lihtaasta")