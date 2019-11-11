import random

def RPSgame():
    
    compChoice = random.randint(0,2)
    playerChoice = int(input("Valige 1:Kivi , 2:Paber , 3: Käärid")) - 1

    gamePlay = ["Kivi","Paber","Käärid"]
    gameWin =  ["Käärid","Kivi","Paber"]

    print ("Te valisite: " + gamePlay[playerChoice])
    print ("Arvuti valis: " + gamePlay[compChoice])

    playerEnemy = gameWin.index(gamePlay[compChoice])
    compEnemy = gameWin.index(gamePlay[playerChoice])

    if compChoice == playerChoice:
        print ("Viik")
    elif compChoice == compEnemy:
        print ("Võitis arvuti")
    elif playerChoice == playerEnemy:
        print ("Te võitsite")

playCond = 1

while playCond == 1:
    RPSgame()
    playCond = int(input("Kirjutage 1 kui soovite edasi mängida või 0 kui ei soovi"))
    
    




            

