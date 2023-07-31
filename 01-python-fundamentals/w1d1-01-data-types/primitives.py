import math

"""
PRIMITIVE (SIMPLE) DATATYPES
- Strings (str)
- Integers (int)
- Floating Point Numbers (float)
- Booleans (bool)
- None (NoneType)
"""

"""
=== === Strings === ===

Strings represent sequences of characters enclosed
in quotes.
"""
# String creation:
print("This is a string".title())

# Literal assignment
my_string = "Like so."
print(my_string.center(50, "*"))

# Constructor function
my_other_string = str("Another string")
print(my_other_string)
my_number = 56
print(type(my_number))
stringified = str(my_number)
print(type(stringified))

# Print function
print("Hello world.")

# Type function
type(my_string)  # Type tells us the datatype of an object.

# Concatenation
hello = "Hello "
world = "world!"

hello_world = hello + world
print(hello_world)
# print(hello_world + 5)  # TypeError
print(hello_world + str(5))  # Fix

# String Methods
print(hello_world.rsplit(" "))  # splits a string based on a separator

# upper, lower, title
print("This is a string".upper())
print("This is a string".lower())
print("This is a string".title())

# length
print(len(hello_world))
print(len("sup bro"))

# strip
whitespace_string = "     hello       "
stripped = whitespace_string.strip()
print(stripped)

# string indices, index ranges
print(hello_world[0])

# Explore more string methods!

"""
=== === BOOLEANS === ===
"""

# Literal assignment
is_awake = True
has_all_pokemon = False
# snake case - every letter is lowercase and
# every word is separated by an underscore

# Logical operators this afternoon

"""
=== === INTEGERS AND FLOATS === ===
"""

# Integer literal assignment
num_of_scoops = 2

# Float literal assignment
pi = 3.14159

# Arithmetic operations
# +, -, *, /, **, //
print(2**3)
print(5 // 2)

# +=, -=, *=, /= assignment operators
x = 2
x = x + 8
x += 2  # alternative to above

# Built-in functions for numbers

# abs, round

# Math module

# sqrt, ceil, floor
print(math.ceil(pi))
print(math.floor(pi))
print(math.sqrt(9))

"""
=== === NONE === ===
"""

# Why use None?
# Sometimes we want values to be optional
# To control code flow

# Constructor functions and casting
five = "5"
print(type(five))
int_five = int(five)
print(type(int_five))

string_true = "True"
bool_true = bool(string_true)
print(type(bool_true))
print(bool_true)
