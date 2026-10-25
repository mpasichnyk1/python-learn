"""Урок 2, крок 2. Функції: даємо ім'я блоку корисних команд."""

# def визначає функцію. Код функції виконується лише під час виклику.
def greet(name):
    print(f"Привіт, {name}! Приємно тебе бачити.")


# Два параметри функції: price і count.
# return ПОВЕРТАЄ результат, який можна зберегти або використати далі.
def calculate_total(price, count):
    total = price * count
    return total


# Функція може ухвалювати рішення і повертати текст.
def describe_temperature(temperature):
    if temperature < 0:
        return "морозно"
    elif temperature < 20:
        return "прохолодно"
    return "тепло"  # Сюди дійдемо, якщо попередні умови не спрацювали.


# Поки що визначали функції. А тепер ВИКЛИКАЄМО їх.
greet("Оля")
greet("Максим")

result = calculate_total(12.5, 3)
print(f"Вартість трьох квитків: {result:.2f} грн")

weather = describe_temperature(24)
print(f"Сьогодні {weather}.")

# СПРОБУЙ:
# 1. Виклич greet() зі своїм ім'ям.
# 2. Заміни 12.5 і 3 на інші числа та перевір результат.
# 3. Створи свою функцію square(number), яка повертає квадрат числа.
#    Перевір: square(4) має дати 16.
