# Script that gets a list of names out of a file and addresses a letter to each of them

# Get the names
with open("./Input/Names/invited_names.txt", "r") as names:
    names = names.readlines()
names = [name.strip() for name in names]

# Get the starting letter
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    starting_letter = letter.read()

# Put the names into a new letter for each name
for name in names:
    with open (f"./Output/ReadyToSend/{name}.txt", "w") as new_letter:
        new_letter.write(starting_letter.replace("[name]", name))