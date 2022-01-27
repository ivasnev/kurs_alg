class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

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
            print(max(self.items))


def is_correct_bracket_seq(str):
    stack = StackMax()
    for i in range(len(str)):
        if str[i] == "[" or str[i] == "(" or str[i] == "{":
            stack.push(str[i])
        else:
            if stack.size() == 0:
                return False
            if stack.peek() == "[" and str[i] == "]":
                stack.pop()
            elif stack.peek() == "{" and str[i] == "}":
                stack.pop()
            elif stack.peek() == "(" and str[i] == ")":
                stack.pop()
            else:
                return False
    if stack.size() == 0:
        return True
    else:
        return False


inp = input()
print(is_correct_bracket_seq(inp))
