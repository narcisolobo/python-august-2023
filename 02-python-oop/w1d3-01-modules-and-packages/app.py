# Import statement - importing a class from a package
from classes.user import User
from classes.guitar import Guitar

user1 = User("Kermit", "Frog", "kermit@frog.com", 44)

guitar1 = Guitar("Gibson", "Les Paul")
guitar2 = Guitar("Fender", "Stratocaster")

# accessing a class attribute on the class itself
print(Guitar.num_of_guitars)

# accessing a class attribute on an instance of the class
print(guitar1.num_of_guitars)

Guitar.display_standard_tuning()

print(guitar1.serial_number)
print(guitar2.serial_number)

print(user1.guitar.brand)
user1.play_guitar()
