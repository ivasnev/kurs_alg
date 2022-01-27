class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        if self.size() == 0:
            self.items.append([item, item])
        elif self.items[-1][1] < item:
            self.items.append([item, item])
        else:
            self.items.append([item, self.items[-1][1]])

    def pop(self):
        if self.size() == 0:
            print("error")
        else:
            self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if self.size() == 0:
            print("None")
        else:
            print(self.items[-1][1])


n = int(input())
stack = StackMax()
for i in range(n):
    inp = input().split()
    if inp[0] == "get_max":
        stack.get_max()
    elif inp[0] == "push":
        stack.push(int(inp[1]))
    elif inp[0] == "pop":
        stack.pop()
    else:
        pass
