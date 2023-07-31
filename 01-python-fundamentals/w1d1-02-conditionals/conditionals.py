# If Statement
x = 10

if x > 5:
    print("x is greater than 5")

# If-Else Statement:
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")


# If-Elif-Else
x = 10

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

# Boolean Operators
# <, >, ==, &, |, and, or, <=, >=

is_monday = True
is_home = False

if is_monday and is_home:
    print("It's Monday and I'm home.")

if is_monday or is_home:
    print("It's either Monday or I'm home.")

if x < 10 and x > 5:
    print("x is between 5 and 10")
