while True:
    try:
        numbers = list(map(float, input("Введите список чисел через пробел: ").split()))
        break
    except ValueError:
        print("Ошибка: Введите только числа.")

min_idx = numbers.index(min(numbers))
max_idx = numbers.index(max(numbers))

numbers[min_idx], numbers[max_idx] = numbers[max_idx], numbers[min_idx]
print("Список после замены:", numbers)
