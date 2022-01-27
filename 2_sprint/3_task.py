def solution(node, idx):
    counter = 0
    if idx == 0:
        return node.next_item;
    head = node;
    while node:
        if counter + 1 == idx:
            node.next_item = node.next_item.next_item
            return head
        node = node.next_item
        counter += 1
