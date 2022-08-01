from abc import abstractmethod
from random import randint

class RPSObject:

	def __init__(self):
		self._beats = None

	def beats(self):
		return self._beats

	def __eq__(self, other):
		return self.__class__ == other.__class__

	def __gt__(self, other):
		return other.__class__.__name__ == self._beats

	def __repr__(self):
		return f'{self.__class__.__name__}'

	def __str__(self):
		return f'{self.__class__.__name__}'

	@abstractmethod
	def victory_line(self):
		pass


class Rock(RPSObject):

	def __init__(self):
		self._beats = "Scissors"

	def victory_line(self):
		return 'Rock sMaSh3z poor little Scissors'


class Paper(RPSObject):

	def __init__(self):
		self._beats = "Rock"

	def victory_line(self):
		return 'LITES OOT 4 Rock! Paper is VICTORIOUS'


class Scissors(RPSObject):

	def __init__(self):
		self._beats = "Paper"

	def victory_line(self):
		return '*Paper lets out blood curdling screams* Snippy-snip, bitches.'


def RPSFactory():
	r = randint(0, 2)
	RPS_LIST = [Rock, Paper, Scissors]
	return RPS_LIST[r]()