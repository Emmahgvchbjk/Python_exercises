print('EXERCITIUL 1')
# 1. Display the sum of 5 + 10, using two variables: x and y.
x = 5
y = 10
print("suma este", x + y)

print('EXERCITIUL 2')
# 2. Create 3 variables:
# ●    One of type int  = 20.
a = 20
print(a)
# ●    One of type float = 10.
b = 10.0
print(b)
# ●    One of type string = “pytho
c = "pytho"
print(c)

print('EXERCITIUL 3')
# 3. Using function type check the type of :
# ●restanta = 0
restanta = 0
print(type(restanta))
# ●    notaFinala = 10.0
notaFinala = 10.0
print(type(notaFinala))
# ●    laborator = “Introducere in informatica”
laborator = "Introducere in informatica"
print(type(laborator))

print('EXERCITIUL 4')
# 4.  Reads two numbers and multiplies them together and print out their product
nr1 = input('citeste un numar: ')
nr2 = input('citeste alt numar: ')
print("produsul numerelor citite este", int(nr1) * int(nr2))

print('EXERCITIUL 5')
# 5. Check if the first and last number of a string  is the same
sir=input('da sirul: ')
p = sir[0]
u = sir[-1]
print(p == u)

print('EXERCITIUL 6')
# 6. Write a program to find how many times substring “Emma” appears in the given string.
# str_x = "Emma is good developer. Emma is a writer"
str_x = "Emma is good developer. Emma is a writer"
print(str_x.count('Emma'))

print('EXERCITIUL 7')
# 7. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# Ex "eu merg la mare" sa imi afiseze "eure"
str_a = input("da sirul: ")
print(str_a[0:2] + str_a[-2:])

print('EXERCITIUL 8')
# 8. Write a Python program to calculate the length of a string.
# pt "eu merg la mare" ->15
sir_b = input("da sirul: ")
print(len(sir_b))

print('EXERCITIUL 9')
# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
sir_c = input("da sirul:")
sir_cc = str.replace(sir_c, sir_c[0], '$')
print(sir_c[0]+sir_cc[1:])

print('EXERCITIUL 10')
# Utilizand tipurile de print pe care vi le-am aratat:
# afisati in consola I have 1000 dollars so I can buy 3 football for 450.00 dollars.
totalMoney = 1000
quantity = 3
price = 450
print(f'I have {totalMoney} dollars so I can buy {quantity} football for {("{:.2f}".format(price))} dolars.')

print('EXERCITIUL 11')
# Build a program to calculate the followings using the input from the user for a, b or r
a = input('introdu dimensiune latura 1: ')
b = input('introdu dimensiune latura 2: ')
r = input('introdu raza: ')
#area and perimeter
print('area is ', int(a)*int(b))
print('perimeter is ', 2*int(a)+2*int(b))
#circle area
print('the area of the circle is ',3.14*int(r)*int(r))

print('EXERCITIUL 13')
username = input('type the username')
password = input('type the password')
zz='*'*len(password)
print(f'The password for the user {username} is \n {zz} is {len(password)}')

print('EXERCITIUL 14')
nume1, nume2, nume3 = input('scrieti numele').split()

print('EXERCITIUL 15')
num = 458.541315
print("{:.2f}".format(num))
