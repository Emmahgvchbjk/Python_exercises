# return the number of 9's in a list
# count = 0
# j= 0
# i = 0
# list = []
# n = int(input("number of elements: "))
# while i< n:
#     el = int(input())
#     list.append(el)
#     i += 1
#
# while j < n:
#     if(list[j] == 9):
#         count += 1
#     j += 1
#
# print("the number of 9s in this list is: ", count)

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6
# i = 0
# while i <= 6:
#     if i == 3 or i == 6:
#         pass
#     else:
#         print(i)
#     i += 1

# Print sum of the numbers between 20 and 100
# i = 20
# sum = 0
# while ( i<= 100 ):
#     sum = sum + i
#     i += 1
# print(sum)

# Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# i = 0
# while (i <= 50):
#     if i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)
#     i += 1

# Write a Python program to create the multiplication table (from 1 to 10) of a number.
# b = int(input("enter the number: "))
# i = 0
# while i <= 10:
#     print (f'{i} x {b} = {i*b}')
#     i += 1

# Write a Python program to construct the pattern..
# i = 1
# while i < 10:
#     print(i*str(i))
#     i += 1

# Write a program to print n natural numbers in descending order
# n = int(input())
# while n > 0:
#     print(n)
#     n = n - 1

# print max and minim from the list
# lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
# print(max(lst))
# print(min(lst))
# count how many times 6 occurs in the list.
# count = 0
# j= 0
#
# while j < len(lst):
#     if(lst[j] == 6):
#         count += 1
#     j += 1
#
# print("the number of 6s in this list is: ", count)

# Given 2D array calculate the sum of diagonal elements.
# a = [[1,3,5],[1,4,6],[7,6,9]]
# s = 0
# i = 0
# j =0
# while i < len(a):
#     while j < len(a):
#         if i == j:
#             s = s + a[i][j]
#         j += 1
#         i += 1
#
# print(s)

# Given a Python list, find value 20 in the list, and if it is present, replace it with 200.
#  Only update the first occurrence of a value
# list1 = [5, 10, 15, 20, 25, 50, 20]
# i = 0
# while i< len(list1):
#     if(list1[i] == 20):
#         list1[i] = 200
#         break
#     i += 1
# print(list1)

# Remove empty strings from the list of strings
# list4 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list5 =[]
# i = 0
# while i < len(list4):
#     if list4[i] !="":
#         list5.append(list4[i])
#     i += 1
#
# print(list5)

# Write a program that appends the square of each number to a new list.
# list6 = []
# list7 = []
# p = int(input("number of elements: "))
# i = 0
# j = 0
# while i < p:
#     ele = int(input("element: "))
#     list6.append(ele)
#     i += 1
#     list7.append(ele*ele)
#
# print(list7)

# Write a python program to print the first 10 numbers Fibonacci series
# sum = 0
# num1 = 0
# num2 = 1
# i = 0
# while (i < 10):
#     print(num1)
#     sum = num1+num2
#     num1 = num2
#     num2 = sum
#     i += 1

# Write a python program to read a number and print a right triangle using "*"
# nr = int(input("number: "))
# i = 1
# while i <= nr:
#     print("*" * i)
#     i += 1

# Write a python program to check given number is prime or not
# value = int(input("value: "))
# counter = 1
# i = 1
# while i < value:
#     if(value%i==0):
#         counter += 1
#     i += 1
# if counter == 2:
#     print("este prim")
# else:
#     print("nu este prim")

# Write a python program to print all prime numbers between 0 to 100 , and print how many prime numbers are there.
# m = 0
# count1 = 0
# while(m <= 100):
#     count = 0
#     i = 2
#     while(i <= m//2):
#         if(m % i == 0):
#             count += 1
#             break
#         i = i + 1
#
#     if(count ==0 and m!=1):
#         print(m, end=" ")
#         count1 += 1
#     m += 1
# print(f'\n there are {count1} prime numbers')