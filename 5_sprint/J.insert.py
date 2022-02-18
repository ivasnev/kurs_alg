from node import Node

def insert(root, key):
    if key >= root.value:
        if root.right is None:
            root.right = Node(value=key)
        else:
            insert(root.right, key)
    else:
        if root.left is None:
            root.left = Node(value=key)
        else:
            insert(root.left, key)
    return root