# Лабораторная работа 5. Одномерные массивы
# Цейгалов А.В., группа 243-321
# Номера элементов в заданиях считаются с 1, в Python индексы с 0.


def read_array():
    return [float(x) for x in input("Элементы массива через пробел: ").split()]


def read_int_array():
    return [int(x) for x in input("Элементы массива через пробел: ").split()]


def task1():
    print("\n1. Массив из N первых положительных нечетных чисел")
    n = int(input("N = "))
    a = []
    for i in range(n):
        a.append(2 * i + 1)
    print(a)


def task2():
    print("\n2. Первые N членов геометрической прогрессии")
    n = int(input("N = "))
    first = float(input("A = "))
    d = float(input("D = "))
    a = [first]
    for i in range(1, n):
        a.append(a[i - 1] * d)
    print(a)


def task3():
    print("\n3. Каждый следующий элемент равен сумме всех предыдущих")
    n = int(input("N = "))
    x = int(input("A = "))
    y = int(input("B = "))
    a = [x, y]
    s = x + y
    for i in range(2, n):
        a.append(s)
        s += a[i]
    print(a)


def task4():
    print("\n4. Вывод A1, AN, A2, AN-1, ...")
    a = read_array()
    n = len(a)
    res = []
    i = 0
    j = n - 1
    while i <= j:
        res.append(a[i])
        if i != j:
            res.append(a[j])
        i += 1
        j -= 1
    print(res)


def task5():
    print("\n5. Сначала нечетные номера по возрастанию, потом четные по убыванию")
    a = read_array()
    n = len(a)
    res = []
    for i in range(0, n, 2):  # номера 1, 3, 5, ...
        res.append(a[i])
    last = n - 1 if n % 2 == 0 else n - 2
    for i in range(last, 0, -2):  # номера ..., 4, 2
        res.append(a[i])
    print(res)


def task6():
    print("\n6. Среднее арифметическое элементов с номерами от K до L")
    a = read_array()
    k = int(input("K = "))
    l = int(input("L = "))
    s = 0
    for i in range(k - 1, l):
        s += a[i]
    print("Среднее =", s / (l - k + 1))


def task7():
    print("\n7. Проверка на арифметическую прогрессию")
    a = read_int_array()
    d = a[1] - a[0]
    ok = True
    for i in range(2, len(a)):
        if a[i] - a[i - 1] != d:
            ok = False
            break
    if ok:
        print("Разность прогрессии:", d)
    else:
        print(0)


def task8():
    print("\n8. Минимальный элемент среди элементов с четными номерами")
    a = read_array()
    m = a[1]
    for i in range(1, len(a), 2):  # номера 2, 4, 6, ...
        if a[i] < m:
            m = a[i]
    print("Минимум =", m)


def task9():
    print("\n9. Номер последнего локального максимума")
    a = read_array()
    n = len(a)
    num = 0
    for i in range(n):
        left = i == 0 or a[i] > a[i - 1]
        right = i == n - 1 or a[i] > a[i + 1]
        if left and right:
            num = i + 1
    if num == 0:
        print("Локальных максимумов нет")
    else:
        print("Номер:", num)


def task10():
    print("\n10. Номера двух одинаковых элементов")
    a = read_int_array()
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                print("Номера:", i + 1, j + 1)
                return
    print("Одинаковых элементов нет")


tasks = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10]

while True:
    n = input("\nНомер задачи (1-10, 0 - выход): ")
    if n == "0":
        break
    if n.isdigit() and 1 <= int(n) <= 10:
        tasks[int(n) - 1]()
    else:
        print("Нет такой задачи")
