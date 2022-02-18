def deep(root):
    if root is None:
        return 0
    return max(deep(root.left), deep(root.right)) + 1


def solution(root):
    if root is None:
        return True
    lh = deep(root.left)
    rh = deep(root.right)
    if (abs(lh - rh) <= 1) and solution(root.left) is True and solution(root.right) is True:
        return True
    return False