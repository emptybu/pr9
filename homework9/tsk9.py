import re

while True:
    email = input("Введите email: ")

    # Проверка на корректность email с помощью регулярного выражения
    pattern = r"^[^\d][a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    matched = re.search(pattern, email)

    if matched:
        try:
            # Найдем индекс символа '@' с помощью метода .index()
            at_index = email.index("@")

            # Разделим строку на имя пользователя и домен с помощью срезов
            username = email[:at_index]
            domain = email[at_index + 1:]

            print(f"Username: {username}")
            print(f"Domain: {domain}")
            break
        except ValueError:
            print("Ошибка: Символ '@' не найден.")
    else:
        print("Ошибка: Введите корректный email, который не начинается с цифры и содержит хотя бы одну точку в домене.")
