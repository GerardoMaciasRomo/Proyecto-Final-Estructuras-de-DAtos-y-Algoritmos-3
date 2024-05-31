import pygame
import Juego
import Bot_Random
import Heuristica
import Bot
import random


# Configuración de Pygame
def initialize_pygame():
    print("Inicializando Pygame...")
    pygame.init()
    SIZE = 5
    CELL_SIZE = 100
    WINDOW_SIZE = SIZE * CELL_SIZE
    LINE_COLOR = (0, 0, 0)
    PLAYER_COLORS = {
        1: (255, 0, 0),
        2: (0, 0, 255),
    }  # Asegura que el jugador 2 tenga un color visible

    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Quixo")
    print("Pygame inicializado correctamente.")
    return window, SIZE, CELL_SIZE, LINE_COLOR, PLAYER_COLORS


def draw_board(window, board, SIZE, CELL_SIZE, LINE_COLOR, PLAYER_COLORS):
    window.fill((255, 255, 255))
    for x in range(SIZE):
        for y in range(SIZE):
            color = PLAYER_COLORS.get(board[x][y], (200, 200, 200))
            pygame.draw.rect(
                window, color, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )
            pygame.draw.rect(
                window,
                LINE_COLOR,
                (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                1,
            )
    pygame.display.update()


def play_game(
    window, bot1, bot2, game_number, SIZE, CELL_SIZE, LINE_COLOR, PLAYER_COLORS
):
    board = game.initialize_board()
    current_player = 1
    print(
        f"Partida {game_number}: {bot1.__class__.__name__} vs {bot2.__class__.__name__}"
    )
    while not game.is_game_over(board):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Pygame cerrado prematuramente.")
                pygame.quit()
                return None
        draw_board(window, board, SIZE, CELL_SIZE, LINE_COLOR, PLAYER_COLORS)
        pygame.time.delay(500)
        if current_player == 1:
            move = bot1.make_move(board, current_player)
        else:
            move = bot2.make_move(board, current_player)
        if not game.is_valid_move(board, move, current_player):
            return (
                3 - current_player
            )  # El jugador actual pierde por hacer un movimiento ilegal
        game.apply_move(board, move, current_player)
        current_player = 3 - current_player  # Alterna entre 1 y 2
    draw_board(window, board, SIZE, CELL_SIZE, LINE_COLOR, PLAYER_COLORS)
    winner = game.get_winner(board)
    if winner is not None:
        print(f"¡El jugador {winner} ha ganado!")
    else:
        print("El juego terminó en empate.")
    return winner


def choose_bots():
    bots = {
        "1": bot_random.BotRandom,
        "2": bot_heuristic.BotHeuristic,
        "3": lambda: bot.Bot(1),
    }
    print("Selecciona el bot para el Jugador 1:")
    print("1: BotRandom")
    print("2: BotHeuristic")
    print("3: BotMinimax")
    choice1 = input("Opción: ")

    print("Selecciona el bot para el Jugador 2:")
    print("1: BotRandom")
    print("2: BotHeuristic")
    print("3: BotMinimax")
    choice2 = input("Opción: ")

    return bots[choice1](), bots[choice2]()


def choose_mode():
    print("Selecciona el modo de emparejamiento:")
    print("1: Seleccionar jugadores manualmente")
    print("2: Emparejamiento aleatorio")
    mode = input("Opción: ")
    return mode


def calculate_score(wins, draws):
    return wins * 1.0 + draws * 0.5


def main():
    window, SIZE, CELL_SIZE, LINE_COLOR, PLAYER_COLORS = initialize_pygame()
    mode = choose_mode()

    if mode == "1":
        bot1, bot2 = choose_bots()
    elif mode == "2":
        bots = [bot_random.BotRandom, bot_heuristic.BotHeuristic, lambda: bot.Bot(1)]
        bot1, bot2 = random.choice(bots)(), random.choice(bots)()

    results = [0, 0, 0]  # [Wins, Draws, Losses]

    for i in range(20):
        result = play_game(
            window, bot1, bot2, i + 1, SIZE, CELL_SIZE, LINE_COLOR, PLAYER_COLORS
        )
        if result == 1:
            results[0] += 1
        elif result == 2:
            results[2] += 1
        else:
            results[1] += 1

    score = calculate_score(results[0], results[1])

    print("\nResumen de resultados:")
    print(f"  Victorias del Jugador 1 ({bot1.__class__.__name__}): {results[0]}")
    print(f"  Empates: {results[1]}")
    print(f"  Victorias del Jugador 2 ({bot2.__class__.__name__}): {results[2]}")
    print(f"  Puntaje total: {score} / 20")

    if 18 <= score <= 20:
        grade = 10
    elif 16 <= score <= 17:
        grade = 9
    elif 14 <= score <= 15:
        grade = 8
    elif 12 <= score <= 13:
        grade = 7
    elif 10 <= score <= 11:
        grade = 6
    elif 6 <= score <= 9:
        grade = 5
    else:
        grade = 0

    print(f"Calificación basada en el puntaje: {grade}")

    print("Cerrando Pygame al final del programa.")
    pygame.quit()


if __name__ == "__main__":
    main()
