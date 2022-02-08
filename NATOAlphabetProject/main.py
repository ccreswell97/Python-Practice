from pandas import DataFrame, read_csv

df = read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for (index,row) in df.iterrows()}

print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

