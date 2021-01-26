import datetime

class Bankrekening:

	def __init__(self, naam, saldo):
		self._name = naam
		self.__saldo = saldo
		# create public var _transaction_overzicht set saldo as first transaction
		self._transactie_overzicht = [(Bankrekening.current_time(), self.__saldo)]
		print("Bankrekening aangemaakt voor " + self._name + " met " + str(self.__saldo) + " euro.")

	def current_time():
		now = datetime.datetime.now()
		return (now.strftime("%Y-%m-%d %H:%M:%S"))

	def storten(self, bedrag):
		if bedrag > 0:
			self.__saldo += bedrag
			self._transactie_overzicht.append( (Bankrekening.current_time(), bedrag) )
			self.toon_saldo()

	def toon_saldo(self):
		print("Saldo bedraagt {}".format(self.__saldo))

	def opnemen(self, bedrag):
		if 0 < bedrag <= self.__saldo:
			self.__saldo -= bedrag
			self._transactie_overzicht.append((Bankrekening.current_time(), -bedrag))
			self.toon_saldo()
		else:
			print("Het bedrag dient groter dan nul (0) en maximaal gelijk aan het saldo te zijn")
			self.toon_saldo()

	def toon_transacties(self):
		for date, bedrag in self._transactie_overzicht:
			if bedrag > 0:
				trans_type = "gestort"
			else:
				trans_type = "opgenomen"
				bedrag *= -1
			print("{} {} op {}".format(bedrag, trans_type, (Bankrekening.current_time())))
