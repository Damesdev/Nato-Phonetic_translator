import pandas


#TODO 1. Create a dictionary in this format:
phonetic_csv = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(phonetic_csv)




#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

phonetic_list = []
run_translator = True

while run_translator:
    # clear()
    letter_word = str(input("\nwhat word would you like to translate? ").upper())
    letter_list = list(letter_word)

    if letter_word == "EXIT":
        run_translator = False
    else:
        for character in letter_list:
            for (index, row) in phonetic_csv.iterrows():
                if row.letter == character:
                    phonetic_list.append(row.code)
        print(phonetic_list)