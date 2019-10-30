import random

compChoice = random.randint(0,2)
playerChoice = int(input("Valige 1:Kivi , 2:Paber , 3: Käärid")) - 1

gamePlay = ["R","P","S"]
gameWin =  ["S","R","P"]

print ("playerchoice: " + str(playerChoice))
print ("compChoice: " + str(compChoice))

#gamePlayC = gamePlay[compChoice]
#gamePlayP = gamePlay[playerChoice]

if compChoice == playerChoice:
    print ("Viik")
elif gamePlay[compChoice] == gameWin[compChoice]:
    print ("Võitis arvuti")
elif gamePlay[playerChoice] == gameWin[playerChoice]:
    print ("Võitis inimene")
else:
    print (playerChoice)
    print (compChoice)
    print ("Machine broke")
  
    


    
