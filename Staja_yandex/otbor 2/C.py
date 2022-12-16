from platform import node


class TreeNode:
    def __init__(self, value, left=None, right=None, per=None):
        self.per = per
        self.value = value
        self.left = left
        self.right = right

    def lvn(self):
        res = ""
        if self.left is not None:
            res += self.left.lvn()
        res += str(self.value) + " "
        if self.right is not None:
            res += self.right.lvn()
        return res

    def change_per(self, root):
        if self.per is None:
            return root
        grand_per = self.per.per
        if grand_per is not None:
            if self.per is grand_per.left:
                grand_per.left = self
            else:
                grand_per.right = self
        else:
            root = self
        if self is self.per.left:
            self.per.left = self.left
            if self.left is not None:
                self.left.per = self.per
            self.left = self.per
        else:
            self.per.right = self.right
            if self.right is not None:
                self.right.per = self.per
            self.right = self.per
        self.per.per = self
        self.per = grand_per
        return root


def go_to(root, node):
    cur = node
    return cur.change_per(root)


def make_node(cur, n, per=None):
    tmp_node = TreeNode(cur, per=per)
    if cur * 2 <= n:
        tmp_node.left = make_node(cur * 2, n, tmp_node)
    if cur * 2 + 1 <= n:
        tmp_node.right = make_node(cur * 2 + 1, n, tmp_node)
    return tmp_node


def make_bin_tree(n):
    return make_node(1, n)


n, q = map(int, input().split())
array = list(map(int, input().split()))
root = make_bin_tree(n)
dic_node = {}
stack = [root]
while len(stack) != 0:
    tmp = stack.pop()
    if tmp is None:
        continue
    dic_node[tmp.value] = tmp
    stack.append(tmp.left)
    stack.append(tmp.right)
for i in array:
    node = dic_node[i]
    root = go_to(root, node)
print(root.lvn())
