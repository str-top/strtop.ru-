### Отчёт по проверке задания: "Написать игру Змейка на Python"

---

#### 1. Формулировка задания:
Создать игру "Змейка" на Python с базовым функционалом: управление змейкой, поедание еды, рост длины при съедании, завершение игры при столкновении с границами экрана или собственным телом.

---

#### 2. Результаты проверки:
Решение студента содержится в файле `homework/asdf.py` и выглядит так:
```python
asdf
```

**Проблемы:**
- Файл не содержит корректного кода на Python.
- Отсутствует реализация каких-либо элементов игры (графика, управление, логика).
- Предоставленный текст `asdf` не является программой и вызывает синтаксическую ошибку.

---

#### 3. Сильные стороны работы:
Отсутствуют. Работа не соответствует требованиям задания.

---

#### 4. Ошибки и способы их исправления:
1. **Основная ошибка**: решение не предоставлено.
   - **Исправление**: написать код, реализующий игру "Змейка".
2. **Отсутствие базовых элементов**:
   - Игровое поле, змейка, еда, система управления.
   - **Исправление**: использовать библиотеку (например, `pygame` или `turtle`) для создания игрового цикла и графики.

---

#### 5. Оценка:
**result: 1/100**  
Обоснование: задание не выполнено. Единственный балл выставлен за наличие файла с расширением `.py`.

---

#### 6. Вариант полного решения:
Пример минимальной реализации с использованием `pygame`:

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
direction = "RIGHT"
food = (random.randint(0, WIDTH // 10 - 1) * 10, 
        random.randint(0, HEIGHT // 10 - 1) * 10)

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Движение змейки
    head_x, head_y = snake[0]
    if direction == "UP":
        new_head = (head_x, head_y - 10)
    elif direction == "DOWN":
        new_head = (head_x, head_y + 10)
    elif direction == "LEFT":
        new_head = (head_x - 10, head_y)
    elif direction == "RIGHT":
        new_head = (head_x + 10, head_y)
    snake.insert(0, new_head)

    # Проверка на съедание еды
    if snake[0] == food:
        food = (random.randint(0, WIDTH // 10 - 1) * 10, 
                random.randint(0, HEIGHT // 10 - 1) * 10)
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
    pygame.display.update()
    clock.tick(15)

pygame.quit()
```

**Пояснение:**
- Используется библиотека `pygame` для графики и управления.
- Змейка представлена списком координат сегментов.
- Еда генерируется случайно на поле.
- Управление осуществляется стрелками клавиатуры.
- Игра завершается при столкновении с границами или собой.
