#
# Simulated Coin-Operated Coffee Machine program
#

from menu import MENU

def checkResources(drink):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    insufficientResources = []
    if water <= MENU[drink]["ingredients"]["water"]:
        insufficientResources.append("water")
    if "milk" in MENU[drink]["ingredients"] and milk <= MENU[drink]["ingredients"]["milk"]:
        insufficientResources.append("milk")
    if coffee <= MENU[drink]["ingredients"]["coffee"]:
        insufficientResources.append("coffee")

    return insufficientResources

def removeResources(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if "milk" in MENU[drink]["ingredients"]: resources["milk"] -= MENU[drink]["ingredients"]["milk"]

def calculateTotal(q, d, n, p):
    return (q*.25) + (d*.1) + (n*.05) + (p*.01)

def refill():
    resources["water"] = 300
    resources["milk"] = 250
    resources["coffee"] = 100

resources = {
    "water": 300,
    "milk": 250,
    "coffee": 100,
    "money" : 0
}

print("Menu\nCappuccino\nLatte\nEspresso")

coffeeMakerOff = False
while not coffeeMakerOff:
    allowedOrders = ['cappuccino', 'latte', 'espresso', 'report', 'refill', 'off']
    order = input("What would you like to order? (cappuccino/latte/espresso): ")

    while order not in allowedOrders:
        order = input("That's not a valid choice. Choose either 'cappuccino', 'latte', or 'espresso': ").lower()
    
    if order in ['cappuccino', 'latte', 'espresso']:
        insufficientResources = checkResources(order)
        if len(insufficientResources) > 0:
            for i in insufficientResources:
                print(f"Sorry, there isn't enough {i} in the machine to make that")
            continue
        
        cost = MENU[order]['cost']
        print("That will cost ${:.2f}".format(cost))

        quarters = int(input("How many quarters to insert? "))
        dimes = int(input("How many dimes to insert? "))
        nickles = int(input("How many nickles to insert? "))
        pennies = int(input("How many pennies to insert? "))

        totalInserted = calculateTotal(quarters, dimes, nickles, pennies)
        print("You inserted ${:.2f}".format(totalInserted))
        if totalInserted < cost:
            print("That's not enough money. Your money has been refunded.")
            continue

        resources["money"] += cost
        change = totalInserted - cost

        removeResources(order)
        
        if change > 0: print("Your change is ${:.2f}".format(change))
        print(f"Here is your {order}. Enjoy!")

    elif order == "report":
        for i in resources:
            print(f"{''.join([i]).title()}: {resources.get(i)}")
    elif order == "refill":
        refill()
    else: 
        coffeeMakerOff = True
    


