import uuid
import utilities  # custom module


class Guitar:
    """The Guitar class."""

    num_of_guitars = 0  # class attribute

    def __init__(self, brand, model, num_strings=6):
        """Creates an instance of the Guitar class."""

        self.serial_number = uuid.uuid4()
        self.brand = brand
        self.model = model
        self.num_strings = num_strings
        self.is_playing = False
        Guitar.increase_num_of_guitars()

    def __str__(self):
        """A human-readable representation of the instance."""

        return f"<Guitar: {self.brand} {self.model}>"

    @classmethod
    def increase_num_of_guitars(cls):
        cls.num_of_guitars += 1

    @staticmethod
    def display_standard_tuning():
        print("E, A, D, G, B, E")

    def play(self):
        """
        Changes the instance's `is_playing` attribute to True
        and prints an informative string.
        """

        self.is_playing = True
        print(f"The {self.brand} {self.model} is being played.")
        return self

    def stop_playing(self):
        """
        Changes the instance's `is_playing` attribute to False
        and prints an informative string.
        """

        self.is_playing = False
        print(f"The {self.brand} {self.model} has stopped playing.")
        return self

    def change_strings(self, new_num_strings):
        """
        Changes the instance's `num_strings` attribute to the
        given new number of strings.
        """

        self.num_strings = new_num_strings
        print(f"Changed to {self.num_strings} strings.")
        return self.num_strings
