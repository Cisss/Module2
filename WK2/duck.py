class Duck:
    def __init__(self):
        self._vleugel = Vleugel(1.8)

    def vliegen(self):
        self._vleugel.vliegen()

    def lopen(self):
        print("Waggel, waggel, waggel")

    def zwemmen(self):
        print("Kom er lekker in, het water is heerlijk")

    def kwaken(self):
        print("Kwak, kwak, kwak")

class Pinguin(object):
    def lopen(self):
        print("Waggel, waggel, ik waggel ook")

    def zwemmen(self):
        print("Kom er in, maar het is wel een beetje koud, zo zuidelijk")

    def kwaken(self):
        print("Kwaken? Lachen, ik ben een pinquin, hoor!")

class Vleugel:

    def __init__(self, ratio):
        self.ratio = ratio

    def vliegen(self):
          if self.ratio > 1:
               print("Wauwwww, dit is fun")
          elif self.ratio == 1:
               print("Pff, hard werken, maar ik vlieg tenminste")
          else:
               print("Ik denk dat ik maar weer gewoon ga waggelen")





def test_duck(duck):
    duck.lopen()
    duck.zwemmen()
    duck.kwaken()

if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)
    donald.vliegen()
    percy = Pinguin()
    test_duck(percy)