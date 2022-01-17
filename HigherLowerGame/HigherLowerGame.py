from art import logo, vs
from gameData import data
import random

def checkAnswer(firstPerson, secondPerson):
    firstPersonFollowers = firstPerson.get('follower_count')
    secondPersonFollowers = secondPerson.get('follower_count')

    if firstPersonFollowers > secondPersonFollowers:
        return "A"
    else:
        return "B"


print(logo)

score = 0
gameOver = False

while not gameOver:
    peopleToCompare = random.choices(data, k=2)
    firstPerson = peopleToCompare[0]
    secondPerson = peopleToCompare[1]
    correctAnswer = checkAnswer(firstPerson, secondPerson)

    print(f"A. {firstPerson.get('name')}, a {firstPerson.get('description')}, from {firstPerson.get('country')}")
    print(vs)
    print(f"B. {secondPerson.get('name')}, a {secondPerson.get('description')}, from {secondPerson.get('country')}")

    guess = input("Who do you think has more followers? (A/B) ").upper()

    if guess == correctAnswer:
        score += 1
        print("Correct!")
        print(f"Score: {score}\n")
    else: 
        print("Incorrect")
        print(f"Game Over. Final Score: {score}")
        gameOver = True

    