import json

data = json.load(open("data.json"))

def translator(w):
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist. Please recheck it. :("

word = input("Enter a word: ")

print(translator(word))
    # jason.load
    # i = input("Enter a word: ")
    # i
    # for word in i:
    #     result = ['word']
    #     print(result)
