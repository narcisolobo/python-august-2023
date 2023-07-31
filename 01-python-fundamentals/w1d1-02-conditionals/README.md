# Conditionals (If Statements)

In Python, conditional statements are used to make decisions in the code based on certain conditions. They allow the program to execute different blocks of code depending on whether a specific condition is true or false. The most common conditional statements in Python are:

1. if statement:  
The if statement is used to check a condition, and if it evaluates to True, the indented block of code below it will be executed. If the condition is False, the block will be skipped.

```py
x = 10

if x > 5:
    print("x is greater than 5")
```

2. if-else statement:  
The if-else statement is used when you want to execute one block of code if the condition is True, and a different block of code if the condition is False.

```py
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

3. if-elif-else statement:  
The if-elif-else statement is used when you have multiple conditions to check. It allows you to specify several conditions and their corresponding blocks of code. The elif stands for "else if."

```py
x = 10

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")
```

4. Nested if statements:  
You can also nest conditional statements within each other to create more complex decision-making logic.

```py
# Example of nested if statements
x = 10
y = 5

if x > 5:
    if y > 2:
        print("Both x and y are greater than their respective thresholds.")
    else:
        print("x is greater than 5, but y is not greater than 2.")
else:
    print("x is not greater than 5.")
```

Remember to indent the code blocks correctly, as Python uses indentation to determine which code belongs to a specific conditional statement. The standard indentation in Python is four spaces.

Conditional statements are fundamental to control the flow of your program and allow it to make decisions based on different scenarios.