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
