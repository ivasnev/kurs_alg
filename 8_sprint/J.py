class AhoNode:
    def __init__(self):
        self.goto = {}
        self.out = []
        self.fail = None


def aho_create_forest(patterns):
    root = AhoNode()
    for path in patterns:
        node = root
        for symbol in path:
            node = node.goto.setdefault(symbol, AhoNode())
        node.out.append(path)
    return root


def aho_find_all(s, root, callback):
    node = root

    for i in range(len(s)):
        while node is not None and s[i] not in node.goto:
            node = node.fail
        if node is None:
            node = root
            continue
        node = node.goto[s[i]]
        for pattern in node.out:
            callback(i - len(pattern) + 1, pattern)


# def on_occurence(pos, patterns):
#     print("At pos %s found pattern: %s" % (pos, patterns))
#
# patterns = ['a', 'ab', 'abc', 'bc', 'c', 'cba']
# s = "abcba"
# root = aho_create_forest(patterns)
# aho_find_all(s, root, on_occurence)

def main():
    n = int(input())
    CamelCase = []
    for _ in range(n):
        tmp_s = ""
        CamelCase.append([input()])
        for i in CamelCase[-1][0]:
            if i.isupper():
                tmp_s += i
        CamelCase[-1].append(tmp_s)
    m = int(input())
    for _ in range(m):
        pattern = input()
        res = []
        for item in CamelCase:
            a = item[1].find(pattern)
            if 0 == a:
                res.append(item[0])
        res.sort()
        print("\n".join(res))


if __name__ == "__main__":
    main()
