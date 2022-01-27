def solution(node, elem):
    counter = 0
    while node:
        if node.value == elem:
            return counter
        node = node.next_item
        counter += 1
    return -1
