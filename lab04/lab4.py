# Лабораторная работа 4. Рекурсивные алгоритмы
# Цейгалов А.В., группа 243-321


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fib(n):
    # fib(1) = 1, fib(2) = 1
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    return x * power(x, n - 1)


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def binary_search(arr, x, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    if arr[mid] < x:
        return binary_search(arr, x, mid + 1, right)
    return binary_search(arr, x, left, mid - 1)


def reverse_words(words):
    if len(words) <= 1:
        return words
    return reverse_words(words[1:]) + [words[0]]


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_sum(n, start):
    # пробуем взять простое p (от большего к меньшему) и разложить остаток
    if n == 0:
        return []
    for p in range(min(n, start), 1, -1):
        if is_prime(p):
            rest = prime_sum(n - p, p)
            if rest is not None:
                return [p] + rest
    return None


def count_digits(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


def hanoi(n, a, b, c):
    # переносим n дисков со стержня a на стержень c через b
    if n == 0:
        return
    hanoi(n - 1, a, c, b)
    print("Диск", n, ":", a, "->", c)
    hanoi(n - 1, b, a, c)


def task1():
    print("\n1. Факториал числа")
    n = int(input("n = "))
    print(str(n) + "! =", factorial(n))


def task2():
    print("\n2. n-ое число Фибоначчи")
    n = int(input("n = "))
    print("F(" + str(n) + ") =", fib(n))


def task3():
    print("\n3. Возведение в степень")
    x = float(input("x = "))
    n = int(input("n = "))
    print("x^n =", power(x, n))


def task4():
    print("\n4. Проверка на палиндром")
    s = input("Строка: ")
    # пробелы и регистр не учитываем
    s1 = s.replace(" ", "").lower()
    if is_palindrome(s1):
        print("Палиндром")
    else:
        print("Не палиндром")


def task5():
    print("\n5. Рекурсивный бинарный поиск")
    arr = [int(x) for x in input("Отсортированный массив через пробел: ").split()]
    x = int(input("Что ищем: "))
    i = binary_search(arr, x, 0, len(arr) - 1)
    if i == -1:
        print("Элемент не найден")
    else:
        print("Элемент найден, номер", i + 1)


def task6():
    print("\n6. Обратный порядок слов")
    s = input("Строка: ")
    print(" ".join(reverse_words(s.split())))


def task7():
    print("\n7. Разложение числа на сумму простых чисел")
    n = int(input("n (>= 2): "))
    res = prime_sum(n, n)
    if res is None:
        print("Разложить нельзя")
    else:
        print(n, "=", " + ".join(str(p) for p in res))


def task8():
    print("\n8. Количество цифр в числе")
    n = int(input("n = "))
    print("Цифр:", count_digits(n))


def task9():
    print("\n9. Ханойская башня")
    n = int(input("Количество дисков: "))
    hanoi(n, "A", "B", "C")
    print("Всего ходов:", 2 ** n - 1)


tasks = [task1, task2, task3, task4, task5, task6, task7, task8, task9]

while True:
    n = input("\nНомер задачи (1-9, 0 - выход): ")
    if n == "0":
        break
    if n.isdigit() and 1 <= int(n) <= 9:
        tasks[int(n) - 1]()
    else:
        print("Нет такой задачи")
