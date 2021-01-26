from aardman import Aardman
from ork import Ork, Mordor, Saruman
from uruk_hai import UrukHai

print("__uruk hai__")
lurtz = UrukHai("Lurtz")
print(lurtz)
lurtz.schade(14)
print(lurtz)

while lurtz._levend:
    lurtz.schade(5)
    print(lurtz)

# ugluk = UrukHai("Ugluk")
# print(ugluk)

# print("")
# print("__orks schade testen__")
# ordan = Ork("Ordan")
# ordan.schade(7)

# print("")
# print("__Mordor__")
# gothmog = Mordor("Gothmog")
# print(gothmog)
# gothmog.schade(12)
# print(gothmog)

# print("")
# print("__Saruman__")
# grimrog = Saruman("Grimrog")
# print(grimrog)
# grimrog.schade(16)
# print(grimrog)
