# Вывод таблицы умножения 10×10
for row in range(1, 11):
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")  # Форматирование для выравнивания
    print()  # Переход на новую строку после каждой строки таблицы
