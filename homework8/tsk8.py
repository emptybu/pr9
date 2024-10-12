import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

user_choices = []
for row in ticket:
    while True:
        try:
            choice = float(input(f"Выберите число из строки {row}: "))
            if not choice.is_integer() or int(choice) not in row:
                print("Ошибка: Введите целое число, которое есть в строке.")
            else:
                user_choices.append(int(choice))
                break
        except ValueError:
            print("Ошибка: Введите корректное число.")

random_choices = [random.choice(row) for row in ticket]

print("Ваш выбор:", user_choices)
print("Случайный выбор:", random_choices)

matches = set(user_choices) & set(random_choices)
print(f"Совпадений: {len(matches)}, Совпавшие числа: {matches}")
