# Лабораторная работа 8. Сортировка вставками
# Цейгалов А.В., группа 243-321


def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        # сдвигаем вправо элементы отсортированной части, которые больше key
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        print("Шаг " + str(i) + " (вставили " + str(key) + "):", a)
    return a


a = [int(x) for x in input("Элементы массива через пробел: ").split()]
print("Исходный массив:", a)
insertion_sort(a)
print("Отсортированный массив:", a)
