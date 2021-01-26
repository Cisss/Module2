class Speler:

    def __init__(self, naam):
        self.naam = naam
        self.__levens = 3
        self.__level = 1
        self.score = 0

    def _get_levens(self):
        return self.__levens

    def _set_levens(self, levens):
        if levens >= 0:
            self.__levens = levens
        else:
            print("Levens kunnen geen negatieve waarde krijgen")
            self.__levens = 0
   
    def _get_level(self):
        return self.__level

    def _set_level(self, level):
        if level > 0:
            delta = level - self.level
            self.score += delta * 1000
            self.__level = level
        else:
            print("Het laagste level is level 1") 

    def __str__(self):
        return "Naam: {0.naam}, Levens: {0.levens}, Level: {0.level}, Score {0.score}".format(self)
    
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score
    
    levens = property(_get_levens, _set_levens)
    level = property(_get_level, _set_level)
