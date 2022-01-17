import random

print("Welcome to the Number Guessing Game\nI'm thinking of a number between 1 and 100.")
diffculty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if diffculty == 'easy' or diffculty == 'e':
    attemptsLeft = 10
    print("You have 10 attempts to guess the number")
else: 
    attemptsLeft = 5
    print("You have 5 attempts to guess the number")

number = random.randint(1, 100)
validAnswers = list(range(1,101))

gameOver = False
while not gameOver: 
    guess = int(input("Guess a number: "))
    while guess not in validAnswers:
        guess = int(input("Oops, that's not valid. Try again. Guess a number from 1 to 100: "))

    if guess > number: 
        attemptsLeft -= 1
        print(f"Too high. You have {attemptsLeft} attempts left")
    elif guess < number:
        attemptsLeft -= 1
        print(f"Too low. You have {attemptsLeft} attempts left")
    elif guess == number:
        print(f"{number} was the number. You win!")
        gameOver = True

    if attemptsLeft < 1:
        print("You ran out of guesses. Game Over")
        gameOver = True

