import json
from difflib import get_close_matches


def get_dict():
    with open("data.json") as data_file:
        dictionary = json.load(data_file)
        return dictionary


def get_definition(w, dictionary):
    if w.lower() in dictionary:
        return dictionary[w]
    elif w.title() in dictionary:
        return dictionary[w.title()]
    elif w.upper() in dictionary:
        return dictionary[w.upper()]
    else:
        result = get_close_matches(w, dictionary.keys())
        if len(result) > 0:
            yn = input("Did you mean %s instead? [Y/n] " % result[0])
            if yn.lower() == "y":
                return dictionary[result[0]]
            elif yn.lower() == "n":
                return "Word doesn't exist, please double check it"
            else:
                return "Your query wasn't understood, please try again."
        else:
            return "Word doesn't exist, please double check it"


word = str(input("Enter word: "))

definition = get_definition(word, get_dict())
if isinstance(definition, list):
    for item in definition:
        print(item)
else:
    print(definition)
