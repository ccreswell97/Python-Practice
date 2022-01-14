# 3 Card Blackjack following the rules as listed here: https://treasurebay.com/wp-content/uploads/2019/01/3Card-Blackjack-HTP.pdf
# Split hands are not implemented in this program
# Doesn't currently account for cards leaving the deck once they are dealt
# Follows the rule that if both dealer and player get Blackjack, it is a push hand

import random
from art import logo

def dealCard(numOfCards):
    hand = random.choices(cardList,k = numOfCards)
    return hand

def calculateCardTotal(listOfCards):
    total = sum(listOfCards)
    if 11 in listOfCards and total > 21:
        total -= 10
        
    return total

print(logo)
# the list is one suit multiplied by 4 for a full deck of 4 suits and multiplied by 6 for 6 decks of cards
# 11 represents aces
cardList = ([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4) * 6
continueGame = True
while continueGame is True:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play == 'y':
        playerHand = dealCard(2)
        playerTotal = calculateCardTotal(playerHand)
        computerHand = dealCard(2)
        computerTotal = calculateCardTotal(computerHand)
        print(f"Your cards: {playerHand}, your total is {playerTotal}")
        print(f"Computer's first card: {computerHand[0]}")
        anotherCard = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if anotherCard == 'y':
            print("Hit")
            newCard = dealCard(1)[0]
            playerHand.append(newCard)
            playerTotal = calculateCardTotal(playerHand)
        else:
            print("Stand")

        if (computerTotal <= 15):
            newCard = dealCard(1)[0]
            computerHand.append(newCard)
            computerTotal = calculateCardTotal(computerHand)

        print(f"Your final hand: {playerHand}, final score: {playerTotal}")
        print(f"Computer's final hand: {computerHand}, final score: {computerTotal}")

        # scoring
        if computerTotal > 21:
            print("Dealer busts. You win")
        elif playerTotal > 21:
            print("You bust. Dealer wins")
        elif playerTotal == computerTotal:
            print("Push hand. You tie")
        elif playerTotal <= 21 and computerTotal <= 21:
            if playerTotal > computerTotal:
                print("You win")
            else:
                print("Dealer wins")
        
    else: 
        continueGame = False