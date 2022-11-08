# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # print(key)
    # print(value)

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # print(f"{index} {row}")
    # print(row.student)
    # print(row.score)
    
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
csv_data = pandas.read_csv("NATO-alphabet\here_nato_phonetic_alphabet.csv")
data = {row.letter : row.code for (index, row) in csv_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#Catch exceptions for numbers typed
is_ok = True
# while is_ok:
#     try:
#         name = input("Enter a name: ")
#         result = [data[letter.upper()] for letter in name]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")

#     else:
#         print(result)
#         #if the result is printed then the while loop will end
#         is_ok = False

#use the rescussion
def generate_phonetic():
    name = input("Enter a word: ").upper()
    try:
        result = [data[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        #Here recussion is used to make the function call itself after the except is hit
        generate_phonetic()
    else:
        print(result)

generate_phonetic()
