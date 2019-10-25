txt = "Leia muutuja abil etteantud tekstis olevate täishäälikute arv."
vowels = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
x = 0
i = 0

for x in txt.lower():
    if x in vowels:
        i = i + 1

print (i)

    
        
    