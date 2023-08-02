class Guitar:
    """The Guitar class."""

    def __init__(self, brand, model, num_strings=6):
        """Creates an instance of the Guitar class."""

        self.brand = brand
        self.model = model
        self.num_strings = num_strings
        self.is_playing = False

    def __str__(self):
        """A human-readable representation of the instance."""

        return f"<Guitar: {self.brand} {self.model}>"

    def play(self):
        """
        Changes the instance's `is_playing` attribute to True
        and prints a informative string.
        """

        self.is_playing = True
        print(f"The {self.brand} {self.model} is being played.")
        return self

    def stop_playing(self):
        """
        Changes the instance's `is_playing` attribute to False
        and prints a informative string.
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
