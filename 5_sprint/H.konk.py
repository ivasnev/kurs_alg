def solution(root) -> int:
    return sum(rec(root, ""))


def rec(root,s) -> list:
    arr = []
    s += str(root.value)
    if root.left is not None:
        arr += rec(root.left, s)
    if root.right is not None:
        arr += rec(root.right, s)
    if root.left is None and root.right is None:
        return [int(s)]
    else:
        return arr