import sys

print("Python Version:", sys.version)

"""
TBD: How do you use the REPL
========================== Arithmetic ===================
"""

x = 5 % 2
print("remainder = ", x)

x = 51 / 15
print("expect float, quotient = ", x)

s = 51//15
print("True integer division", s)

# Strings =====================

user_input = input()
print(f"You typed {user_input}")

words = ["halloween", "Diwali", "Christmas", "New Year"]
festivals = f"first {words[0]}, then {words[1]} then {words[2]} and finally {words[3]}"

print(festivals)

tokens = festivals.split()
print(tokens)

# so the default split is by space, but whole words can be used as delimiters too.
tokens = festivals.split("then")
print(tokens)

# print characters in a string, so a for loop works
sentence = 'judas the hammer'
for c in sentence:
    print(c)

# find the numbers in a string
"""
The Regex says 

r - raw string, i.e. the slashes are not for python but for the regex
slash d = 0-9 characters
+ - 1 or many
"""
senty = "there are 50 gold coins and in 7 bags"
import re
numbers = re.findall(r'\d+', senty)
print("numbers from string = ", numbers)

"""
=========================================
Logical conditions and branching
=========================================
"""

if len(user_input) > 100:
    print("That was a long sentence")
elif len(user_input) <= 100 and len(user_input) > 15:
    print("sentence of average length")
else:
    print("short sentence")

### switch case

number = 3

"""
works only with version greater than 3.10

word_rep = match number:
    case 1:
        "one"
    case 2:
        "two"
    case 3:
        "three"
    case _:
        "Out of range number"
"""

### Lists

sample_list = [22, 51, 33, 82, 99, 64, 83]

for i in sample_list:
    print(i)

for idx, i in enumerate(sample_list):
    print(f"index = {idx}, item = {sample_list[idx]}")
    print(i)

# create lists using list comprehension

fruit_list = ["apple", "banana", "orange", "pear", "kiwi", "strawberry"]
e_fruit_list = [x for x in fruit_list if 'e' in x]
print(e_fruit_list)

# Using the list keyword
"""
class_b_list = list(1, 2, 3, 5, 10, 4)
print(class_b_list)

The above doesn't work.. looks like it is to convert other iterables to list
"""

my_tuple = (1, 2, 3, 4, 5)
from_tuple_list = list(my_tuple)
print(f" List created from tuple = {from_tuple_list}")

# Create a java style array of a certain length, initialized to Nones

fixed_array = [None] * 5
fixed_array[3] = "Black Cab"
print("fixed Array = ", fixed_array)

# Updating and returning a new list
base_list = ["anger", "frustration", "envy", "confusion"]
print("Will get a None: ", base_list.append("healing"))
print("Will see the combination: ", base_list + ["healing"])


# Custom Sorting of a list, Key and Sorted
def custom_comp(input_str: str):
    return len(input_str)


# not in place update.. interesting that it removes duplicates.
sorted_list = sorted(base_list, key=custom_comp)
print("List sorted by length = ", sorted_list)


"""
=================================================
Set

Looks like there is some difference between {} and set(),
but it is not mutability
=================================================
"""

first_set = {}
print(first_set)

first_set = {1, 2, 3}
first_set.add(1)
print(first_set)
print(first_set.add(4))
first_set.remove(3)
print(first_set)
print(2 in first_set)

second_set = set()
print(second_set)
second_set.add("hammer")
print(second_set)
second_set.remove("hammer")
print(second_set)

third_set = frozenset({1, 5, 99})
print(third_set)

# Nested Sets
set_outer = set()
set_inner = set()
set_inner.add(2)
# set_outer.add(set_inner) This will not work
set_outer.add(frozenset(set_inner))
# so you can add only a frozen set inside a set
print("nested set = ", set_outer)

# Append an item to a set and return a new set
print("This is an in place updated, doesn't return anything: ", set_inner.add(33))

print("This should return a new set with: ", set_inner | {33})


"""
===============================
Dict
=================================
"""

first_dict = {}

## directly add a key value pair
first_dict.update({1: "a"})
print(first_dict)
print(first_dict[1])

first_dict = {1: "one", 2: "two", 3: "three"}

for key in first_dict.keys():
    print(f"{key} = {first_dict[key]}")

