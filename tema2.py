print('EXERCITIUL 1')
# 1.Take two int values from user and print greatest among them
def greatest_num(a,b):
    if a>b:
        print(a, "is the greatest value")
    elif b>a:
        print(b, "is the greatest value")
    else:
        print("the two numbers are equal")

a = int(input("da primul numar: "))
b = int(input("da al doilea numar: "))
greatest_num(a, b)

print("\n EXERCITIUL 2")
# A school has following rules for grading system:
# a. Below 25 - F, b. 25 to 45 - E, c. 45 to 50 - D, d. 50 to 60 - C, e. 60 to 80 - B, f. Above 80 - A
# Ask user to enter marks and print the corresponding grade
def grade(mark):
    if mark < 25:
        print("your grade is F")
    elif 25 <= mark < 45:
        print("your grade is E")
    elif 45 <= mark < 50:
        print("your grade is D")
    elif 50 <= mark < 60:
        print("your grade is C")
    elif 60 <= mark < 80:
        print("your grade is B")
    else:
        print("your grade is A")

mark = int(input("what's your mark?"))
grade(mark)

print("\n EXERCITIUL 3")
# A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity
def price(quantity):
    if quantity >= 1000:
        print("you will be rewarded with a 10% discount")
    else:
        print("thank you for your purchase")
quantity = int(input("what is the purchased quantity?"))
price(quantity)

print("\n EXERCITIUL 4")
# Write an if statement that asks for the user's name via input() function.
# If the name is "Bond" make it print "Welcome on board 007." Otherwise make it print "Good morning NAME". (Replace Name with user's name)
def hello(name):
     if name == "Bond":
         print("Welcome on board 007.")
     else:
         print("Good morning,", name)
name = input("what's your name?")
hello(name.capitalize())

print("\n EXERCITIUL 5")
# Write a Python program to check the validity of password input by users.
# At least 1 letter between [a-z], 1 letter between [A-Z], 1 number between [0-9], 1 character from [$#@].
# Minimum length 6 characters. Maximum length 16 characters.
def pass_checker(p):
    characters=['$','#','@']
    counter = True
    if not any(i.isupper() for i in p):
        print("the password must contain at least one uppercase")
        counter = False
    elif not any(i.islower() for i in p):
        print("the password must contain at least one lowercase")
        counter = False
    elif not any(i in characters for i in p):
        print("the password must contain at least one special character")
        counter = False
    elif not any(i.isdigit() for i in p):
        print("the password must contain at least one number")
        counter = False
    else:
        counter = True
    if counter == True and 6< len(p) <16:
        print("valid password")
    else:
        print("therefore the password is invalid")

p = input("input your password")
pass_checker(p)

