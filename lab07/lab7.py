# Лабораторная работа 7. Сортировка пузырьком
# Цейгалов А.В., группа 243-321


def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        swapped = False
        # после каждого прохода самый большой элемент "всплывает" в конец
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        print("Проход", i + 1, ":", a)
        if not swapped:  # обменов не было, массив уже отсортирован
            break
    return a


a = [int(x) for x in input("Элементы массива через пробел: ").split()]
print("Исходный массив:", a)
bubble_sort(a)
print("Отсортированный массив:", a)
