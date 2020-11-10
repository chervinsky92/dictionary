import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word): 
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: 
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        close_match = get_close_matches(word, data.keys(), cutoff=0.8)[0]
        correction = input(f'Did you mean {close_match}? ').lower()
        if correction in ['y', 'yes']:
            return data[close_match]
        elif correction in ['n', 'no']:
            return "That word doesn't exist."
        else:
            return "We did not understand your entry."
    else:
        return "That word doesn't exist."

while True:
    word = input('Enter word: ')
    if not word: 
        break
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)