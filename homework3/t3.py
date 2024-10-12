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

# Фильтруем все числа, которые не делятся на 2
odd_numbers = [x for x in numbers if x % 2 != 0]
print("Нечетные элементы списка:", odd_numbers)
