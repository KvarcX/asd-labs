# Лабораторная работа 5. Одномерные массивы
# Цейгалов А.В., группа 243-321
# Номера элементов в заданиях считаются с 1, в Python индексы с 0.


def read_array():
    return [float(x) for x in input("Элементы массива через пробел: ").split()]


def read_int_array():
    return [int(x) for x in input("Элементы массива через пробел: ").split()]


def task1():
    # 2 * i + 1 при i от нуля даёт 1, 3, 5 и так далее.
    print("\n1. Массив из N первых положительных нечетных чисел")
    n = int(input("N = "))
    a = []
    for i in range(n):
        a.append(2 * i + 1)
    print(a)


def task2():
    # в геометрической прогрессии каждый следующий элемент получаем умножением предыдущего на D.
    print("\n2. Первые N членов геометрической прогрессии")
    n = int(input("N = "))
    first = float(input("A = "))
    d = float(input("D = "))
    a = [first]
    for i in range(1, n):
        a.append(a[i - 1] * d)
    print(a)


def task3():
    # держим сумму уже добавленных элементов: она и будет следующим элементом.
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
    # берём по очереди с левого и правого края и идём к середине. Если встретились, берём элемент один раз.
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
    # сначала берём позиции 1, 3, 5 слева направо, потом позиции 2, 4, 6 в обратном порядке.
    print("\n5. Сначала нечетные номера по возрастанию, потом четные по убыванию")
    a = read_array()
    n = len(a)
    res = []
    for i in range(0, n, 2):  # номера 1, 3, 5, ...
        res.append(a[i])
    # если длина нечётная, последний элемент стоит на нечётной позиции, поэтому начинаем с предпоследнего.
    last = n - 1 if n % 2 == 0 else n - 2
    for i in range(last, 0, -2):  # номера ..., 4, 2
        res.append(a[i])
    print(res)


def task6():
    # от K до L включительно всего L - K + 1 элементов, на это число делим сумму.
    print("\n6. Среднее арифметическое элементов с номерами от K до L")
    a = read_array()
    k = int(input("K = "))
    l = int(input("L = "))
    s = 0
    for i in range(k - 1, l):
        s += a[i]
    print("Среднее =", s / (l - k + 1))


def task7():
    # в арифметической прогрессии разница между соседями одинаковая. Берём разницу первых двух за образец.
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
    # чётные здесь номера позиций, а не сами числа. Например, в [8, 3, 1, 5] смотрим только на 3 и 5.
    print("\n8. Минимальный элемент среди элементов с четными номерами")
    a = read_array()
    m = a[1]
    for i in range(1, len(a), 2):  # индексы 1, 3, 5 - это позиции 2, 4, 6
        if a[i] < m:
            m = a[i]
    print("Минимум =", m)


def task9():
    # локальный максимум больше своих соседей, а не всего массива. В [1, 7, 2, 5, 1] последний максимум - 5 на позиции 4.
    print("\n9. Номер последнего локального максимума")
    a = read_array()
    n = len(a)
    num = 0
    for i in range(n):
        # сравниваем с предыдущим и со следующим, то есть с соседями.
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
        # сравниваем текущий элемент со всеми, что стоят справа.
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
