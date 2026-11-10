# Лабораторная работа 1. Линейные алгоритмы
# Цейгалов А.В., группа 243-321

import math


def task1():
    print("\n1. Площадь и периметр прямоугольника")
    a = float(input("a = "))
    b = float(input("b = "))
    s = a * b
    p = 2 * (a + b)
    print("S =", s)
    print("P =", p)


def task2():
    print("\n2. Длина окружности")
    d = float(input("d = "))
    pi = 3.14
    l = pi * d
    print("L =", round(l, 2))


def task3():
    print("\n3. Среднее арифметическое двух чисел")
    a = float(input("a = "))
    b = float(input("b = "))
    print("Среднее =", (a + b) / 2)


def task4():
    print("\n4. Сумма, разность, произведение и частное квадратов")
    a = float(input("a = "))
    b = float(input("b = "))
    a2 = a ** 2
    b2 = b ** 2
    print("Сумма =", a2 + b2)
    print("Разность =", a2 - b2)
    print("Произведение =", a2 * b2)
    print("Частное =", a2 / b2)


def task5():
    print("\n5. Сумма, разность, произведение и частное модулей")
    a = float(input("a = "))
    b = float(input("b = "))
    a1 = abs(a)
    b1 = abs(b)
    print("Сумма =", a1 + b1)
    print("Разность =", a1 - b1)
    print("Произведение =", a1 * b1)
    print("Частное =", a1 / b1)


def task6():
    print("\n6. Расстояние между двумя точками")
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    r = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("Расстояние =", r)


def task7():
    print("\n7. Длины отрезков AC и BC и их сумма")
    a = float(input("A = "))
    b = float(input("B = "))
    c = float(input("C = "))
    ac = abs(c - a)
    bc = abs(c - b)
    print("AC =", ac)
    print("BC =", bc)
    print("AC + BC =", ac + bc)


def task8():
    print("\n8. Произведение длин отрезков AC и BC (C между A и B)")
    a = float(input("A = "))
    b = float(input("B = "))
    c = float(input("C = "))
    ac = abs(c - a)
    bc = abs(c - b)
    print("AC * BC =", ac * bc)


def task9():
    print("\n9. Периметр и площадь прямоугольника по двум противоположным вершинам")
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    a = abs(x2 - x1)
    b = abs(y2 - y1)
    print("P =", 2 * (a + b))
    print("S =", a * b)


def task10():
    print("\n10. Периметр и площадь треугольника по координатам вершин")
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    x3 = float(input("x3 = "))
    y3 = float(input("y3 = "))
    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    p = a + b + c
    # площадь по формуле Герона
    pp = p / 2
    s = math.sqrt(pp * (pp - a) * (pp - b) * (pp - c))
    print("P =", p)
    print("S =", s)


def task11():
    print("\n11. y = 3x^6 - 6x^2 - 7")
    x = float(input("x = "))
    x2 = x * x
    y = 3 * x2 * x2 * x2 - 6 * x2 - 7
    print("y =", y)


def task12():
    print("\n12. y = 4(x-3)^6 - 7(x-3)^3 + 2")
    x = float(input("x = "))
    t = x - 3
    t3 = t * t * t
    y = 4 * t3 * t3 - 7 * t3 + 2
    print("y =", y)


tasks = [task1, task2, task3, task4, task5, task6,
         task7, task8, task9, task10, task11, task12]

while True:
    n = input("\nНомер задачи (1-12, 0 - выход): ")
    if n == "0":
        break
    if n.isdigit() and 1 <= int(n) <= 12:
        tasks[int(n) - 1]()
    else:
        print("Нет такой задачи")
