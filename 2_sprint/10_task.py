class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class MyQueueOnLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self):
        if self.size == 0:
            print("error")
            return
        print(self.head.value)
        self.head = self.head.next_item
        self.size -= 1

    def put(self, x):
        new_node = Node(x)
        if self.size == 0:
            self.head = new_node
        else:
            self.tail.next_item = new_node
        self.tail = new_node
        self.size += 1

    def getsize(self):
        return self.size


n = int(input())
MyQueue = MyQueueOnLinkedList()
for i in range(n):
    inp = input().split()
    if inp[0] == "get":
        MyQueue.get()
    elif inp[0] == "put":
        MyQueue.put(int(inp[1]))
    elif inp[0] == "size":
        print(MyQueue.getsize())
