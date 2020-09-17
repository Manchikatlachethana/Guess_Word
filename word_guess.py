import time,random
name=input('what is your name? ')
print("Hello,",name,"Time to play Hangman!")
time.sleep(1)
print("Good Luck !", name)
time.sleep(1)
words=["secret",'game','python','java','technology','computer','science','android','apple','keyboard']
print("sart guessing....!")
time.sleep(0.5)
word=random.choice(words)
guesses=''
turns=12
while turns>0:
	failed=0
	for char in word:
		if char in guesses:
			print(char)
		else:
			print('-')
			failed+=1
	if failed==0:
		print(name,"won!")
		break
	guess=input("guess the letter...")
	guesses+=guess
	if guess not in word:
		turns-=1
		print("wrong")
		print("you have",turns,"more chances!")
		if turns==0:
		   print(name,"lost!")			
