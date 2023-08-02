from classes.stringed_instrument import StringedInstrument


class Guitar(StringedInstrument):
    """The Guitar class."""

    def __init__(self, brand, model, num_strings=6):
        """Creates an instance of the Guitar class."""

        super().__init__(brand, model, num_strings)

    def __str__(self):
        """A human-readable representation of the instance."""

        return f"<Guitar: {self.brand} {self.model}>"

    # Overriding the parent method
    def play(self):
        """
        Changes the instance's `is_playing` attribute to True
        and prints an informative string.
        """

        self.is_playing = True
        print(f"The {self.brand} {self.model} is being shredded upon.")
        return self
