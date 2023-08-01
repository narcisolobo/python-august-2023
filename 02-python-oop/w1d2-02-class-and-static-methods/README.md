# Class and Static Methods
Let's revisit our `Guitar` class and add class and static methods.

```py
class Guitar:
    num_guitars_in_stock = 0  # Class attribute

    def __init__(self, brand, model, num_strings = 6):
        self.brand = brand
        self.model = model
        self.num_strings = num_strings
        self.is_playing = False
        Guitar.num_guitars_in_stock += 1

    def start_playing(self):
        self.is_playing = True
        print(f"The {self.brand} {self.model} is now being played.")

    def stop_playing(self):
        self.is_playing = False
        print(f"The {self.brand} {self.model} has stopped playing.")

    @classmethod
    def display_stock(cls):
        print(f"Number of guitars in stock: {cls.num_guitars_in_stock}")

    @staticmethod
    def standard_tuning():
        print("E, A, D, G, B, E")


# Create instances of the Guitar class
guitar1 = Guitar("Fender", "Stratocaster", 6)
guitar2 = Guitar("Gibson", "Les Paul", 6)

# Access class attributes and call class methods
print(Guitar.num_guitars_in_stock)    # Output: 2
Guitar.display_stock()                # Output: Number of guitars in stock: 2

# Output: E, A, D, G, B, E
Guitar.standard_tuning()
```
