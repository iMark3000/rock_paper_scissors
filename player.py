import json
from os import getenv

class Player:

	def __init__(self, name, wins, played, **kwargs):
		self._name = name
		self._wins = wins
		self._played = played
		self._rps = None

	@property
	def name(self):
		return self._name

	@property
	def rps(self):
		return self._rps

	@rps.setter
	def rps(self, rps):
		self._rps = rps
	
	def increase_wins(self):
		self._wins += 1

	def increase_played(self):
		self._played += 1

	def __str__(self):
		return f'{self._name} ({self._wins} Wins/{self._played - self._wins} Losses)'

	def to_dict(self):
		return {
		"name": self._name,
		"wins": self._wins,
		"played": self._played
		}


def get_players():
	players = list()
	player_file = getenv("PLAYER_FILE")
	with open(player_file, 'r') as pf:
		data = json.load(pf)
		for player in data:
			players.append(Player(**player))
	return players


def save_players(player_list):
	saved_list = [player.to_dict() for player in player_list]
	player_file = getenv("PLAYER_FILE")
	with open(player_file, "w") as pf:
		json.dump(saved_list, pf, indent=2)
