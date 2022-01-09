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
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

crossRoadsChoice = input("You're at fork in the road. Do you go left or right? ").lower()
validCrossRoadsOptions = ["left", "right", "l", "r"]
while crossRoadsChoice not in validCrossRoadsOptions:
    crossRoadsChoice = input("Oops, that wasn't a valid choice. Try again (left, right): ")

if crossRoadsChoice == "left" or crossRoadsChoice == "l": 
    print("You chose left.")
    swimChoice = input("You walk until you come to a lake. There's an island in the middle. Do you swim to the island or wait for someone to come around with a boat? (Swim/Wait) ").lower()
    
    validSwimOptions = ["swim", "wait", "s", "w"]
    while swimChoice not in validSwimOptions:
        swimChoice = input("Oops, that wasn't a valid choice. Try again (swim/wait): ")

    if swimChoice == "wait":
        print("You choose to wait for a boat. You camp out, and an old fisherman takes you out to the island in his small boat first thing in the morning.")
        doorChoice = input("You find a building on the island, and there is a staircase inside that leads down. You walk down for a long time, and finally reach the bottom.\nYou find 3 doors. Do you open the red, yellow, or blue door? ").lower()

        validDoorOptions = ["yellow", "red", "blue", "y", "r", "b"]
        while doorChoice not in validDoorOptions:
            doorChoice = input("Oops, that wasn't a valid choice. Try again (red/yellow/blue): ")

        if doorChoice == "yellow":
            print("You open the yellow door and enter the room. After killing a few spiders and removing some cobwebs, you see a small door built into the floor. You pull it open and find the treasure chest!\nYou win the game!")
        elif doorChoice == "red":
            print("You open the red door. A fireball shoots out, burning you badly.\nGame Over")
        else:
            print("You open the blue door and walk in. A trap door opens up underneath you and you fall down into a pit.\nGame Over")
    else:
        print("You chose to swim to the island. It's farther than it looks, and the Lake Monster attacks you.\nGame Over.")
else:
    print("You chose right.\nYou walk for a while and then stumble into a well-hidden trap. You plummet to the bottom of a hole.\nGame Over.")