for key, value in first_dict.items():
    print(f"{key} = {value}")

transactions = [
    {'date': '2023-11-01', 'product': 'A', 'amount': 100, 'customer': 'Alice'},
    {'date': '2023-11-02', 'product': 'B', 'amount': 150, 'customer': 'Bob'},
    {'date': '2023-11-03', 'product': 'A', 'amount': 200, 'customer': 'Charlie'},
    {'date': '2023-11-04', 'product': 'C', 'amount': 50, 'customer': 'David'},
    {'date': '2023-11-05', 'product': 'B', 'amount': 75, 'customer': 'Eve'},
]

tran_map = {}
for tran in transactions:
    product = tran['product']
    if product not in tran_map:
        tran_map[product] = []
    tran_map[product].append(tran)

print(tran_map)
"""#====================================
Using default dict
#===================================="""

from collections import defaultdict

default_tran_map = defaultdict(list)
for tran in transactions:
    product = tran["product"]
    default_tran_map[product].append(tran)

print(default_tran_map)

"""#====================================
Tuples - 

1. Immutable collections - ordered as well
2. Multiple return values from methods
3. As shown above, they are iterables which can be converted to a list.
#===================================="""

sample_tuple = (7, 4, 5, 6, 8, 10)
print(sample_tuple)

for i in sample_tuple:
    print(i)

"""
====================
Functions in Python
===================
"""


def first_function():
    print("Hello from inside a function")


first_function()


def second_function(param1: str):
    print(f"This was sent to the function = {param1}")


second_function("Hello hi")


# Python also has var-args
def third_function(*params):
    for param in params:
        print(f"Input = {param}")


# so, the array is treated as a single parameter
third_function([1, 2, 3, 4, 5])
# the below arguments are treated as multiple individuals
third_function(1, 2, 3, 4, 5)


# keyword args
def fourth_function(param1=None, param2=0):
    print(f"param1 = {param1}")
    print(f"param2 = {param2}")


fourth_function("hi", 1)  # surprisingly works
fourth_function(param2=1, param1="Hi")  # This works too, but you are able to maintain the order


# fourth_function(2000, param1="Hi") This doesn't work - says multiple values for param1
# fourth_function(param1="Hi", 2000) SyntaxError: positional argument follows keyword argument

# the star and double star for args and kwargs
def fifth_function(*params, **key_params):
    print(f"params = {params}")
    print(f"key_params = {key_params}")


fifth_function(1, 2, x=10, y=20)
fifth_function(x=10, y=20)
# fifth_function( x=10, y=20, 30) doesn't work

"""
Using type hints 
"""


def get_combined_len(s1: str, s2: str) -> int:
    return len(s1 + s2)


print(get_combined_len("hello", "him"))

"""
With Python 3.9, it looks there are 2 ways to provide type hints

https://stackoverflow.com/questions/39458193/using-list-tuple-etc-from-typing-vs-directly-referring-type-as-list-tuple-etc 
"""


def process_list1(array1: list[int]) -> list[int]:
    print(array1)
    return array1


from typing import List


def process_list2(array1: List[int]) -> List[int]:
    print(array1)
    return array1

process_list1([1, 5, 7, 9])
process_list2([1, 5, 7, 9])

"""
Type aliases are also available
https://docs.python.org/3/library/typing.html#type-aliases

you can use the "type" keyword to create new types.

"""

Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector)

## The above is 3.8 and 3.9 syntax; 3.12 has a different one.
"""
Class inheritance and Exception Handling

In python everything is a checked exception.
Even runtime errors are subclasses of the Exception class.

Not really BaseException is the superclass of all classes
Exception is its sub class, and is the base class of all non fatal exceptions.

Other sub-classes of BaseException include SystemExit produced by sys.exit()
and KeyboardInterrupt. These are typically not meant to be handled
"""
f = FileNotFoundError()
print(isinstance(f, Exception))

a = ValueError()
print(isinstance(a, Exception))

b = ZeroDivisionError()
print(isinstance(b, Exception))

se = SystemExit()
print(isinstance(se, Exception))
print("Is SystemExit and instance of BaseException? ", isinstance(se, BaseException))

"""
Simple try catch
"""
print("Looking for user input: ")
while True:
    try:
        x = int(input("enter a valid number: "))
        print(x)
        break
    except ValueError:
        print("That's not a valid number")

