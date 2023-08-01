import pygame
import random

def play_snakegame():
    width, height = 800, 600
    cell_size = 20
    fps = 10

    purple = (128, 0, 128)
    green = (0, 255, 0)
    black = (0, 0, 0)

    pygame.init()
    window = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    class Snake:
        def __init__(self):
            self.body = [(width // 2, height // 2)]
            self.direction = (cell_size, 0)
            self.grow = False

        def move(self):
            x, y = self.body[0]
            dx, dy = self.direction
            new_head = ((x + dx) % width, (y + dy) % height)
            self.body.insert(0, new_head)

            if not self.grow:
                self.body.pop()
            else:
                self.grow = False

        def draw(self):
            for segment in self.body:
                pygame.draw.rect(window, green, (segment[0], segment[1], cell_size, cell_size))

        def check_crash(self):
            return len(self.body) != len(set(self.body))

        def handle_event(self, event):
            if event.key == pygame.K_w:
                self.direction = (0, -cell_size)
            elif event.key == pygame.K_s:
                self.direction = (0, cell_size)
            elif event.key == pygame.K_a:
                self.direction = (-cell_size, 0)
            elif event.key == pygame.K_d:
                self.direction = (cell_size, 0)

        def check_prey_crash(self, prey):
            return self.body[0] == prey.position

    class prey:
        def __init__(self):
            self.position = self.random_position()

        def random_position(self):
            x = random.randrange(0, width, cell_size)
            y = random.randrange(0, height, cell_size)
            return x, y

        def draw(self):
            pygame.draw.rect(window, purple, (self.position[0], self.position[1], cell_size, cell_size))

    snake = Snake()
    prey = prey()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                snake.handle_event(event)

        snake.move()
        if snake.check_crash():
            running = False

        if snake.check_prey_crash(prey):
            prey.position = prey.random_position()
            snake.grow = True

        window.fill(black)
        snake.draw()
        prey.draw()
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    play_snakegame()
