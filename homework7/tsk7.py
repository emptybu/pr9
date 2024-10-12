while True:
    try:
        numbers = list(map(float, input("Введите список чисел через пробел: ").split()))
        break
    except ValueError:
        print("Ошибка: Введите только числа.")

# Выполняем циклический сдвиг вправо
numbers = [numbers[-1]] + numbers[:-1]
print("Список после циклического сдвига вправо:", numbers)
