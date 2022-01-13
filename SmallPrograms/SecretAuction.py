import os

def cls():
    os.system("cls" if os.name == "nt" else "clear")

print("Welcome to the secret auction program.")

bidDictionary = {}
auctionOver = False
while not auctionOver:
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bidDictionary.update({name:bid})
    moreBidders = input("Are there other bidders? (yes/no) ")
    cls()
    if moreBidders == "no":
        highestBid = max(bidDictionary.values())
        highestBidder = max(bidDictionary, key=bidDictionary.get)
        print("The winner is {} with a bid of ${:.2f}".format(highestBidder, highestBid))
        auctionOver = True