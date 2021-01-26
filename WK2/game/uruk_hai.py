import random
from aardman import Aardman

class UrukHai(Aardman):
    def __init__(self, naam):
        super().__init__(naam=naam, levens=3, hit_points=12)
        self._naam = naam

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("***** {0._naam} dodges *****".format(self))
            return True
        else:
            return False

    def schade(self, geraakt):
        if not self.dodges():
            super().schade(geraakt=geraakt) 