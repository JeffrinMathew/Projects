import random

def guess(x):
 random_number=random.randint(1,x)
 guess=0
 while guess != random_number:
  guess=int(input(f'Guess a number between 1 and {x}: '))
  print(guess)
  if guess > random_number:
    print('Sorry,Try again. Your guess is too high (%d) '%guess)

  elif guess < random_number:
    print('Sorry,Try again. your guess is too low (%d) '%guess)
 
 print(f'Congratz! You have guessed the right number.Its {random_number}!')

guess(10)    