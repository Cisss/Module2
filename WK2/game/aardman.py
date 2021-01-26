class Aardman:
    def __init__(self, naam="Aardman", hit_points=0, levens=1):
        self._naam = naam
        self._hit_points = hit_points
        self._levens = levens
        self._levend = True

    def schade(self, geraakt):
        punten_over = self._hit_points - geraakt
        if (self._levens <= 0 and punten_over <= 0):
            self._levend = False
            print(self._naam + " is overleden :(")
        else:    
            if (punten_over >= 0):
                self._hit_points = punten_over
                print("Je bent {} keer geraakt en hebt nog {} hit points over".format(geraakt, self._hit_points))
            else:
                self._levens -= 1
                print( self._naam + " is een leven verloren")
    
    def __str__(self):s
        return "Naam: {0._naam}, Levens: {0._levens}, Hit points: {0._hit_points}".format(self)