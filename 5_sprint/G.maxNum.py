def solution(root) -> int:
    a = 0
    b = 0
    if root is None:
        return 0
    if root.left is not None:
        a = solution(root.left)
    if root.right is not None:
        b = solution(root.right)
    return max(a, b) + root.value