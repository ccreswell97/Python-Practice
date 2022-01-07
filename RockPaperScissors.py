import random

print("Welcome to Rock, Paper, Scissors\n")
userRpsChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

computerRpsChoice = random.randint(0,2)

while userRpsChoice not in range(0,3):
    userRpsChoice = int(input("Oops, that's not valid. Try again.\nType 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

rpsDict = {
    0 : '''
        _______
    ---'   ____)
        _(_____)
        _(_____)
        __(____)
    ---.__(___)
    ''',

    1 : '''
        _______
    ---'   ____)__
            ______)
            _______)
            _______)
    ---.__________)
    ''',

    2 : '''
        _______
    ---'   ____)__
            ______)
        __________)
        (____)
    ---.(___)
    '''
}

print("\nYou chose: {}".format(rpsDict.get(userRpsChoice)))
print("Computer chose: {}".format(rpsDict.get(computerRpsChoice)))

if userRpsChoice == computerRpsChoice:
    print("That's a draw!")
else:
    if userRpsChoice == 0:
        #rock 
        if computerRpsChoice == 1:
            #paper
            print("You lose.")
        else:
            #scissors
            print("You win!")
    elif userRpsChoice == 1:
        #paper
        if computerRpsChoice == 0:
            #rock
            print("You win!")
        else:
            #scissors
            print("You lose.")
    else:
        #scissors
        if computerRpsChoice == 0:
            #rock
            print("You lose.")
        else:
            #paper
            print("You win!")
