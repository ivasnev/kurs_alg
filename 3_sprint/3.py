def checker(first, second):
    start = -1
    for i in first:
        start = second.find(i, start + 1)
        if start == -1:
            return False
    return True


first, second = input(), input()
print(checker(first,second))
