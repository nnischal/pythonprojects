print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Jumanji: Welcome to the jungle!!  ")
to_play = input("To play the game! Please enter.. Y or N. ")
if to_play == 'Y'or to_play == 'y':
    print("Please select your gender to play the game! ")
    gender = input("Enter your gender: M =Male or F= female ?? \n")
    if gender == 'M' or gender == 'm':
        character = input("You have chosen to play the game with Male. \n Please select your character to play the game.---------> \n 1. Dr. Xander \n 2. Franklin \n")
        if character == '1':
            name = character
            input("You have chosen to play the game with the: \n Dr. Xander 'Smolder' Bravestone a strong, confident archaeologist and explorer. ")
        else:
            name = character
            input("You have chosen to play the game with the: \n Franklin 'Mouse' Finbara diminutive zoologist and weapons carrier. ")
    else:
        name = input("You have chosen to play the game with Female. \n Please select your character to play the game.---------> \n 1. Shelly \n 2. Ruby \n")
        if character == '1':
            name = character
            input("You have chosen to play the game with the male character: \n Professor Sheldon 'Shelly' Oberon, an expert in many scientific fields including cartography ")      
        else:
            name = character
            input("You have chosen to play the game with the female character: \n Ruby Roundhouse, a scantily-clad commando ")
    
        
else:
    print("Thank you for playing the game!")
    