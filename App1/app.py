import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w,data.keys())[0]) #or w,data.keys(),n=1)
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]] 
        elif yn == "N":
            return "We don't have it."
        else: 
            return "Cannot process this query." 
    else:
        return "The word doesn't exist. Please recheck it. :("

word = input("Enter a word: ")

output = translate(word)
if  type(output) == list:
    for item in output:
        print(item)
    else: 
        print(output)
    # jason.load
    # i = input("Enter a word: ")
    # i
    # for word in i:
    #     result = ['word']
    #     print(result)
