while True:
    try:
        numbers = list(map(float, input("Введите список чисел через пробел: ").split()))
        break
    except ValueError:
        print("Ошибка: Введите только числа.")

# Выводим те элементы, которые больше предыдущего
result = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]]
print("Числа больше предыдущего:", result)