"""
Except can catch multiple exceptions 
"""
try:
    print("Just for fun")
except (ValueError, RuntimeError, NameError):
    print("You have raised one of the 3")

"""
Just like java, if there are multiple except clauses, put the 
specific ones on top, the generalized ones at the bottom.
"""


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass

"""
raise the exceptions 1 by 1.
The subclasses are on top, the superclasses are towards the bottom
"""
exception_classes = [B, C, D]
for ex_class in exception_classes:
    try:
        raise ex_class()

    except D:
        print("Raised D")
    except C:
        print("Raised C")
    except B:
        print("Raised B")

"""
Just as in java, the Exception objects can be manipulated inside the handling block
"""

try:
    raise Exception("Idli", "Dosa")
except Exception as e:
    print(e)
    print(type(e))
    print(e.args)

    a, b = e.args
    print(f"The args are {a}, {b}")


"""
You can chain exceptions using the "from" keyword, this will make it clearer
Throwing another exception without "from" will also work 


def err_func():
    raise NameError

try:
    err_func()
except NameError as ne:
    raise RuntimeError from ne
    
"""

try:
    print("Hello - no errors here")
except NameError:
    print("This error shouldn't have happened")
else:
    print("This is being printed because there werent't any exceptions")
finally:
    print("This will always be printed")

"""
Read this https://docs.python.org/3/tutorial/errors.html
for exception groups, adding notes to exceptions etc.

File Handling:
"""

with open("input.txt", encoding="utf-8") as file_ref:

    lines = file_ref.readlines()
    print(lines)
    for i, line in enumerate(lines):
        print(f" line number {i} is {line}")
    file_ref.close()

"""
Above was reading lines, below reads the whole file
"""

with open("input.txt", encoding="utf-8") as file_ref:
    file_data = file_ref.read()
    print(file_data)
    file_ref.close()

"""
The open method takes 3 parameters
1. File name/path
2. Mode - read, write, append
3, Encoding.
"""
with open("output_second.txt", 'w') as write_ref:
    write_ref.write("This is a sample write to the file")

"""
The import statement combines two operations; 
it searches for the named module, 
then it binds the results of that search to a name in the local scope.
"""

# 2 ways of importing
import random
courses = ['SST', 'Science', 'English', 'Hindi']
print(random.choice(courses))

from sys import path
print(path)
# Now this path is just like a list, you can append locations to it and import from those locations.
# i.e. it is equal to Java - classpath (finds java classes)

print(random.__file__)
# The above is called the dunder file, it is available in a few modules but not in sys etc

"""
When the __init__.py file is present in a directory, Python treats that directory as a package. 
This file can be empty, or it can contain Python code that initializes the package. T
This code is executed when the package is imported.

In addition to initializing packages, __init__.py can also 
be used to initialize individual modules within a package. 
"""

from email.mime.text import MIMEText
arbitrary_mime_text = MIMEText("Mary had a little lamb")
print(arbitrary_mime_text)

import email
some_mime = email.mime.text.MIMEText("hello hello hello")
print(some_mime)

from email.mime import text
random_mime = text.MIMEText("xyz")
print(random_mime)
"""
mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    ├── module3.py
    └── module4.py

The general structure 

Packages are directories
Sub Packages are directories
Modules are files, they contain classes, variables etc.

In import, the . operator is used to separate packages from sub packages or modules.
Not modules from their contained entities

but it can be done in the usage as above.

Relative imports can also be done - . = current directory, .. = parent directory.
"""

if __name__ == "__main__":
    # Check if __spec__ is defined (available in Python 3.4 and later)
    print(__spec__)

"""
Class definitions:

Empty classes
"""

class Employee:
    pass

emp = Employee()
print(emp)


emp.name = "Mashika De Alameida"
print(emp.name)
print(emp)

"""
With Constructor
"""
class Employee:
    def __init__(self, name):
        self._name = name

emp_t = Employee("Karthika Saran")
print(emp_t)
print(emp_t._name)

"""
Instance methods
"""
class Employee:
    def __init__(self, name):
        self._name = name

    def print_name(self):
        print(self._name)


emp_m = Employee("LJ")
print(emp_m)
emp_m.print_name()
# You applied a method on an older version of the class which didn't have print_name :)
Employee.print_name(emp_t)


