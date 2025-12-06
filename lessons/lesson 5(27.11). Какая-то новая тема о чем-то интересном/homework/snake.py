import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (CELL_SIZE, 0)

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % WIDTH, (head_y + dy) % HEIGHT)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self):
        return len(self.body) != len(set(self.body))

class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        return (x, y)

def main():
    snake = Snake()
    food = Food()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, CELL_SIZE):
                    snake.direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -CELL_SIZE):
                    snake.direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and snake.direction != (CELL_SIZE, 0):
                    snake.direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-CELL_SIZE, 0):
                    snake.direction = (CELL_SIZE, 0)

        snake.move()

        # Проверка съедания еды
        if snake.body[0] == food.position:
            snake.grow()
            food.position = food.generate_position()
            score += 1

        # Проверка столкновения с собой
        if snake.check_collision():
            pygame.quit()
            sys.exit()

        # Отрисовка
        screen.fill(BLACK)
        for segment in snake.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, (food.position[0], food.position[1], CELL_SIZE, CELL_SIZE))
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
