# Лабораторная работа 3. Циклические алгоритмы
# Цейгалов А.В., группа 243-321


def task1():
    print("\n1. Стоимость 0.1, 0.2, ..., 1 кг конфет")
    price = float(input("Цена 1 кг: "))
    for i in range(1, 11):
        w = i / 10
        print(w, "кг -", round(price * w, 2))


def task2():
    print("\n2. Произведение 1.1 * 1.2 * 1.3 * ... (N сомножителей)")
    n = int(input("N = "))
    p = 1
    x = 1.1
    for i in range(n):
        p *= x
        x += 0.1
    print("Произведение =", round(p, 6))


def task3():
    print("\n3. Квадрат числа через сумму нечетных чисел")
    n = int(input("N = "))
    s = 0
    for i in range(1, n + 1):
        s += 2 * i - 1
        print("Сумма после", i, "слагаемого:", s)
    print("N^2 =", s)


def task4():
    print("\n4. Сумма 1 + A + A^2 + ... + A^N")
    a = float(input("A = "))
    n = int(input("N = "))
    s = 1
    p = 1
    for i in range(n):
        p *= a
        s += p
    print("Сумма =", s)


def task5():
    print("\n5. Значение 1 - A + A^2 - A^3 + ... ± A^N")
    a = float(input("A = "))
    n = int(input("N = "))
    s = 1
    p = 1
    for i in range(n):
        p *= -a  # знак меняется сам при умножении на -A
        s += p
    print("Значение =", s)


def task6():
    print("\n6. Числа от A до B, каждое столько раз, каково его значение")
    a = int(input("A = "))
    b = int(input("B = "))
    for i in range(a, b + 1):
        for j in range(i):
            print(i, end=" ")
        print()


def task7():
    print("\n7. Длина незанятой части отрезка A")
    a = float(input("A = "))
    b = float(input("B = "))
    while a >= b:
        a -= b
    print("Незанятая часть =", round(a, 6))


def task8():
    print("\n8. Наименьшее K, при котором 1 + 2 + ... + K >= N")
    n = int(input("N = "))
    k = 0
    s = 0
    while s < n:
        k += 1
        s += k
    print("K =", k)
    print("Сумма =", s)


def task9():
    print("\n9. Через сколько месяцев вклад превысит 1100 руб.")
    p = float(input("P (0 < P < 25): "))
    s = 1000
    k = 0
    while s <= 1100:
        s += s * p / 100
        k += 1
    print("K =", k)
    print("S =", round(s, 2))


def task10():
    print("\n10. НОД по алгоритму Евклида")
    a = int(input("A = "))
    b = int(input("B = "))
    while b != 0:
        a, b = b, a % b
    print("НОД =", a)


tasks = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10]

while True:
    n = input("\nНомер задачи (1-10, 0 - выход): ")
    if n == "0":
        break
    if n.isdigit() and 1 <= int(n) <= 10:
        tasks[int(n) - 1]()
    else:
        print("Нет такой задачи")
