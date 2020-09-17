import time,random
name=input('what is your name? ')
time.sleep(1)
print("Hello,",name,"Time to play!")
time.sleep(1)
print("Let the game begin..")
time.sleep(1)
print("Good Luck !", name)
time.sleep(1)
words=["secret",'game','python','java','technology','computer','science','android','apple','keyboard']
print("start guessing....!")
time.sleep(0.5)
word=random.choice(words)
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
