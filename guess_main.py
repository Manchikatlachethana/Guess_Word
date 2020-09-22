import time
from GuessLogic import GuessLogic

class Game():
	def game(self):
		name=input('what is your name? ')
		time.sleep(1)
		print("Hello,",name,"Time to play!")
		time.sleep(1)
		print("Let the game begin..")
		time.sleep(1)
		print("Good Luck !", name)
		time.sleep(1)
		print("start guessing....!")
		logic = GuessLogic()
		logic.checkLogic(name)
ga = Game()
ga.game()
