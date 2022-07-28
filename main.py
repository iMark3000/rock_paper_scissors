import logging
from random import randint


logging.basicConfig(filename='output.log', encoding='utf-8', level=logging.INFO)


def main():
	r = randint(1, 20)
	logging.info(f"Random number is {r}")
	if r > 10:
		print("Big Number")
	else:
		print("Small potatoes")
		logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

if __name__ == "__main__":
	main()
