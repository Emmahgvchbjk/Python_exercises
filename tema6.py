# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of the rectangle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("the area is", int(self.length) * int(self.width))

    def perimeter(self):
        print("the perimeter is", int(2*self.length + 2*self.width))

# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.

    def display(self):
        print("the length is", self.length)
        print("the width is", self.width)
        print("the area is", self.area())
        print("the perimeter is", self.perimeter())

# Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate
# the volume of the Parallelepiped
class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def volume(self):
        volume = int(self.length*self.width*self.height)
        print("the volume is", volume)

rectangle1 = Rectangle(2, 8)
rectangle1.area()
rectangle1.perimeter()
rectangle1.display()
parallelepipede1 = Parallelepipede(4, 8, 2)
parallelepipede1.volume()

# Define a Book class with the following attributes: Title, Author (Full name), Price.
# Set the View() method to display information for the current book.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def view(self):
        print (f'the book{self.title} was written by {self.author} and costs {self.price}')

book1 = Book("cdsc","cdss",44)
book1.view()

# Create a Python class Person with attributes: name and age of type string.
# Create a display() method that displays the name and age of an object created via the Person class.
# Create a child class Student  which inherits from the Person class and which also has a section attribute.
# Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# Create a student object via an instantiation on the Student class and then test the displayStudent method.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'the person {self.name} is {self.age} years old')

class Student(Person):
    def __init__(self, name, age, section):
        Person.__init__(self, name, age)
        self.section = section

    def displayStudent(self):
        print(f'the student {self.name} is {self.age} years old; his/her section is {self.section}')

student = Student("mary", "23", "vfdvd")
student.displayStudent()


# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method  which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details.

class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self, dep):
        self.balance = self.balance + dep

    def Withdrawal(self, withd):
        if(self.balance < withd):
            print("insufficient funds")
        else:
            self.balance = self.balance - withd

    def bankFees(self):
        self.balance = self.balance - self.balance*0.5

    def display(self):
        print(f'{self.name}, you have {self.balance} dollars in the account {self.accountNumber}')

# - Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
# - Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
# - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
# - Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
# - Create  a method called testPrims() allowing to test if two numbers are prime between them.
# - Create a tableMult() method which creates and displays the multiplication table of a given integer.
# - Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
# - Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv.
# - Create another listDivPrim() method that gets all the prime divisors of a given integer.
class Computation:
    def __init__(self):
        pass

    def factorial(self, n):
        fact = 1
        for i in range(1,n+1):
            fact = i * fact
        return fact

    def sum(self, n):
        s = 1
        for i in range(1, n + 1):
            s = i + s
        return s

    def testPrim(self, n):
        div = 0
        i = 1
        for i in range(1, n + 1):
            if n%i == 0:
                div += 1
        if div == 2:
            return True
        else:
            return False

    def testPrims(self, n, m):
        cd = 1
        for i in range (1, n):
            if(n%i==0 and m%i==0):
                cd += 1
        if cd ==1:
            return True
        else:
            return False

    def tableMult(self, n):
        for i in range(1, 11):
            print(f'{i} x {n} = i*n')

    def allTablesMult(self):
        for i in range(1, 10):
            for j in range (1, 10):
                print(f'{i} x {j} = i*j')

    def listDiv(self, n):
        Ldiv=[]
        for i in range(1, n):
            if (n%i ==0):
               Ldiv.append(i)
        return Ldiv

    def listDivPrim(self, n):
        Ldprim = []
        for i in range(1, n):
            if (n%i ==0 and self.testPrim(i)):
                Ldprim.append(i)
        return Ldprim