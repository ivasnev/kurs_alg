def solution(node):
    while node:
        tmpForSwap = node.next
        node.next = node.prev
        node.prev = tmpForSwap
        if tmpForSwap is None:
            return node
        else:
            node = tmpForSwap