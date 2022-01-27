# ID 63783637
# Сложность по времени каждой операции с таблицей всреднем O(1),
# в худшем случае O(n) где n размер массива создаваемого при инициализации
# Сложность по памяти каждой операции с таблицей O(1) так как мы лист ноду
# или переменных зависящих от n при работе


class Node:
    def __init__(self, key=None, data=None, next=None):
        self.key = key
        self.data = data
        self.next = next


class HashTbListNode:
    def __init__(self):
        self.size = 200003
        self.table = [Node() for i in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def put(self, key, data):
        hash_value = self.hash_function(key)
        if self.table[hash_value].key is None or self.table[hash_value].key == key:
            self.table[hash_value].key = key
            self.table[hash_value].data = data
        else:
            p = self.table[hash_value]
            temp = Node(key, data, p)
            self.table[hash_value] = temp

    def get(self, key):
        hash_value = self.hash_function(key)
        if self.table[hash_value].key == key:
            return self.table[hash_value].data
        else:
            p = self.table[hash_value]
            while p is not None and p.key != key:
                p = p.next
            if p is not None and p.key == key:
                return p.data
        return False

    def delete(self, key):
        if not self.get(key):
            return 'None'
        hash_value = self.hash_function(key)
        if self.table[hash_value].key == key:
            tmp = self.table[hash_value]
            if tmp.next is None:
                self.table[hash_value] = Node()
            else:
                self.table[hash_value] = tmp.next
            return tmp.data
        else:
            p = self.table[hash_value]
            pre = None
            while p is not None and p.key != key:
                pre = p
                p = p.next
            if p is None:
                return 'None'
            else:
                pre.next = p.next
                return p.data


n = int(input())
tb = HashTbListNode()
for i in range(n):
    array = input().split()
    if array[0] == 'put':
        tb.put(int(array[1]), array[2])
    elif array[0] == 'get':
        a = tb.get(int(array[1]))
        if a == False:
            print("None")
        else:
            print(a)
    elif array[0] == 'delete':
        print(tb.delete(int(array[1])))
