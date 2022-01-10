import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def passwordGenerator(lettersInPass, symbolsInPass, numbersInPass):
    password = "".join(random.choices(letters, k=lettersInPass))
    password += password.join(random.choices(symbols, k=symbolsInPass))
    password +=password.join(random.choices(numbers, k=numbersInPass))

    passwordList = list(password)
    random.shuffle(passwordList)
    password = "".join(passwordList)

    return password

print("Welcome to the PyPassword Generator")

lettersInPassword = int(input("How many letters would you like in your password?\n"))
symbolsInPassword = int(input("How many symbols would you like in your password?\n"))
numbersInPassword = int(input("How many numbers would you like in your password?\n"))

generatedPassword = passwordGenerator(lettersInPassword, symbolsInPassword, numbersInPassword)

print("Here is your password: {}".format(generatedPassword))
