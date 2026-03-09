print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

Direction = input("You're at a crossroad.\nPress L for Left and R for Right. Good luck adventurer: ")

if Direction == "L":
    print("You arrive at a lake ")
    S_or_W = input("At this lake there is an island."
                   "Type S to swim and W to wait for a boat: ")

    if S_or_W == "W":
        print("A boat arrives and picks up and drops you off in front of a door")
        Door = input("There are 3 doors. Choose carefully."
                     "Y for yellow, B for blue, or R for red ")

        if Door == "Y":
            print("Congrats adventurer. You found the treasure")
        elif Door == "B":
            print("you picked the wrong door. Game over")
        elif Door == "R":
            print("you picked the wrong door. Game over")
        else:
            print("invalid")

    elif S_or_W == "S":
        print("You get roughly halfway before a shark eats you alive. Game Over!")
    else:
        print("invalid")

elif Direction == "R":
    print("Game Over")
else:
    print("Invalid")






