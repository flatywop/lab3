def zad1():
 n = int(input("Введите количество слов: "))
 words = []
 for i in range(n):
    word = input("Введите слово: ")
    words.append(word)
 result = " ".join(words)
 print("Результат:", result)

def zad2():
 words = []
 while True:
    word = input("Введите слово или 'stop' для завершения: ")
    if word == "stop":
        break
    words.append(word)
 result = " ".join(words)
 print("Результат:", result)


def zad3():
 word = input("Введите слово: ")
 if "ф" in word.lower():
    print("Ого! Это редкое слово!")
 else:
    print("Эх, это не очень редкое слово...")

def zad4():
 import random

 errors = 0
 correct_answers = 0

 while errors < 3:
    a, b = random.randint(1, 10), random.randint(1, 10)
    expression = f"{a} + {b} = "
    user_answer = input(expression)
    correct_answer = str(a + b)
    if user_answer == correct_answer:
        print("Правильно!")
        correct_answers += 1
    else:
        print("Ответ неверный")
        errors += 1

 print(f"Игра окончена. Правильных ответов: {correct_answers}")

