# return the number of 9's in a list
# list = []
# list = [int(a) for a in input("Enter the list items : ").split()]
#
# def nine_in_list(list):
#     count = 0
#     for element in list:
#         if(element == 9):
#             count += 1
#     return count
#
# print(nine_in_list(list))

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6
# for i in range(0,7):
#     if i == 3 or i == 6:
#         continue
#     else:
#         print(i)

# Print sum of the numbers between 20 and 100
# def sum():
#     sum = 0
#     for i in range(20,100):
#         sum = sum + i
#     return sum
#
# print(sum())

# Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# def integers():
#     for i in range(1,51):
#         if i % 3 == 0:
#             print("fizz")
#         elif i % 5 == 0:
#             print("buzz")
#         else:
#             print(i)
#
# integers()

# Write a Python program to create the multiplication table (from 1 to 10) of a number.
# def multiplication_table():
#     b = int(input("enter the number: "))
#     for i in range(1,11):
#         prod = i * b
#         print(f'{i}x{b} = {prod}')
# multiplication_table()

# Write a Python program to construct the pattern..
# def pattern():
#     for i in range(1,10):
#         print(i*str(i))
# pattern()

# Write a program to print n natural numbers in descending order
# numbers = []
# numbers = [int(a) for a in input("input the numbers that you want to sort : ").split()]
# numbers.sort(reverse=True)
# print(numbers)

# print max and minim from the list
# lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
# print(max(lst))
# print(min(lst))
# count how many times 6 occur in the list.
# count = 0
# for i in lst:
#     if i == 6:
#         count+=1
# print(count)

# Using .remove() method, clear the last element of the list.
# lst.remove(lst[-1])
# print(lst)

# Concatenate two lists:
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# list3 = list1 + list2
# print(list3)

# add the sub-list: ["socks", "tshirt", "pajamas"] to the end of the gift_list
# gift_list=['socks', '4K drone', 'wine', 'jam']
# gift_list = gift_list + ["socks", "tshirt", "pajamas"]
# print(gift_list)

# Given 2D array calculate the sum of diagonal elements.
# a = [[1,3,5],[1,4,6],[7,6,9]]
# s = 0
# for i in range(0,len(a)):
#     for j in range(0,len(a)):
#         if (i == j):
#             s = s + a[i][j]
# print(s)

# Add item 7000 after 6000 in the following Python List
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)

# Given a Python list, find value 20 in the list, and if it is present, replace it with 200.
#  Only update the first occurrence of a value
# list1 = [5, 10, 15, 20, 25, 50, 20]
# for i in range(len(list1)):
#      if(list1[i] == 20):
#          list1[i] = 200
#          break
# print(list1)

# Remove empty strings from the list of strings
# list4 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list5=[]
# for i in list4:
#     if i != "":
#         list5.append(i)
# print(list5)

# Write a program that appends the square of each number to a new list.
# list6 = [int(i) for i in input("Enter the list items : ").split()]
# list7 = []
# for i in list6:
#     list7.append(i*i)
# print(list7)

# Write a function that takes a list as a parameter and returns the reversed list.
# Do NOT use the built-in reverse() function.
# def reversed():
#     li = [int(i) for i in input("enter the list items:").split()]
#     li1= li[::-1]
#     print(li1)
# reversed()

# Write a python program to print the first 10 numbers Fibonacci series
# sum = 0
# num1 = 0
# num2 = 1
# for i in range(1, 10):
#     print(num1, end=" ")
#     sum = num1 + num2
#     num1 = num2
#     num2 = sum

# Write a python program to read a number and print a right triangle using "*"
# z = int(input("type the number: "))
# for i in range(0,z+1):
#     print("*"*i)

# Write a python program to check given number is prime or not
# v = int(input("type the number: "))
# count1 = 0
# for i in range(1,v):
#     if v % i ==0:
#         count1 += 1
# if count1!=2:
#     print("the number is prime")
# else:
#     print("it's not")

# Write a python program to print all prime numbers between 0 to 100 , and print how many prime numbers are there.
# count3 = 0
# list3 = []
# for i in range(0,101):
#     count2 = 0
#     for j in range(2,(i//2 +1)):
#         if i % j ==0:
#             count2 += 1
#
#     if count2==0:
#         list3.append(i)
# print("the prime numbers are", list3, len(list3))
