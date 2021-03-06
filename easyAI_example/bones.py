from easyAI import TwoPlayersGame, Human_Player, AI_Player, Negamax

class GameOfBones( TwoPlayersGame ):
    """ In turn, the players remove one, two or three bones from a
    pile of bones. The player who removes the last bone loses. """

    def __init__(self, players):
        self.players = players
        self.pile = 21 # start with 20 bones in the pile
        self.nplayer = 2 # player 1 starts

    def possible_moves(self): return ['1','2','3']
    def make_move(self,move): self.pile -= int(move) # remove bones.
    def win(self): return self.pile<=0 # opponent took the last bone ?
    def is_over(self): return self.win() # Game stops when someone wins.
    def show(self): print "%d bones left in the pile"%self.pile
    def scoring(self): return 100 if self.win() else 0 # For the AI

# Start a match (and store the history of moves when it ends)
ai = Negamax(13) # The AI will think 13 moves in advance
game = GameOfBones( [ Human_Player(), AI_Player(ai) ] )
history = game.play()

from easyAI import id_solve
r,d,m = id_solve(GameOfBones, ai_depths=range(2,20), win_score=100)
print(r,d,m)