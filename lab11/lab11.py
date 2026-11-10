# Лабораторная работа 11. Работа с деревьями (обход дерева)
# Цейгалов А.В., группа 243-321


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    # вставка в бинарное дерево поиска
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def preorder(root, res):
    # прямой обход: корень, левое, правое
    if root is not None:
        res.append(root.value)
        preorder(root.left, res)
        preorder(root.right, res)


def inorder(root, res):
    # симметричный обход: левое, корень, правое
    if root is not None:
        inorder(root.left, res)
        res.append(root.value)
        inorder(root.right, res)


def postorder(root, res):
    # обратный обход: левое, правое, корень
    if root is not None:
        postorder(root.left, res)
        postorder(root.right, res)
        res.append(root.value)


def level_order(root):
    # обход в ширину, по уровням
    res = []
    if root is None:
        return res
    q = [root]
    while q:
        node = q.pop(0)
        res.append(node.value)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    return res


def print_tree(root, level=0):
    # дерево "на боку": правое поддерево сверху
    if root is not None:
        print_tree(root.right, level + 1)
        print("    " * level + str(root.value))
        print_tree(root.left, level + 1)


values = [int(x) for x in input("Числа для дерева через пробел: ").split()]
root = None
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
