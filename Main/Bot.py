# Pichon aquí va el bot normal we
import game

class Bot:
    def __init__(self, symbol):
        # Inicializa el símbolo del bot (por ejemplo, 'X' o 'O')
        self.symbol = symbol

    def make_move(self, board, player):
        # Determina el mejor movimiento utilizando el algoritmo Minimax
        # Llama a la función minimax con una profundidad de 4 y límites iniciales alfa y beta
        _, best_move = self.minimax(board, player, 4, float('-inf'), float('inf'), True)
        return best_move

    def reset(self, symbol):
        # Reinicia el símbolo del bot
        self.symbol = symbol

    def minimax(self, board, player, depth, alpha, beta, maximizing_player):
        # Implementa el algoritmo Minimax con poda alfa-beta
        # Condición de terminación: si se alcanza la profundidad máxima o el juego ha terminado
        if depth == 0 or game.is_game_over(board):
            return self.evaluate_board(board, player), None

        # Obtiene los movimientos válidos para el estado actual del tablero
        valid_moves = game.valid_moves(board)
        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            # Itera sobre cada movimiento válido
            for move in valid_moves:
                # Aplica el movimiento para generar un nuevo tablero
                new_board = [row[:] for row in board]
                game.apply_move(new_board, move, player)
                # Llama recursivamente a minimax para el nuevo tablero
                eval, _ = self.minimax(new_board, player, depth - 1, alpha, beta, False)
                # Actualiza la evaluación máxima y el mejor movimiento
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                # Actualiza alfa y realiza la poda si es necesario
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            # Itera sobre cada movimiento válido
            for move in valid_moves:
                # Aplica el movimiento para generar un nuevo tablero
                new_board = [row[:] for row in board]
                game.apply_move(new_board, move, 3 - player)
                # Llama recursivamente a minimax para el nuevo tablero
                eval, _ = self.minimax(new_board, player, depth - 1, alpha, beta, True)
                # Actualiza la evaluación mínima y el mejor movimiento
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                # Actualiza beta y realiza la poda si es necesario
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def evaluate_board(self, board, player):
        # Evalúa el tablero para determinar el resultado del juego
        winner = game.get_winner(board)
        if winner == player:
            return 1
        elif winner == 3 - player:
            return -1
        else:
            return 0
#Ya quedo padrino se supone que ya jala 
