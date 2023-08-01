import pygame
import random
import sys

def play_hangman():
    WIDTH, HEIGHT = 800, 600
    FPS = 60
    WORD_LIST = ["PYTHON", "JAVA", "JAVASCRIPT", "HTML", "CSS", "RUBY", "PHP", "CPLUSPLUS"]
    FONT_NAME = "Arial"

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)  
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(FONT_NAME, 40)

    hangman_images = [pygame.image.load(f"hangman{i}.png") for i in range(7)]

    def get_random_word():
        return random.choice(WORD_LIST)

    def draw_word(word, guessed_letters):
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        text = font.render(display_word, True, BLACK)
        window.blit(text, (WIDTH // 2 - text.get_width() // 2, 400))

    def hangman():
        nonlocal window, WIDTH, HEIGHT  
        word = get_random_word()
        guessed_letters = set()
        attempts = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.unicode.isalpha():
                    letter = event.unicode.upper()
                    guessed_letters.add(letter)
                elif event.type == pygame.VIDEORESIZE:  
                    WIDTH, HEIGHT = event.w, event.h
                    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

            window.fill(WHITE)

            window.blit(hangman_images[attempts], (WIDTH // 2 - hangman_images[attempts].get_width() // 2, 100))

            draw_word(word, guessed_letters)

            if set(word) == guessed_letters:
                text = font.render("You Win!", True, BLACK)
                window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
            elif attempts == 6:
                text = font.render("You Lose!", True, BLACK)
                window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

            pygame.display.update()
            clock.tick(FPS)

            incorrect_attempts = len([letter for letter in guessed_letters if letter not in word])
            if incorrect_attempts > attempts:
                attempts = incorrect_attempts

        pygame.quit()
        sys.exit()

    hangman()

if __name__ == "__main__":
    play_hangman()
