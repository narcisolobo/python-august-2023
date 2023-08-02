# package import syntax
from classes.guitar import Guitar


class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.guitar = Guitar("Fender", "Telecaster")

    def display_info(self):
        """Prints all of the users' details on separate lines."""

        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}, Age: {self.age}")

    def play_guitar(self):
        self.guitar.play()
