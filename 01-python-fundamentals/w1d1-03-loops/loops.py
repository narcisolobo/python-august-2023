# Loops in Python

# Two major types of loops: for loops and while loops.

"""
For loops with range()
range takes in three arguments - start, stop, and step
The range function has a default of 0 for start
and a default of 1 for step
CAVEAT - if you pass a step, you must also pass start and stop
"""

for i in range(1, 5):
    print(i)

"""
Behind the scenes this loop is a "for in" loop.
A for in loop requires an iterator (i) and an
iterable (range(1, 5))
"""

print(range(1, 5))

muppets = [
    {"name": "Kermit the Frog", "location": "The swamp. I'm a frog."},
    {"name": "Miss Piggy", "location": "The green room. Where's my champagne?"},
    {"name": "Fozzie Bear", "location": "The Comedy Store - tonight at 8!"},
    {"name": "Gonzo the Great", "location": "Waiting to be shot out of a cannon."},
]

for i in range(len(muppets)):
    print(muppets[i]["name"])

for muppet in muppets:
    print(muppet["name"])

"""
In the second loop, our iterator is muppet,
and the iterable is the muppets list.
"""
