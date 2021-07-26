import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        suggestion = get_close_matches(w, data.keys())[0]
        answer = input('Did you mean %s instead? Y or N. ' % suggestion)
        if answer.lower() == 'y':
            return data[suggestion]
        else:
            return 'Sorry, cannot find word. Please check spelling.'  
    else:
        return 'Word does not exist'

userWord = input('Enter word: ')

output = translate(userWord);

if type(output) == list:
    for item in output: 
        print(item)
else:
    print(output)
