correct_password = "python123"
name = input("Enter Name: ")
lastname = input("Great now enter your last name:")
password = input("Enter your password: ")

while correct_password != password:
    password = input("Nope. That's wrong. Enter your password: ")


message = "Okay thanks, %s %s, You're now logged in." % (name,lastname)
print(message)
 
