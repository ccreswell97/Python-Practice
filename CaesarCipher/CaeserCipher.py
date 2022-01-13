import string
from art import logo

def caesar(text, shift, direction):
    if shift > 26:
        shift = shift%26
    newMessage = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in lowercaseAlphabet: 
            letterIndex = lowercaseAlphabet.index(letter)
            newMessage += lowercaseAlphabet[letterIndex + shift]
        elif letter in uppercaseAlphabet:
            letterIndex = uppercaseAlphabet.index(letter)
            newMessage += uppercaseAlphabet[letterIndex + shift]
        else:
            newMessage += letter

    print(f"The {direction}d message is {newMessage}")

print(logo + "\n\n\n")

shouldEnd = False
while not shouldEnd:
    allowedAnswers = ['encode', 'decode']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    while direction not in allowedAnswers:
        direction = input("Oops, that's not a valid response. Try again (encode/decode): ")
    text = input("Enter your message: ")
    shift = int(input("Enter the shift number: "))

    lowercaseAlphabet = list(string.ascii_lowercase)*2
    uppercaseAlphabet = list(string.ascii_uppercase)*2

    caesar(text, shift, direction)

    restart = input("Would you like to use the Caesar Cipher again? (yes/no) ").lower()
    if restart != "yes":
        print("Goodbye!")
        shouldEnd = True
