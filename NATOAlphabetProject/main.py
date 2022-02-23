from pandas import read_csv

def main():
    df = read_csv("nato_phonetic_alphabet.csv")
    alphabet_dict = {row.letter:row.code for (index,row) in df.iterrows()}

    word = ""
    while word != "EXIT":
        word = input("Enter a word to get the phonetic alphabet version of: ").upper()
        phonetic_word = [alphabet_dict.get(letter) for letter in word]

        try: 
            print(f"{' '.join(phonetic_word)}\n")
        except TypeError:
            print("Please only enter letters\n")

if __name__ == "__main__":
    main()
