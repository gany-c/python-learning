import sys

print("Python Version:", sys.version)

# Strings

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

"""
Logical conditions and branching
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

