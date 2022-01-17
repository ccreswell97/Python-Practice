#
# Higher Lower Game
# Guess if a user has more followers, keep going until you get one wrong
# The second option becomes the first option after each correct answer
#

from art import logo, vs
from gameData import data
import random
import os

def cls():
    os.system("cls" if os.name == "nt" else "clear")

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

peopleToCompare = random.choices(data, k=2)
firstPerson = peopleToCompare[0]
secondPerson = peopleToCompare[1]

while not gameOver:
    secondPerson = random.choice(data)
    correctAnswer = checkAnswer(firstPerson, secondPerson)

    print(f"A. {firstPerson.get('name')}, {firstPerson.get('description')}, from {firstPerson.get('country')}")
    print(vs)
    print(f"B. {secondPerson.get('name')}, {secondPerson.get('description')}, from {secondPerson.get('country')}")

    guess = input("Who do you think has more followers? (A/B) ").upper()

    if guess == correctAnswer:
        cls()
        score += 1
        print("Correct!")
        print(f"Score: {score}\n")
        firstPerson = secondPerson
    else: 
        print("Incorrect")
        print(f"Game Over. Final Score: {score}")
        gameOver = True

    