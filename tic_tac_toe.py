import pygame
import sys

def play_tic_tac_toe():
    width, height = 300, 300
    line_width = 6
    board_size = 3
    cell_size = width // board_size

    white = (255, 255, 255)
    black = (0, 0, 0)

    pygame.init()
    window = pygame.display.set_mode((width, height))

    def draw_board():
        for i in range(1, board_size):
            pygame.draw.line(window, white, (i * cell_size, 0), (i * cell_size, height), line_width)
            pygame.draw.line(window, white, (0, i * cell_size), (width, i * cell_size), line_width)

    def draw_x(row, col):
        x = col * cell_size + cell_size // 2
        y = row * cell_size + cell_size // 2
        pygame.draw.line(window, white, (x - cell_size // 4, y - cell_size // 4), (x + cell_size // 4, y + cell_size // 4), line_width)
        pygame.draw.line(window, white, (x + cell_size // 4, y - cell_size // 4), (x - cell_size // 4, y + cell_size // 4), line_width)

    def draw_o(row, col):
        x = col * cell_size + cell_size // 2
        y = row * cell_size + cell_size // 2
        pygame.draw.circle(window, white, (x, y), cell_size // 4, line_width)

    def check_win(player):
        for row in range(board_size):
            if all(board[row][col] == player for col in range(board_size)):
                return True

        for col in range(board_size):
            if all(board[row][col] == player for row in range(board_size)):
                return True

        if all(board[i][i] == player for i in range(board_size)):
            return True

        if all(board[i][board_size - 1 - i] == player for i in range(board_size)):
            return True

        return False

    board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
    current_player = 'X'
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN and not check_win('X') and not check_win('O'):
                row = event.pos[1] // cell_size
                col = event.pos[0] // cell_size
                if board[row][col] == ' ':
                    board[row][col] = current_player
                    if current_player == 'X':
                        current_player = 'O'
                    else:
                        current_player = 'X'

        window.fill(black)
        draw_board()

        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] == 'X':
                    draw_x(row, col)
                elif board[row][col] == 'O':
                    draw_o(row, col)

        if check_win('X'):
            print("Player X wins!")
        elif check_win('O'):
            print("Player O wins!")

        pygame.display.update()

    pygame.quit()
    sys.exit()

play_tic_tac_toe()
