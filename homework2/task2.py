while True:
    try:
        a = int(input("Введите число a: "))
        b = int(input("Введите число b: "))
        if a > b:
            print("Ошибка: a должно быть меньше или равно b.")
            continue
        break
    except ValueError:
        print("Ошибка: Введите корректные числа.")

squares = [x**2 for x in range(a, b + 1)]
print("Квадраты чисел:", squares)
