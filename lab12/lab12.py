# Лабораторная работа 12. Очередь
# Цейгалов А.В., группа 243-321


class Queue:
    # очередь: добавляем в конец, забираем из начала (FIFO)
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []


q = Queue()

while True:
    print("\nОчередь:", q.items)
    print("1 - добавить элемент")
    print("2 - взять элемент из начала")
    print("3 - посмотреть первый элемент")
    print("4 - размер очереди")
    print("5 - проверить, пуста ли очередь")
    print("6 - очистить очередь")
    print("0 - выход")
    c = input("Выбор: ")
    if c == "1":
        x = input("Элемент: ")
        q.enqueue(x)
    elif c == "2":
        x = q.dequeue()
        if x is None:
            print("Очередь пуста")
        else:
            print("Взяли:", x)
    elif c == "3":
        x = q.peek()
        if x is None:
            print("Очередь пуста")
        else:
            print("Первый элемент:", x)
    elif c == "4":
        print("Размер:", q.size())
    elif c == "5":
        if q.is_empty():
            print("Очередь пуста")
        else:
            print("Очередь не пуста")
    elif c == "6":
        q.clear()
        print("Очередь очищена")
    elif c == "0":
        break
    else:
        print("Нет такого пункта")
