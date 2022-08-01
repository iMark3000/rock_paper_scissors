
import json
import logging
from random import shuffle

from player import get_players, save_players
from RPSClasses import RPSFactory


logging.basicConfig(filename='output.log', encoding='utf-8', level=logging.INFO)


def select_players(player_list):
	shuffle(player_list)
	return player_list[0], player_list[1]

def get_rps(player):
	player.rps = RPSFactory()

def run_round(p1, p2):

	while True:
		get_rps(p1)
		get_rps(p2)
		if p1.rps == p2.rps:
			logging.info(f'{p1.rps} equals {p2.rps}')
			logging.info("Again!!!")
			continue
		elif p1.rps > p2.rps:
			logging.info(p1.rps.victory_line())
			logging.info(f"{p1.name} wins!!!\n")
			return p1
		else:
			logging.info(p2.rps.victory_line())
			logging.info(f"{p2.name} wins!!!\n")
			return p2

def log_result():
	pass

def main():
	logging.info("INITIALIZING BATTLE SEQUENCE.....")

	logging.info("Loading players.....")
	players = get_players()

	logging.info("Picking contestants.....\n")
	player1, player2 = select_players(players)

	logging.info(f"{player1.name} vs. {player2.name}")
	player1.increase_played()
	player2.increase_played()

	winner = run_round(player1, player2)
	winner.increase_wins()

	save_players(players)

	

if __name__ == "__main__":
	main()
