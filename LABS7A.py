import random

print("Hello! Welcome to the Rock Paper Scissors Program!")
count_q=0
count_p=0
champ= False

while champ == False:
    print("")
    print("Press 1 for Rock.")
    print("Press 2 for Paper.")
    print("Press 3 for Scissors.")

    PLAYER = int(input("What would you like to play?"))
    ComputerInput = random.randint(1,3)

    if (PLAYER == 1) and (ComputerInput == 1):
        champ= False
        PLAYER=win & ComputerInput=lose
        count_q=count_q+0
        print("It's a draw; you both played Rock!")
        
    if (PLAYER == 2) and (ComputerInput == 1):
        champ == True
        print("You win! The computer played Rock!")

    if (PLAYER== 3) and (ComputerInput == 1):
        champ== True
        print("You lose! The computer played Rock!")
        
    if (PLAYER == 1) and (ComputerInput == 2):
        champ = True
        print("You lose! The computer played Paper!")
        
    if (PLAYER == 2) and (ComputerInput == 2):
        champ== False
        print("It's a draw; the computer played Paper!")

    if (PLAYER == 3) and (ComputerInput == 2):
        champ== True
        print("You win! The computer played Paper!")
        
    if (PLAYER == 1) and (ComputerInput == 3):
        champ= True
        print("You win! The computer played Scissors!")
        
    if (PLAYER == 2) and (ComputerInput == 3):
        champ == True
        print("You lose! The computer played Scissors!")

    if (PLAYER == 3) and (ComputerInput == 3):
        champ == False
        print("It's a draw; the computer played Scissors!")