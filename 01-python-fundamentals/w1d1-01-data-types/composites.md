# COMPOSITE (COMPLEX) DATATYPES
- Lists (list)
- Dictionaries (dict)

## Lists
In Python, arrays are called lists. You can
create them as you would an array. Use square
brackets and comma separators.

### List creation
```py
colors = ["rebeccapurple", "cornflowerblue", "goldenrod", "firebrick", "darkorchid"]
```

### List indices

Lists have indices just like arrays have indices in
JavaScript. They are also zero-indexed as well.

```py
print(colors[1])  # cornflowerblue
```

### List negative indices

Python supports negative indices. A -1 index will refer
to the last element in a list.

```py
print(colors[-1])  # darkorchid
print(colors[-2])  # firebrick
```

### Common list methods

There are many useful methods we can use with lists.

```py
nums = [5, 8, 2, 9, 11, 3]
words = ["pig", "dog", "zebra", "cat", "bunny"]
```

### length

Pass a list to the len() method to return the number of
elements in the list.

```py
print(len(nums))  # 6
print(len(words))  # 4
```

### append, remove, pop
- `append()` - adds an element to the end of a list.
- `remove()` - removes the specified element from a list.
- `pop()` - removes the element at the specified position

```py
nums.append(1)
print(nums)  # [5, 8, 2, 9, 11, 3, 1]

words.remove("dog")
print(words)  #  ['pig', 'zebra', 'cat']

words.pop(3)
```

### sort, reverse

The sort() method sorts a list in ascending order in-place.
The reverse() method reverses a list.

```py
nums.sort()
print(nums)  # [1, 2, 3, 5, 8, 9, 11]
nums.reverse()
print(nums)  # [11, 9, 8, 5, 3, 2, 1]

words.sort()
print(words)  # ['cat', 'pig', 'zebra']
words.reverse()
print(words)  # ['zebra', 'pig', 'cat']
```

[Explore more list methods!](https://www.w3schools.com/python/python_ref_list.asp)

## Dictionaries
Python dictionaries are collection datatypes. We can
store a series of key-value pairs in these collections.
Use curly braces at the bookends, separate each element
with a comma, use a colon between keys and values, and
surround the key name with quotation marks.

## Dictionary creation
```py
strat = {
    "brand": "Fender",
    "model": "Stratocaster",
    "year": 1977,
    "color": "blue",
    "is_new": False,
}
```

## Accessing values with bracket notation

We can access values in a dictionary by their
key names. Use bracket notation with quotes.

```py
print(strat["year"])  # 1977
```

## Accessing values with the get() method

We can access values in a dictionary with the get()
method. Pass the key name in the method call in quotes.

```py
print(strat.get("is_new"))  # False
```

> What's the difference between bracket notation and .get()?  
> With .get(), our application doesn't break if we specify a key name that doesn't exist.

```py
# print(strat["non_existent_key"])  # KeyError: 'non_existent_key'
print(strat.get("non_existent_key"))  # None
```

## Dictionary methods
There are many useful methods we can use with lists.

### keys, values, items

- `.keys()` - returns an array of the dictionary's keys.
- `.values()` - returns an array of the dictionary's values.
- `.items()` - returns an array of tuples of the dictionary's key-value pairs.

```py
print(strat.keys())  # dict_keys(['brand', 'model', 'year', 'color', 'is_new'])
print(strat.values())  # dict_values(['Fender', 'Stratocaster', 1977, 'blue', False])
print(strat.items())
# dict_items([('brand', 'Fender'), ('model', 'Stratocaster'), ('year', 1977), ('color', 'blue'), ('is_new', False)])
```

### in, not in

We can use the 'in' and 'not in' keywords to check if a key
name exists in a dictionary.

```py
if "color" in strat:
    print("color exists in strat")

if "banana" not in strat:
    print("banana not in strat")
```

[Explore more dictionary methods!](https://www.w3schools.com/python/python_ref_dictionary.asp)
