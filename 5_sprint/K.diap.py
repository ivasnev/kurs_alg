def find_left(node, l, r):
    if node.value < l:
        if node.right is not None:
            print_range(node.right, l, r)
        else:
            return
    elif node.value >= l:
        if node.left is not None:
            print_range(node.left, l, r)
        else:
            return node.value

def print_range(node, l, r):
    tmp = find_left(node,l,r)
    if tmp is not None:
        pass
