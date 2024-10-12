numbers = []

while True:
    value = input("Введите число (или 'end' для завершения): ")
    if value == 'end':
        break
    try:
        num = float(value)
        numbers.append(num)
    except ValueError:
        print("Ошибка: Введите корректное число.")

# Подсчитываем четные и нечетные только среди целых чисел
even_count = len([x for x in numbers if x.is_integer() and int(x) % 2 == 0])
odd_count = len([x for x in numbers if x.is_integer() and int(x) % 2 != 0])

print(f"Четных чисел: {even_count}, Нечетных чисел: {odd_count}")
