"""
================================================================================
                         COMPLETE PYTHON LANGUAGE COURSE
                     BASIC → INTERMEDIATE → ADVANCED
                 (Learn by reading COMMENTS + CODE)

 HOW TO RUN:
 - Install Python 3.x
 - Run: python python_full_course.py
================================================================================
"""

# =============================================================================
# 1️⃣ BASIC OUTPUT
# =============================================================================
print("========= PYTHON FULL COURSE START =========\n")

# =============================================================================
# 2️⃣ VARIABLES & DATA TYPES
# =============================================================================

# Python is dynamically typed (no type declaration needed)
name = "Bhanu"          # string
age = 20                # integer
marks = 88.75           # float
grade = 'A'             # character (string of length 1)
is_student = True       # boolean

print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Grade:", grade)
print("Is Student:", is_student)

# =============================================================================
# 3️⃣ TYPE CHECKING
# =============================================================================
print("\nTypes:")
print(type(name), type(age), type(marks), type(is_student))

# =============================================================================
# 4️⃣ OPERATORS
# =============================================================================
a, b = 10, 3

print("\nOperators:")
print(a + b)     # addition
print(a - b)     # subtraction
print(a * b)     # multiplication
print(a / b)     # division
print(a % b)     # modulus
print(a > b)     # relational
print(a == b)    # equality

# =============================================================================
# 5️⃣ CONDITIONAL STATEMENTS
# =============================================================================
print("\nConditionals:")
if marks >= 90:
    print("Excellent")
elif marks >= 60:
    print("Good")
else:
    print("Fail")

# =============================================================================
# 6️⃣ LOOPS
# =============================================================================
print("\nFor Loop:")
for i in range(1, 6):
    print(i, end=" ")

print("\n\nWhile Loop:")
i = 1
while i <= 3:
    print(i)
    i += 1

# =============================================================================
# 7️⃣ DATA STRUCTURES
# =============================================================================

# List (ordered, mutable)
numbers = [10, 20, 30, 40]
print("\nList:", numbers)

# Tuple (ordered, immutable)
point = (10, 20)
print("Tuple:", point)

# Set (unordered, unique)
unique_nums = {1, 2, 3, 3}
print("Set:", unique_nums)

# Dictionary (key-value)
student = {
    "name": "Bhanu",
    "age": 20,
    "marks": 88.75
}
print("Dictionary:", student)

# =============================================================================
# 8️⃣ FUNCTIONS
# =============================================================================
def add(x, y):
    return x + y

# Function with default argument
def greet(name="User"):
    print("Hello", name)

print("\nFunctions:")
print("Add:", add(5, 10))
greet("Bhanu")

# =============================================================================
# 9️⃣ FUNCTION ARGUMENT TYPES
# =============================================================================
def student_info(name, age, *skills, **details):
    print("\nName:", name)
    print("Age:", age)
    print("Skills:", skills)
    print("Details:", details)

student_info("Bhanu", 20, "Python", "AI", city="Hyderabad")

# =============================================================================
# 🔟 LAMBDA FUNCTIONS
# =============================================================================
multiply = lambda x, y: x * y
print("\nLambda Result:", multiply(3, 4))

# =============================================================================
# 1️⃣1️⃣ LIST COMPREHENSION
# =============================================================================
squares = [x * x for x in range(1, 6)]
print("\nList Comprehension:", squares)

# =============================================================================
# 1️⃣2️⃣ OOP – CLASS & OBJECT
# =============================================================================
class Student:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age

    def display(self):
        print(f"Student: {self.name}, {self.age}")

s1 = Student("Bhanu", 20)
s1.display()

# =============================================================================
# 1️⃣3️⃣ INHERITANCE & POLYMORPHISM
# =============================================================================
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Person:", self.name)

class CollegeStudent(Person):
    def __init__(self, name, college):
        super().__init__(name)
        self.college = college

    def display(self):
        print(f"{self.name} studies at {self.college}")

p = CollegeStudent("Bhanu", "GIOE")
p.display()

# =============================================================================
# 1️⃣4️⃣ ENCAPSULATION
# =============================================================================
class BankAccount:
    def __init__(self):
        self.__balance = 0     # private variable

    def set_balance(self, amount):
        self.__balance = amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.set_balance(5000)
print("\nBalance:", acc.get_balance())

# =============================================================================
# 1️⃣5️⃣ EXCEPTION HANDLING
# =============================================================================
print("\nException Handling:")
try:
    x = 10 / 0
except Exception as e:
    print("Error:", e)
finally:
    print("Finally executed")

# =============================================================================
# 1️⃣6️⃣ FILE HANDLING
# =============================================================================
with open("demo.txt", "w") as f:
    f.write("Hello from Python file handling")

with open("demo.txt", "r") as f:
    print("\nFile Content:")
    print(f.read())

# =============================================================================
# 1️⃣7️⃣ MODULES (STANDARD LIBRARY)
# =============================================================================
import math

print("\nMath Module:")
print("Square root:", math.sqrt(25))
print("PI:", math.pi)

# =============================================================================
# 1️⃣8️⃣ JSON HANDLING
# =============================================================================
import json

data = {"name": "Bhanu", "age": 20}
json_data = json.dumps(data)

print("\nJSON Encode:")
print(json_data)

print("JSON Decode:")
obj = json.loads(json_data)
print(obj["name"])

# =============================================================================
# 1️⃣9️⃣ ITERATORS & GENERATORS
# =============================================================================
def count_up(n):
    for i in range(1, n + 1):
        yield i

print("\nGenerator:")
for num in count_up(5):
    print(num)

# =============================================================================
# 2️⃣0️⃣ DECORATORS (ADVANCED)
# =============================================================================
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello from function")

say_hello()

# =============================================================================
# 2️⃣1️⃣ MULTITHREADING (BASIC)
# =============================================================================
import threading
import time

def task():
    time.sleep(1)
    print("Thread executed")

t = threading.Thread(target=task)
t.start()
t.join()

# =============================================================================
# 2️⃣2️⃣ ASYNC PROGRAMMING
# =============================================================================
import asyncio

async def async_task():
    await asyncio.sleep(1)
    print("Async task completed")

asyncio.run(async_task())

# =============================================================================
# END
# =============================================================================
print("\n========= PYTHON FULL COURSE END =========")
