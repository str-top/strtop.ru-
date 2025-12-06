### Отчёт по проверке задания "Написать игру Змейка на Python"

---

#### 1. Формулировка задания
Требовалось реализовать классическую игру "Змейка" на Python с использованием библиотеки для работы с графикой (например, Pygame или curses). Основные элементы:
- Управление змейкой с клавиатуры.
- Появление еды в случайных местах.
- Увеличение длины змейки при поедании еды.
- Завершение игры при столкновении с границами экрана или самой собой.

---

#### 2. Результаты проверки
**Решение отсутствует.**  
В предоставленном файле `asdf.py` содержится только строка `asdfasd` (без какого-либо кода). Это не соответствует требованиям задания.

---

#### 3. Сильные стороны работы
Отсутствуют, так как работа не выполнена.

---

#### 4. Ошибки и способы их исправления
**Критическая ошибка:**  
- Задание не выполнено — нет кода, логики или даже попытки реализации игры.  

**Рекомендации:**  
1. Используйте библиотеку Pygame или curses для создания игрового поля и обработки ввода.  
2. Реализуйте базовые классы/функции:  
   - Змейка (хранение координат, направление движения).  
   - Генерация еды.  
   - Обработка столкновений.  
3. Добавьте игровой цикл с обновлением состояния и отрисовкой.  

---

#### 5. Оценка
**1/100**  
Обоснование:  
- Работа не содержит ни одной значимой части кода, соответствующей заданию.  
- Нет демонстрации понимания принципов разработки игр (цикл игры, обработка событий, отрисовка).  

---

#### 6. Пример решения
Минимальная реализация на Pygame:

```python
import pygame
import random

# Инициализация
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Цвета
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Змейка
snake = [(100, 100), (90, 100), (80, 100)]
direction = (10, 0)
food = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 10):
                direction = (0, -10)
            elif event.key == pygame.K_DOWN and direction != (0, -10):
                direction = (0, 10)
            elif event.key == pygame.K_LEFT and direction != (10, 0):
                direction = (-10, 0)
            elif event.key == pygame.K_RIGHT and direction != (-10, 0):
                direction = (10, 0)

    # Движение змейки
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    # Проверка на съедение еды
    if snake[0] == food:
        food = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))
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
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], 10, 10))
    pygame.draw.rect(screen, RED, (food[0], food[1], 10, 10))
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
```

**Пояснение:**  
- Змейка управляется стрелками.  
- Еда появляется случайно.  
- Игра завершается при столкновении с границами или собой.
