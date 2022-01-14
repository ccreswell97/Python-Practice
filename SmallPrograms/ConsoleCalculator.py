def add(num1, num2): 
    return num1 + num2

def subtract(num1, num2): 
    return num1 - num2

def multiply(num1, num2): 
    return num1 * num2

def divide(num1, num2): 
    return num1 / num2

def modulo(num1, num2):
    return num1 % num2

def exponent(num1, num2):
    return num1 ** num2

operationDict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "%" : modulo,
    "**": exponent
}

print("Welcome to the Calculator")
def calculator():
    firstNumber = float(input("Enter the first number:  "))
    
    shouldContinue = True
    while shouldContinue:
        for i in operationDict: print(i, end=" ")
        operation = input("\nEnter the operator (choose from above symbols): ")
        while operation not in operationDict:
            operation = input("Oops, that's not valid. Enter the operator (choose from above symbols): ")
        
        secondNumber = float(input("Enter the second number: "))

        answer = operationDict[operation](firstNumber, secondNumber)

        print(f"{firstNumber} {operation} {secondNumber} = {answer}")
        continueCalculating = input(f"Type 'y' to continue calculating with {answer}, type 'c' to clear and start a new calculation, or type 'n' to exit: ").lower()
        if continueCalculating == 'n':
            print("Goodbye")
            shouldContinue = False
        elif continueCalculating == 'y':
            firstNumber = answer
        elif continueCalculating == 'c':
            calculator()

calculator()
