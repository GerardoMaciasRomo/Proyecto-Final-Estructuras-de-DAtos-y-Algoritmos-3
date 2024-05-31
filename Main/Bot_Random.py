# Pichon Aqui va el bot random que vamos a usar para probarlo
import random
import game

class BotRandom:
    def make_move(self, board, player):
        # Elige un movimiento al azar, pero asegúrate de que sea válido
        valid_moves = game.valid_moves(board)
        return random.choice(valid_moves)
#Aqui esta padrino, el codigo mas complicado que eh echo 
