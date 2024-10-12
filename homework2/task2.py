while True:
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        if a > b:
            print("Ошибка: a должно быть меньше или равно b.")
            continue
        break
    except ValueError:
        print("Ошибка: Введите корректные числа.")

# Находим квадраты только целых чисел в диапазоне от a до b (включительно)
squares = [x**2 for x in range(int(a), int(b) + 1) if x == int(x)]
print("Квадраты целых чисел:", squares)
