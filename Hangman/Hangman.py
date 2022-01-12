import random
from HangmanArt import stages, logo
from HangmanWords import wordList

print(logo)
lives = len(stages)
wordPicked = random.choice(wordList)
wordBlanks = ["_" for i in wordPicked]
userGuesses = []

print(" ".join(wordBlanks))

gameOver = False

while not gameOver:
    letterGuess = input("\nGuess a letter: ").lower()
  
    if letterGuess in userGuesses:
      print("You've already guessed that letter")
      continue

    userGuesses.append(letterGuess)
        
    for position in range(len(wordPicked)):
        letter = wordPicked[position]
        if letterGuess == letter:
            wordBlanks[position] = letter
    
    if letterGuess not in wordPicked:
      lives -= 1
      print("{} is not in the word.".format(letterGuess))
      print(stages[lives])

    print(" ".join(wordBlanks))
    if "_" not in wordBlanks:
        print("You win!")
        gameOver = True

    if lives == 0:
        print("You lost. The word was {}".format(wordPicked))
        gameOver = True