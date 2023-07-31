"""
COMPOSITE (COMPLEX) DATATYPES
- Lists (list)
- Dictionaries (dict)
"""

"""
=== === LISTS === ===
In Python, arrays are called lists. You can
create them as you would an array. Use square
brackets and comma separators.
"""

# List creation
colors = ["rebeccapurple", "cornflowerblue", "goldenrod", "firebrick", "darkorchid"]

# List indices
"""
Lists have indices just like arrays have indices in
JavaScript. They are also zero-indexed as well.
"""

print(colors[1])
colors[1] = "kellygreen"
print(colors)

# List negative indices
"""
Python supports negative indices. A -1 index will refer
to the last element in a list.
"""

print(colors[-2])

# Common list methods
"""
There are many useful methods we can use with lists.
"""

# length
"""
Pass a list to the len() method to return the number of
elements in the list.
"""
print(len(colors))

for i in range(len(colors)):
    print(colors[i])

# append, remove, pop
"""
append() - adds an element to the end of a list.
remove() - removes the specified element from a list.
pop() - removes the element at the specified position
"""

colors.append("hotpink")
print(colors)

colors.remove("goldenrod")
print(colors)

colors.pop(1)
print(colors)

# sort, reverse
"""
The sort() method sorts a list in ascending order in-place.
The reverse() method reverses a list.
"""

nums = [5, 8, 2, 9, 11, 3]
words = ["pig", "dog", "zebra", "cat", "bunny"]

nums.sort()
print(nums)
words.sort()
print(words)

nums.reverse()
print(nums)
words.reverse()
print(words)

# Explore more list methods!
# https://www.w3schools.com/python/python_ref_list.asp

"""
=== === DICTIONARIES === ===
Python dictionaries are collection datatypes. We can
store a series of key-value pairs in these collections.
Use curly braces at the bookends, separate each element
with a comma, use a colon between keys and values, and
surround the key name with quotation marks.
"""

# Dictionary creation
strat = {
    "brand": "Fender",
    "model": "Stratocaster",
    "year": 1977,
    "color": "blue",
    "is_new": False,
}

# Accessing values with bracket notation
"""
We can access values in a dictionary by their
key names. Use bracket notation with quotes.
"""

print(strat["year"])
strat["year"] = 1983
print(strat["year"])

# Accessing values with the get() method
"""
We can access values in a dictionary with the get()
method. Pass the key name in the method call in quotes.
"""

print(strat.get("model"))

"""
What's the difference between bracket notation and .get()?
With .get(), our application doesn't break if we specify
a key name that doesn't exist.
"""

# print(strat["owner"])
print(strat.get("owner"))

# Dictionary methods
"""
There are many useful methods we can use with lists.
"""

# keys, values, items
"""
.keys() - returns an array of the dictionary's keys.
.values() - returns an array of the dictionary's values.
.items() - returns an array of tuples of the dictionary's key-value pairs.
"""

print(strat.keys())
print(strat.values())
print(strat.items())

# in, not in
"""
We can use the 'in' and 'not in' keywords to check if a key
name exists in a dictionary.
"""

if "owner" in strat:
    print("owner in strat")
else:
    print("owner not in strat")

# Explore more dictionary methods!
# https://www.w3schools.com/python/python_ref_dictionary.asp
