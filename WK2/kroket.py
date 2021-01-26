class Kroket(object):
	soort = "runvleeskroket"
	def __init__(self, leverancier, prijs):
		self.leverancier = leverancier
		self.prijs = prijs
		self.trek = False

	def in_frituur(self):
		self.trek = True