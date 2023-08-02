from classes.stringed_instrument import StringedInstrument


class Ukulele(StringedInstrument):
    """The Ukulele class."""

    def __init__(self, brand, model, num_strings=4):
        """Creates an instance of the Ukulele class."""

        super().__init__(brand, model, num_strings)

    def __str__(self):
        """A human-readable representation of the instance."""

        return f"<Ukulele: {self.brand} {self.model}>"

    # Overriding the parent method
    def play(self):
        """
        Changes the instance's `is_playing` attribute to True
        and prints an informative string.
        """

        self.is_playing = True
        print(f"The {self.brand} {self.model} is being strummed.")
        return self
