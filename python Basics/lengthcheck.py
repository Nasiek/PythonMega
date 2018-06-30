if len("Hi") == 2:
    print(True)
else:
    print(False)

def string_length(mystring):
    if type(mystring) == int:
         return "Sorry, integers don't have length"
     else:
         return len(mystring)
