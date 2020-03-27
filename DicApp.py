# CameronSD
# App: Dictionary
# Course: "Python Mega Course" by Ardit Sulce
import json
from difflib import get_close_matches

# Loads data from .json file 
data = json.load(open("data.json"))

# Gets user input and compares it to .json file
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: 
        return data[w.title()]
    elif w.upper() in data: 
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn.upper() == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.upper() == "N":
            return "That word doesn't exist. Please try again."
        else:
            return "We didn't understand your entry."
    else:
        return "That word doesn't exist, please check it"

word = input("Enter word: ")

output = translate(word)

# Organizes the output into seperate lines for better readability
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)