def solution(root):
    if root.left is None and root.right is None:
        return root.value
    else:
        m = root.value
        if root.left is not None:
            m = max(solution(root.left), m)
        if root.right is not None:
            m = max(solution(root.right), m)
        return m