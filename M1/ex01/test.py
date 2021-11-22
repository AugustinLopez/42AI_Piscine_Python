#!/usr/bin/env python

from game import GotCharacter, Stark


Random = GotCharacter()
Extra = GotCharacter("Extra", False)
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
