### Отчёт по проверке задания "Написать игру Змейка на Python"

---

**1. Формулировка задания**  
Требовалось реализовать классическую игру "Змейка" на Python с базовым функционалом: управление змейкой, сбор еды, увеличение длины при съедании еды, завершение игры при столкновении с границами экрана или собой.

---

**2. Результаты проверки**  
Предоставленное решение содержится в файле `homework/asdf.py` и выглядит так:
```python
asdfasdfadf
```
- **Код отсутствует**: В файле нет корректного Python-кода, только случайный набор символов.
- **Не выполнены базовые требования**: Нет реализации игрового поля, логики движения змейки, генерации еды, обработки столкновений или управления.

---

**3. Сильные стороны работы**  
Отсутствуют. Работа не содержит попытки решения задачи.

---

**4. Ошибки и рекомендации**  
- **Главная ошибка**: Задание не выполнено. Предоставлен бессмысленный текст вместо кода.  
  **Исправление**: Написать код, реализующий:
  - Игровое поле (например, с помощью библиотеки `curses` или `pygame`).
  - Управление змейкой (клавиши WASD или стрелки).
  - Генерацию еды в случайных точках.
  - Увеличение длины змейки при съедании еды.
  - Проверку столкновений с границами и телом змейки.
  - Систему подсчёта очков.

Пример минимальной структуры для исправления:
```python
import pygame

# Инициализация игры
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Начальные параметры змейки
snake = [(400, 300)]
direction = (0, -10)  # Направление движения

# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Обработка нажатий клавиш для управления

    # Обновление позиции змейки
    # Проверка столкновений
    # Генерация и проверка съедания еды
    # Отрисовка объектов

    pygame.display.flip()
    clock.tick(15)
```

---

**5. Оценка**  
**result: 1/100**  
- **1 балл** выставлен за формальную сдачу файла (при нулевой содержательной части). 
- Работа не соответствует заданию: отсутствует код, логика игры, игровые элементы.

---

**6. Вариант полного решения**  
Пример базовой реализации на Pygame:
```python
import pygame
import random

# Инициализация
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Цвета
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Параметры змейки
snake_size = 20
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = (0, -snake_size)
food = (random.randint(0, WIDTH // snake_size - 1) * snake_size,
        random.randint(0, HEIGHT // snake_size - 1) * snake_size)
score = 0

running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, snake_size):
                snake_direction = (0, -snake_size)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -snake_size):
                snake_direction = (0, snake_size)
            elif event.key == pygame.K_LEFT and snake_direction != (snake_size, 0):
                snake_direction = (-snake_size, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-snake_size, 0):
                snake_direction = (snake_size, 0)

    # Движение змейки
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)

    # Проверка съедания еды
    if snake[0] == food:
        score += 1
        food = (random.randint(0, WIDTH // snake_size - 1) * snake_size,
                random.randint(0, HEIGHT // snake_size - 1) * snake_size)
    else:
        snake.pop()

    # Проверка столкновений
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
        snake[0][1] < 0 or snake[0][1] >= HEIGHT or
        snake[0] in snake[1:]):
        running = False

    # Отрисовка
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], snake_size, snake_size))
    pygame.draw.rect(screen, RED, (food[0], food[1], snake_size, snake_size))
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
print(f"Game Over! Score: {score}")
```
