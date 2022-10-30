import random
from words import words #importing from word.py
import string #for calling alphabets


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word: #to remove the space and - in words
        word = random.choice(words)

    return word.upper()

def hangman():
    word=get_valid_word(words)
    word_letters = set(word) #set containing letters in the the answer 
    alphabet = set(string.ascii_uppercase) #calling forth alphabets as options
    used_letters = set() # empty set for user to use words
    lives = 6
    
    while len(word_letters)>0:
        print('You have used these letters: ',''.join(used_letters))
        word_list= [letter if  letter in used_letters else '-' for letter in word]
        print('Current word: ',''.join(word_list))
        user_letter = input('Guess the letter: ').upper()

        if user_letter in alphabet - used_letters:
           used_letters.add(user_letter)
        
           if user_letter in word_letters:
                  word_letters.remove(user_letter)

           else:
                  lives = lives - 1
                  print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
          print('You have already used that character.Please try again.')

        else:
           print('Invalid character!')
    if lives == 0:
      print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')
print(hangman())