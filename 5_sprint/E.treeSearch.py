def solution(root):
    return isBST(root, -4294967296, 4294967296)


def isBST(root, min, max):
    if root is None:
        return True
    if root.value < min or root.value > max:
        return False
    return isBST(root.left, min, root.value - 1) and isBST(root.right, root.value + 1, max)

