"""
Looks like range itself is an object
"""
x = range(3)
print(x)

for i in range(5):
    print(f" i = {i}")

for i in range(20, 30, 3):
    print(f"j = {i}")

"""
java style for loop with index and value - use enumerate
"""
print("for loop")

in_list = [1, 2, 3, 4, 5]

for index, val in enumerate(in_list):
    print(f"index = {index} and value = {val}")



