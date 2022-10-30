import random

def play():
      user = input("Whats your choice? \n'r' for rock, 'p' for paper, 's' for scissors:" " ")
      computer = random.choice(['r','p','s']) 
      if user == computer:
            return 'It\' a tie! '
      if is_win(user,computer):
            return 'You Win!'

      return 'You Lose!'
 
def is_win(player,opponent):
      if(player == 'r' and opponent == 'p') or (player == 'p' and opponent == 's') or (player == 's' and opponent == 'r'):
            return True

print(play())