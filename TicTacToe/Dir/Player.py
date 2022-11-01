import math
import random

class Player:
    def _init_(self,letter):
        self.letter=letter
    
    def _init_(self,game):
        pass

class RandomComputerPlayer(Player):
    def _init_(self, letter):
        super()._init_(letter)

    def get_move(self,game):
        square=random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def _init_(self, letter):
        super()._init_(letter)

    def get_move(self,game):
        valid_square=False
        val=None
        while not valid_square:
            square=input(self.letter+'\'s turn. InputMove(0-8).. Play on!')

            try:
                val=int(square)
                if val not in game.available_move():
                    raise ValueError
                valid_square=True
            except ValueError:
                print('Invalid square. Try Again.')

        return val


       