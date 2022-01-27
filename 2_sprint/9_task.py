class MyQueueSized:
    def __init__(self,max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.real_size = 0

    def is_empty(self):
        return self.real_size == 0

    def push(self, x):
        if self.real_size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.real_size += 1
        else:
            print("error")

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.real_size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.queue[self.head]

    def size(self):
        return self.real_size

n = int(input())
max = int(input())
MyQueue = MyQueueSized(max)
for i in range(n):
    inp = input().split()
    if inp[0] == "peek":
        print(MyQueue.peek())
    elif inp[0] == "push":
        MyQueue.push(int(inp[1]))
    elif inp[0] == "pop":
        print(MyQueue.pop())
    elif inp[0] == "size":
        print(MyQueue.size())