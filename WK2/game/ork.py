from aardman import Aardman

class Ork(Aardman):
    def __init__(self, naam):
        super().__init__(naam=naam, levens=1, hit_points=23)
    
    def slaan(self):
        print("Me {0._naam}. {0._naam} stomp you".format(self))


class Mordor(Ork):
    def __init__(self, name):
        super().__init__(name)
        self._hit_points = 140

    def schade(self, geraakt):
        super().schade(geraakt // 4)

class Saruman(Ork):
    def __init__(self, name):
        super().__init__(name)
        self._hit_points = 180
    
    def schade(self, geraakt):
        super().schade(geraakt // 8)