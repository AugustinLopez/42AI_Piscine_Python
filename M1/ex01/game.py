class GotCharacter:
    """Not having a great house name in the GoT world is rough."""
    def verify_name(self, name):
        if not (isinstance(name, str) or name is None):
            raise TypeError("Expected str or None. Got" + str(type(name)))
        return (name)

    def verify_is_alive(self, is_alive):
        if isinstance(is_alive, bool) is False:
            raise TypeError("is_alive is not a boolean")
        return (is_alive)

    def __init__(self, first_name=None, is_alive=True):
        self.first_name: str = self.verify_name(first_name)
        self.is_alive: bool = self.verify_is_alive(is_alive)
        print("Spawned Character " + str(self.first_name), end='')
        if self.is_alive:
            print(". Alive.")
        else:
            print(". Already dead.")


class Stark(GotCharacter):
    """A class representing the Stark family. \
Or when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        print("It is a Stark !")
        self.family_name: str = "Stark"
        self.house_words: str = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
