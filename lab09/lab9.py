# Лабораторная работа 9. Сортировка выбором
# Цейгалов А.В., группа 243-321


def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        # ищем минимальный элемент в неотсортированной части
        k = i
        for j in range(i + 1, n):
            if a[j] < a[k]:
                k = j
        a[i], a[k] = a[k], a[i]
        print("Шаг " + str(i + 1) + " (минимум " + str(a[i]) + "):", a)
    return a


a = [int(x) for x in input("Элементы массива через пробел: ").split()]
print("Исходный массив:", a)
selection_sort(a)
print("Отсортированный массив:", a)
