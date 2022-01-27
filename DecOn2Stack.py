from queue import LifoQueue


class Dec:
    def __init__(self, max_n):
        self.max_size = max_n
        self.left_stack = LifoQueue(maxsize=max_n)
        self.right_stack = LifoQueue(maxsize=max_n)

    def push_back(self, x):
        if self.left_stack.qsize() + self.right_stack.qsize() == self.max_size:
            print("error")
            return
        self.left_stack.put(x)

    def pop_back(self):
        if not self.left_stack.empty():
            return self.left_stack.get()
        else:
            if self.right_stack.empty():
                return "error"
            size = self.right_stack.qsize()
            local = LifoQueue()
            for i in range(int(size / 2)):
                local.put(self.right_stack.get())
        while not self.right_stack.empty():
            self.left_stack.put(self.right_stack.get())
        while not local.empty():
            self.right_stack.put(local.get())
        return self.left_stack.get()

    def push_font(self, x):
        if self.left_stack.qsize() + self.right_stack.qsize() == self.max_size:
            print("error")
            return
        self.right_stack.put(x)

    def pop_font(self):
        if not self.right_stack.empty():
            return self.right_stack.get()
        else:
            if self.left_stack.empty():
                return "error"
            size = self.left_stack.qsize()
            local = LifoQueue()
            for i in range(int(size / 2)):
                local.put(self.left_stack.get())
        while not self.left_stack.empty():
            self.right_stack.put(self.left_stack.get())
        while not local.empty():
            self.left_stack.put(local.get())
        return self.right_stack.get()