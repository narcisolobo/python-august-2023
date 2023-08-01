"""
Python Functions
"""


def greet(name):
    print("Hello, " + name)


def greet_with_annotations(name: str):
    print("Hello, " + name)


greet("Kenneth")
greet_with_annotations("Mike")

"""
The return keyword
"""


# Return keyword returns a value to the caller
def greet_with_return(name):
    return f"Hello, {name}"


# In this example, greeting is the caller
greeting = greet_with_return("Elle")
print(greeting)

"""
Scope in functions
Scope is the block of code where a variable exists
"""


x = 3  # Global variable
y = 4
hello = "hello"


def multiply(a, b):
    result = a * b  # Local variable
    print(hello)  # Global variables exist here
    return result


product = multiply(x, y)
print(product)  # Output: 12