"""
Class variables, changing in class vs changing in instance
"""
class Employee:

    id = 100
    # should not be assigned using self

    def __init__(self, name):
        self._name = name

    def print_name(self):
        print(self._name)

e1 = Employee("Gany")
e2 = Employee("Dhivya")
print(f" the 2 employee ids are {e1.id}, {e2.id}")

Employee.id = 200
print(f" the 2 employee ids are {e1.id}, {e2.id}")

e1.id = 300
print(f" the 2 employee ids are {e1.id}, {e2.id}")

"""
Class methods, class methods as factory methods
"""

class Employee:

    inc = 0.05
    # should not be assigned using self

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def print_name(self):
        print(self.first_name +" "+ self.last_name)

    @classmethod
    def create_from_str(cls, input_str):
        first_name, last_name, salary = input_str.split("-")
        return cls(first_name, last_name, float(salary))

    @classmethod
    def get_increment(cls, salary):
        return cls.inc * salary + salary

    def get_future_salary(self):
        return Employee.get_increment(self.salary)

    @staticmethod
    def is_above_threshold(in_employee, threshold):
        return in_employee.salary > threshold


emp = Employee.create_from_str("Ram-Niranjan-5000")
print(emp.print_name())
print(emp.get_future_salary())
print(Employee.is_above_threshold(emp, 4500))

"""
Class Inheritance
"""

class A:
    def __init__(self):
        print("I'm in Class A's init")

a = A()

class B(A):
    def __init__(self):
        print("I'm in Class B's init")
        # so calling B's init is not going to call A's init automatically
b = B()


class C(A):
    def __init__(self):
        super().__init__()
        # so the super class's init has to be explicitly called.
        print("I'm in Class C's init")

c = C()

"""
Multiple Inheritance
"""
class North:
    def __init__(self):
        print("In North constructor")


class West(North):
    def __init__(self):
        print("In West constructor")
        super().__init__()


class East(North):
    def __init__(self):
        print("In East constructor")
        super().__init__()


class South(West, East):
    def __init__(self):
        print("In South constructor")
        super().__init__()


dakshin = South()
# despite the diamond shaped hierarchy, the North constructor is called only once

"""
issubclass and isinstance
"""
print(f"is south a sub class of north? {issubclass(South, North)}")
# so is instance works with super class also
print(f"is dakshin an instance of north? {isinstance(dakshin, North)}")

"""
private methods
"""

class Shell:
    def __inner_method(self):
        print(self.val)

    def outer_method(self):
        self.__inner_method()
        # class methods can invoke the private method

    def __init__(self, val):
        self.val = val

s = Shell(55)

# s.__inner_method() this method is private, can't be done
s.outer_method()


class SecondShell(Shell):

    def __init__(self, val):
        super().__init__(val)

    def facade(self):
        # self.__inner_method() private methods can't be seen by the subclass, just like java.
        self.outer_method()


ss = SecondShell(84)
ss.facade()

"""
Super outside the constructor
"""

class City:
    def __init__(self):
        pass

    def get_something(self):
        return " Chodiye"

class Bombay(City):
    def __init__(self):
        pass

    def get_something(self):
        return f"Hello Hi {super().get_something()}"

b = Bombay()
print(b.get_something())

"""
property annotation, getter and setter
"""


class ScalarRep:
    """
    observe the setter's annotation
    """
    inner_val = 0

    @property
    def get_vector(self):
        return [self.inner_val, self.inner_val**2, self.inner_val**3]

    @get_vector.setter
    def set_vector(self, vector):
        self.inner_val = vector[0]


scalar = ScalarRep()
scalar.set_vector = [2, 4, 8]
print(scalar.get_vector)

"""
Magic methods
"""


class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.salary}"

    def __add__(self, other):
        """
        adds other's salary and return's self
        :param other:
        :return:
        """
        self.salary = self.salary + other.salary
        return self

    def __len__(self):
        """
        returns the full name length
        :return:
        """
        return len(self.first_name) + len(self.last_name) + 1


emp1 = Employee("Bhuvana", "Ganesh", 5500)
print("emp1 = ", emp1)
emp2 = Employee("Ramanan", "Chid", 5000)
print(emp2 + emp1)
print(len(emp2))
