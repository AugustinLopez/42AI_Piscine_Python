#!/usr/bin/env python

class GotCharacter:
    """Not having a great house name in the GoT world is rough.
"""
    def verify_name(self, name):
        if isinstance(name, str) is False and name != None:
            raise TypeError("Expected str or None. Got" + str(type(name)))
        return (name)

    def verify_is_alive(self, is_alive):
        if isinstance(is_alive, bool) is False:
            raise TypeError("is_alive is not a boolean")
        return (is_alive)

    def __init__(self, first_name=None, is_alive=True):
        self.first_name: str = self.verify_name(first_name)
        self.is_alive: bool = self.verify_is_alive(is_alive)


class Stark(GotCharacter):
    """A class representing the Stark family. \
Or when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name: str = "Stark"
        self.house_words: str = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

Random = GotCharacter()
print(str(Random.first_name) + " " + str(Random.is_alive))
Extra = GotCharacter("Extra", False)
print(str(Extra.first_name) + " " + str(Extra.is_alive))
print(Extra.__doc__)
Eddard = Stark()
print(Eddard.__dict__)
Eddard.print_house_words()
print(Eddard.is_alive)
Eddard.die()
print(Eddard.is_alive)
print(Eddard.__doc__)
Arya = Stark("Arya")
print(Arya.is_alive)
