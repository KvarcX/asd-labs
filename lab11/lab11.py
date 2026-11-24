# Лабораторная работа 11. Работа с деревьями (обход дерева)
# Цейгалов А.В., группа 243-321


class Node:
    def __init__(self, value):
        # Храним число в узле.
        self.value = value
        # У нового узла пока нет детей.
        self.left = None
        self.right = None


def insert(root, value):
    # пустое место - создаём узел.
    if root is None:
        return Node(value)
    # Число меньше текущего - вставляем в левую ветку.
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        # Больше или равно - вставляем в правую ветку.
        root.right = insert(root.right, value)
    # Возвращаем узел вместе с обновлённой веткой.
    return root


def preorder(root, res):
    # Пустую ветку пропускаем.
    if root is not None:
        # Сначала записываем число из текущего узла.
        res.append(root.value)
        # Потом обходим левую ветку.
        preorder(root.left, res)
        # Затем правую.
        preorder(root.right, res)


def inorder(root, res):
    # Пустую ветку пропускаем.
    if root is not None:
        # Сначала обходим левую ветку.
        inorder(root.left, res)
        # Потом записываем число из текущего узла.
        res.append(root.value)
        # Затем обходим правую ветку.
        inorder(root.right, res)


def postorder(root, res):
    # Пустую ветку пропускаем.
    if root is not None:
        # Сначала обходим левую ветку.
        postorder(root.left, res)
        # Потом правую.
        postorder(root.right, res)
        # Текущий узел записываем после обеих веток.
        res.append(root.value)


def level_order(root):
    # Сюда записываем числа в порядке обхода.
    res = []
    # Если дерево пустое, обходить нечего.
    if root is None:
        return res
    # Начинаем очередь с корня.
    q = [root]
    # Обходим дерево, пока в очереди есть узлы.
    while q:
        # Забираем первый узел из очереди.
        node = q.pop(0)
        # Записываем его число.
        res.append(node.value)
        # Если есть левый ребёнок, ставим его в конец очереди.
        if node.left is not None:
            q.append(node.left)
        # Правого добавляем туда же, после левого.
        if node.right is not None:
            q.append(node.right)
    return res


def print_tree(root, level=0):
    # Пустую ветку не печатаем.
    if root is not None:
        # Сначала печатаем правую ветку, чтобы она была сверху.
        print_tree(root.right, level + 1)
        # Чем глубже узел, тем больше отступ.
        print("    " * level + str(root.value))
        # Левую ветку печатаем снизу.
        print_tree(root.left, level + 1)


values = [int(x) for x in input("Числа для дерева через пробел: ").split()]
root = None
# Добавляем числа по одному, начиная с пустого дерева.
for v in values:
    root = insert(root, v)

print("\nДерево:")
print_tree(root)

res = []
preorder(root, res)
print("\nПрямой обход:", res)
res = []
inorder(root, res)
print("Симметричный обход:", res)
res = []
postorder(root, res)
print("Обратный обход:", res)
print("Обход в ширину:", level_order(root))
