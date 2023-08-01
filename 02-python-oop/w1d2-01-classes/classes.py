# Class names are singular nouns and in PascalCase
class Guitar:
    # constructor function (dunder init)
    def __init__(self, brand, model, num_strings=6):
        self.brand = brand
        self.model = model
        self.num_strings = num_strings
        self.is_playing = False

    def __str__(self):
        return f"<Guitar: {self.brand} {self.model}>"

    # Instance methods always take self as the
    # first parameter
    def play(self):
        self.is_playing = True
        print(f"The {self.brand} {self.model} is being played.")
        return self

    def stop_playing(self):
        self.is_playing = False
        print(f"The {self.brand} {self.model} has stopped playing.")
        return self

    def change_strings(self, new_num_strings):
        self.num_strings = new_num_strings
        print(f"Changed to {self.num_strings} strings.")
        return self.num_strings


# Instantiating an object of type Guitar
fender = Guitar("Fender", "Stratocaster", 7)

# Accessing values using dot notation
print(fender.num_strings)

print(fender.play())
print(fender.is_playing)
print(fender.stop_playing())
print(fender.is_playing)

print(fender.change_strings(12))
print(fender.num_strings)

# If you want to chain off a method, that method
# must return self
fender.play().stop_playing()


# If a method is already returning a value, then
# that method cannot be chained off of
fender.change_strings()
