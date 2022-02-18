#ID 65053539
#По времени сложность удаления О(h), где h глубина древа
#По памяти сложность O(1) ведь мы не создаём доп массивов
#и переменных, зависящих от n, где n кол. элем. в древе


def findMin(root):
    if root.left is None:
        return root
    return findMin(root.left)


def remove(root, key):
    if root is None:
        return None
    if root.value == key:
        if root.left is None and root.right is None:
            return None
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        leftNodeInSubTree = findMin(root.right)
        root.value = leftNodeInSubTree.value
        root.right = remove(root.right,leftNodeInSubTree.value)
        return root
    if key < root.value:
        if root.left is None:
            return root
        root.left = remove(root.left, key)
        return root
    if key > root.value:
        if root.right is None:
            return root
        root.right = remove(root.right,key)
        return root