# Loops
In Python, loops are used to execute a block of code repeatedly until a specific condition is met. There are two main types of loops in Python: for loops and while loops.

## `for` Loop:
The `for` loop is used when you have a specific number of iterations or when you want to iterate over a sequence (such as a list, string, or range of numbers). Here's the general syntax of a `for` loop:

```py
for item in sequence:
    # Code block to be executed
```
In each iteration, the loop variable `item` takes the value of the current item in the sequence. The code block indented under the `for` loop is executed repeatedly for each item in the sequence until the end is reached.

**Example 1: Iterating over a list**
```py
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```
**Example 2: Iterating over a range of numbers**
```py
for i in range(1, 6):
    print(i)
```

## `while` Loop:
The `while` loop is used when you want to repeatedly execute a block of code as long as a condition remains `True`. Here's the general syntax of a `while` loop:

```py
while condition:
    # Code block to be executed
```
The code block is executed as long as the condition remains `True`. Once the condition becomes `False`, the loop is exited, and the program continues with the next statement after the loop.

**Example:**
```py
count = 0
while count < 5:
    print(count)
    count += 1
```
In this example, the loop starts with `count` equal to 0. The code block is executed as long as `count` is less than 5. In each iteration, it prints the current value of `count` and increments it by 1. The loop continues until `count` reaches 5, at which point the condition becomes `False`, and the loop is exited.

It's important to ensure that your loops have an exit condition to prevent infinite looping. You can use loop control statements like `break` and `continue` to control the flow within loops, allowing you to skip iterations or prematurely exit the loop based on specific conditions.
