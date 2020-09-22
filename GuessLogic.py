import random
from Guess_Words_Lib import GuessWordsLib

class GuessLogic():
	def checkLogic(self,name):
		guessWordsLib = GuessWordsLib()
		word=random.choice(guessWordsLib.getWords())
		guesses=''
		turns=12
		while turns>0:
			failed=0
			for char in word:
				if char in guesses:
					print(char, end=' ')
				else:
					print('-',end=' ')
					failed+=1
			if failed==0:
				print("\n ",name,"won!")
				print("word is ",word)
				break
			guess=input("\nguess the letter... : ")
			guesses+=guess
			if guess not in word:
				turns-=1
				print("wrong")
				print("you have",turns,"more chances!")
				if turns==0:
				   print(name,"lost!")
				   print("word is : ",word)
				   print('Be happy that you learnt new word.. :)')
