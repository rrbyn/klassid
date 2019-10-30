import random

goal = (random.randint(0, 100))
currentGuess = -1
tries = 0

while currentGuess != goal:
    currentGuess = int(input("Mis arvu ma välja mõtlesin 0 - 100?: "))
    tries = tries + 1
    if currentGuess < goal:
        print("Vastus on pakkumisest suurem")
    elif currentGuess > goal:
        print("Vastus on pakkumisest väiksem")
    
if currentGuess == goal:
    print ("Olete võitnud! Teil läks vaja " + str(tries) + " pakkumist")
    
        
    
    
