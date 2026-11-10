# Лабораторная работа 10. Бинарный поиск
# Цейгалов А.В., группа 243-321


def binary_search(a, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        print("left =", left, "right =", right, "mid =", mid, "a[mid] =", a[mid])
        if a[mid] == x:
            return mid
        if a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1


a = [int(x) for x in input("Элементы массива через пробел: ").split()]
a.sort()  # бинарный поиск работает только на отсортированном массиве
print("Отсортированный массив:", a)
x = int(input("Что ищем: "))
i = binary_search(a, x)
if i == -1:
    print("Элемент не найден")
else:
    print("Элемент найден, индекс", i)
