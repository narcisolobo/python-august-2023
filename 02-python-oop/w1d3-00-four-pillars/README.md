# The Four Pillars of OOP
The Four Pillars of Object-Oriented Programming (OOP) are a set of principles that guide the design and implementation of object-oriented systems. These pillars are encapsulation, abstraction, inheritance, and polymorphism. Each pillar represents a fundamental concept that helps in building robust and maintainable code.

They are often remembered by an acronym - APIE.

## Encapsulation: Bundling Data and Behavior
Encapsulation is the concept of bundling data (attributes) and behavior (methods) together within a class. It allows us to create self-contained objects that hide their internal details and provide controlled access to their functionalities. In our Guitar class, we can see encapsulation in action. The attributes like "manufacturer," "number_of_strings," and methods like "play" and "tune" are encapsulated within the class, ensuring that they are accessed and modified only through defined interfaces.

Encapsulation promotes information hiding, as the internal implementation details of a class are not exposed to the outside world. It provides data protection and prevents unwanted external access, ensuring the integrity and consistency of the object's state.

## Abstraction: Simplifying Complexity

Abstraction is the process of simplifying complex systems by focusing on the essential aspects and hiding unnecessary details. In the context of the Guitar class, abstraction allows us to represent the concept of a guitar without concerning ourselves with the intricate inner workings of the instrument. We can interact with the Guitar object using its public interface (methods) without needing to know the specific implementation details.

Abstraction allows us to create classes and objects that model real-world entities or concepts in a simplified manner. By abstracting away complex details, we can manage the complexity of our codebase, enhance code readability, and make it easier to maintain and extend our systems.

**Encapsulation** and **abstraction** are crucial pillars of OOP that promote modularity, code organization, and code reusability. Encapsulation ensures that objects maintain their integrity and follow defined access rules, while abstraction simplifies the complexity of systems by focusing on the essential aspects. By leveraging encapsulation and abstraction effectively, we can write clean, modular, and maintainable code that reflects the real-world entities and concepts we are modeling.

**Inheritance** and **Polymorphism** are fundamental concepts in object-oriented programming that allow us to create relationships between classes and enhance code reusability. Inheritance enables us to define a new class based on an existing class, inheriting its properties and behaviors. Polymorphism, on the other hand, allows objects of different classes to be treated as objects of a common parent class.

## Inheritance: Building a Hierarchy

```py
class StringedInstrument:
    def __init__(self, brand, model, num_strings, is_playing=False):
        self.brand = brand
        self.model = model
        self.num_strings = num_strings
        self.is_playing = is_playing

    def play(self):
        self.is_playing = True
        print(f"The {self.brand} {self.model} is now being played.")

    def stop_playing(self):
        self.is_playing = False
        print(f"The {self.brand} {self.model} has stopped playing.")

```

In our example, we have a parent class called `StringedInstrument`. This class represents the common attributes and behaviors shared by different types of stringed instruments. Let's rewrite the `Guitar` class as a child class of `StringedInstrument`.

```py
class Guitar(StringedInstrument):
    def __init__(self, brand, model, num_strings=6, is_playing=False):
        super().__init__(brand, model, num_strings, is_playing)
```

The Guitar class, as a child class, will inherit these characteristics from the StringedInstrument class. By using inheritance, we can avoid duplicating code and organize our classes in a logical hierarchy.

We can now create as many child classes as necessary.

```py
class Ukulele(StringedInstrument):
    def __init__(self, brand, model, num_strings=4, is_playing=False):
        super().__init__(brand, model, num_strings, is_playing)
```
## Polymorphism: Adapting Behavior Across Different Classes

Polymorphism is a powerful concept in object-oriented programming that enables objects of different classes to respond differently to the same method call. It means, "many forms". In our example, both the `Guitar` and `Ukulele` classes inherit from the StringedInstrument class, which establishes a common parent class relationship.

When we call a method, such as `play()`, on these objects, the actual implementation that gets executed is determined by the specific subclass. Each instrument class can override the method and provide its own unique behavior. This flexibility of polymorphism allows us to write code that can work with various instruments, each producing a different sound or exhibiting distinct behavior, while still adhering to a common interface provided by the parent class.

Let's expand the `Guitar` and `Ukulele` classes to implement the `play()` method uniquely.

```py
class Guitar(StringedInstrument):
    def __init__(self, brand, model, num_strings=6, is_playing=False):
        super().__init__(brand, model, num_strings, is_playing)
    
    def play(self):
        self.is_playing = True
        print(f"The {self.brand} {self.model} is now being picked.")


class Ukulele(StringedInstrument):
    def __init__(self, brand, model, num_strings=4, is_playing=False):
        super().__init__(brand, model, num_strings, is_playing)

    def play(self):
        self.is_playing = True
        print(f"The {self.brand} {self.model} is now being strummed.")
```

