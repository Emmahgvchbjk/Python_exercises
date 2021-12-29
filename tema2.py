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
    elif 80 <= mark < 100:
        print("your grade is A")
    else:
        print("your mark is incorrect")

mark = int(input("what's your mark?"))
grade(mark)

print("\n EXERCITIUL 3")
# A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity
def price(pr):
    if pr >= 1000:
        print("you will be rewarded with a 10% discount, you need to pay ", pr - pr*0.1)
    else:
        print("thank you for your purchase, your total is ", pr)
pr = int(input("what is the price of the purchased quantity?"))
price(pr)

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

p = input("input your password: ")
pass_checker(p)

print("\n EXERCITIUL 6")
def number(nr):
    if nr == "5" or nr == "6":
        print("numarul este ", nr)
    else:
        print("numarul este diferit de 5 si 6")

nr = input("da numarul:")
number(nr)

print("\n EXERCITIUL 7")
def sort(n1, n2, n3):
    if (n1 < n2) and (n1 < n3) and (n2 < n3):
        print(n1, n2, n3)
    elif (n1 < n3) and (n1 < n2) and (n3 < n2):
        print(n1, n3, n2)
    elif (n2 < n1) and (n2 < n3) and (n1 < n3):
        print(n2, n1, n3)
    elif (n2 < n3) and (n2 < n1) and (n3 < n1):
        print(n2, n3, n1)
    elif (n3 < n1) and (n3 < n2) and (n1 < n2):
        print(n3, n1, n2)
    elif (n3 < n2) and (n3 < n1) and (n2 < n1):
        print(n3, n2, n1)

n1 = int(input("da numarul 1 :"))
n2 = int(input("da numarul 2 :"))
n3 = int(input("da numarul 3 :"))
sort(n1, n2, n3)

print("\n EXERCITIUL 8")
def talking(hour):
    if hour < 0 or hour > 24:
        print("intervalul orar este 0-24, incearca din nou sa introduci o ora corecta")
    elif hour < 7 or hour >20:
        print("shh, suntem in intervalul orar de odihna!!")
    else:
        print("papapagalul poate sa faca zgomot")

hour = int(input("ce ora este?"))
talking(hour)

print("\n EXERCITIUL 9")
def negatie(cuv):
    if cuv[0:3] == "not":
        print(cuv)
    else:
        print("not"+cuv)

cuv = input("care este cuvantul? ")
negatie(cuv)

print("\n EXERCITIUL 10")
def check(cuv2):
    print(cuv2[0:2] == "hi")

cuv2=input("da string-ul: ")
check(cuv2)

print("\n EXERCITIUL 11")
def sums(a, b):
    sum = a + b
    if(0 < sum < 19):
        print(20)
    else:
        print(sum)
a = int(input("value 1: "))
b = int(input("value 2: "))
sums(a, b)

print("\n EXERCITIUL 12")
def verificare(special):
    if special > 0:
        print(special % 11 == 0)
    else:
        print("numarul introdus nu este pozitiv")

special = int(input("da un numar pozitiv"))
verificare(special)