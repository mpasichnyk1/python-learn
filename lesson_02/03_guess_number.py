"""Урок 2, крок 3. Перша гра: вгадай число за 5 спроб."""

# random — частина стандартної бібліотеки Python.
import random

# Великі літери в іменах — домовленість для значень, які не змінюємо.
MIN_NUMBER = 1
MAX_NUMBER = 20
MAX_ATTEMPTS = 5

secret = random.randint(MIN_NUMBER, MAX_NUMBER)
won = False

print("=== ВГАДАЙ ЧИСЛО ===")
print(f"Я загадав число від {MIN_NUMBER} до {MAX_NUMBER}.")
print(f"У тебе є {MAX_ATTEMPTS} спроб.")

for attempt in range(1, MAX_ATTEMPTS + 1):
    print(f"\nСпроба {attempt}/{MAX_ATTEMPTS}")
    answer = input("Твій варіант: ").strip()

    # isdigit() перевіряє, чи рядок складається тільки із цифр.
    # Так ми не отримуємо помилку під час int("привіт").
    if not answer.isdigit():
        print("Введи ціле додатне число, наприклад 7.")
        continue  # Ця спроба витрачена, переходимо до наступної.

    guess = int(answer)

    if guess < MIN_NUMBER or guess > MAX_NUMBER:
        print("Твоє число за межами діапазону!")
        continue

    if guess == secret:
        won = True
        print(f"Перемога! Ти вгадав(ла) з {attempt}-ї спроби!")
        break  # Вихід із циклу: далі вгадувати не потрібно.
    elif guess < secret:
        print("Замало! Спробуй більше число.")
    else:
        print("Забагато! Спробуй менше число.")

if not won:
    print(f"\nСпроби закінчилися! Правильне число: {secret}.")

print("Дякую за гру!")

# СПРОБУЙ:
# 1. Зміни MAX_NUMBER на 50 і MAX_ATTEMPTS на 7.
# 2. Що станеться, якщо ввести слово замість числа?
# 3. СКЛАДНІШЕ: зроби так, щоб некоректне введення НЕ витрачало спробу.
#    Підказка: потрібно змінити спосіб підрахунку спроб.
