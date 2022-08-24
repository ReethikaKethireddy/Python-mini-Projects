#rock paper scissors
import random

play = ['r','p','s']

def lets_play():
	user = input("What do you wanna choose? 's', for scissors, 'r', for rock 'r' for paper:")
	opponent = random.choice(play)
	print("Opponent choice:", opponent)

	if user == opponent:
		print("It's a tie")
	if win(user,opponent):
		print("You Won!!!")

	print("You Lost!")


def win(user,opponent):
	if (user=='r' and opponent=='s') or (user=='s' and opponent=='p') or (user=='p'and opponent=='r'):
		return True

while True:
	lets_play()  
	replay = input("Do you wanna play again? 'y' or 'n' ")  
	if replay == 'y' :
		continue
	if replay == 'n' :
	    break	
