# Лабораторная работа 6. Двумерные массивы
# Цейгалов А.В., группа 243-321
# Номера строк и столбцов в заданиях считаются с 1, в Python индексы с 0.


def read_matrix():
    m = int(input("Количество строк M = "))
    print("Введите", m, "строк, элементы через пробел:")
    a = []
    for i in range(m):
        row = [int(x) for x in input().split()]
        a.append(row)
    return a


def print_matrix(a):
    for row in a:
        print(" ".join(str(x).rjust(4) for x in row))


def task1():
    print("\n1. Вывод квадратной матрицы по спирали против часовой стрелки")
    a = read_matrix()
    m = len(a)
    res = []
    top = 0
    bottom = m - 1
    left = 0
    right = m - 1
    while top <= bottom:
        if top == bottom:
            res.append(a[top][left])  # центральный элемент
            break
        for i in range(top, bottom + 1):  # первый столбец вниз
            res.append(a[i][left])
        for j in range(left + 1, right + 1):  # последняя строка вправо
            res.append(a[bottom][j])
        for i in range(bottom - 1, top - 1, -1):  # последний столбец вверх
            res.append(a[i][right])
        for j in range(right - 1, left, -1):  # первая строка влево
            res.append(a[top][j])
        top += 1
        bottom -= 1
        left += 1
        right -= 1
    print(" ".join(str(x) for x in res))


def task2():
    print("\n2. Сумма и произведение элементов K-й строки")
    a = read_matrix()
    k = int(input("K = "))
    s = 0
    p = 1
    for x in a[k - 1]:
        s += x
        p *= x
    print("Сумма =", s)
    print("Произведение =", p)


def task3():
    print("\n3. Столбец с наименьшим произведением элементов")
    a = read_matrix()
    m = len(a)
    n = len(a[0])
    best = 0
    min_p = None
    for j in range(n):
        p = 1
        for i in range(m):
            p *= a[i][j]
        if min_p is None or p < min_p:
            min_p = p
            best = j
    print("Номер столбца:", best + 1)
    print("Произведение =", min_p)


def task4():
    print("\n4. Количество элементов больше среднего в каждом столбце")
    a = read_matrix()
    m = len(a)
    n = len(a[0])
    for j in range(n):
        s = 0
        for i in range(m):
            s += a[i][j]
        avg = s / m
        cnt = 0
        for i in range(m):
            if a[i][j] > avg:
                cnt += 1
        print("Столбец", j + 1, ":", cnt)


def task5():
    print("\n5. Первый столбец, содержащий только нечетные числа")
    a = read_matrix()
    m = len(a)
    n = len(a[0])
    res = 0
    for j in range(n):
        odd = True
        for i in range(m):
            if a[i][j] % 2 == 0:
                odd = False
                break
        if odd:
            res = j + 1
            break
    print(res)


def task6():
    print("\n6. Поменять местами минимальный и максимальный элемент в каждой строке")
    a = read_matrix()
    for row in a:
        i_min = row.index(min(row))
        i_max = row.index(max(row))
        row[i_min], row[i_max] = row[i_max], row[i_min]
    print_matrix(a)


def task7():
    print("\n7. Поменять местами столбцы с минимальным и максимальным элементом")
    a = read_matrix()
    m = len(a)
    n = len(a[0])
    j_min = 0
    j_max = 0
    mn = a[0][0]
    mx = a[0][0]
    for i in range(m):
        for j in range(n):
            if a[i][j] < mn:
                mn = a[i][j]
                j_min = j
            if a[i][j] > mx:
                mx = a[i][j]
                j_max = j
    for i in range(m):
        a[i][j_min], a[i][j_max] = a[i][j_max], a[i][j_min]
    print_matrix(a)


def task8():
    print("\n8. Поменять местами левую верхнюю и правую нижнюю четверти")
    a = read_matrix()
    m = len(a)
    n = len(a[0])
    hm = m // 2
    hn = n // 2
    for i in range(hm):
        for j in range(hn):
            a[i][j], a[i + hm][j + hn] = a[i + hm][j + hn], a[i][j]
    print_matrix(a)


def task9():
    print("\n9. Упорядочить строки по возрастанию первых элементов")
    a = read_matrix()
    m = len(a)
    # сортировка выбором по первому элементу строки
    for i in range(m - 1):
        k = i
        for j in range(i + 1, m):
            if a[j][0] < a[k][0]:
                k = j
        a[i], a[k] = a[k], a[i]
    print_matrix(a)


def task10():
    print("\n10. Суммы диагоналей, параллельных главной")
    a = read_matrix()
    m = len(a)
    # d = j - i, начинаем с левого нижнего угла (одноэлементная диагональ)
    for d in range(-(m - 1), m):
        s = 0
        for i in range(m):
            j = i + d
            if 0 <= j < m:
                s += a[i][j]
        print("Диагональ", d + m, ":", s)


tasks = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10]

while True:
    n = input("\nНомер задачи (1-10, 0 - выход): ")
    if n == "0":
        break
    if n.isdigit() and 1 <= int(n) <= 10:
        tasks[int(n) - 1]()
    else:
        print("Нет такой задачи")
