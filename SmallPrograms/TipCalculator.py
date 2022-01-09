print("Welcome to the tip calculator.")

def splitBill(totalBill, numberOfPeople, tipPercent):
    tipPercentDecimal = tipPercent/100
    billAndTipTotal = totalBill + (totalBill*tipPercentDecimal)
    
    return billAndTipTotal/numberOfPeople

totalBill = input("What is the total bill amount? ").strip("$")
numberOfPeople = input("How many people are you splitting the bill between? ")
tipPercent = input("What percentage of tip would you like to give? ").strip("%")

splitAmount = splitBill(float(totalBill), int(numberOfPeople), float(tipPercent))

print("Each person should pay ${:.2f}".format(splitAmount))