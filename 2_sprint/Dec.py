# id 60676376
# -- ПРИНЦИП РАБОТЫ --
# Я реализовал двунаправленную очередь на статичном списке.
# при инициализации создаётся статичный массив максимального размера очереди
# устанавливается указатель на голову очереди в начале ноль
# при добавление в начало очереди добавляем элемент по индексу головы, индекс головы смещаем(+1)
# при удалении из начала смещаем голову(-1) удаляем элемент по индексу
# при добавление в конец очереди добавляем элемент по индексу, который вычисляем
# по формуле (индекс головы + максимальная длина очереди - текущая длина -1) % максимальная длина очереди
# при удалении с конца удаляем элемент по индексу, который вычисляем
# по формуле (индекс головы + максимальная длина очереди - текущая длина) % максимальная длина очереди
# реализация работает как цикличный буфер в котором расширяется и сужается очередь
# в случае удаления из пустой очереди или заполненой на максимум выводится error
#
#
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Для реализации дек выбран статичный массив,
# при создании массива тратится O(n) на выделение памяти под n элементов, где n максимальнный размер очереди
# Добавление в  стоит O(1), потому что мы лишь обращаемся к ячейке массива по индексу.
# Извлечение из очереди стоит O(1), аналогично добавлению мы лишь обращаемся к ячейке массива по индексу.
# Итого: создание: O(n)
#        функции добавления и удаления: O(1)
#
#
# Оценим основной алгоритм:
# n в данном случае кол. обращений к деку
# Считываем n O(1)
# Считываем максимальную длину очереди O(1)
# Создаём очередь временная сложность О(n), как было сказано ранее.
# В цикле n раз считываем команду и вызываем её от нашего дека обе операции выполняются за O(1)
# ,но это выполняется n раз, следовательно временная сложность О(n)
#
# Общая сложность алгоритма по времени О(n) + О(n) = О(n)
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Статичный массив будет содержать n элементов не зависимо от того содержет ли
# дек элементы,поэтому дек занимает O(n) памяти, где n максимальная длина очереди.
# Поэтому моя реализация дека
# будет потреблять O(n) памяти.

class NumberNotInRangeError(Exception):
    def __init__(self, ):
        pass


class Dec:
    def __init__(self, capacity):
        self.dec_body = [None] * capacity
        self.size_max = capacity
        self.dec_size = 0
        self.head = 0

    def push_back(self, value):
        if self.dec_size + 1 > self.size_max:
            raise NumberNotInRangeError
        index = (self.head + self.size_max - self.dec_size - 1) % self.size_max
        self.dec_body[index] = value
        self.dec_size += 1

    def pop_back(self):
        if self.dec_size == 0:
            raise NumberNotInRangeError
        index = (self.head + self.size_max - self.dec_size) % self.size_max
        self.dec_size -= 1
        return self.dec_body[index]

    def push_front(self, value):
        if self.dec_size + 1 > self.size_max:
            raise NumberNotInRangeError
        self.dec_body[self.head] = value
        self.head = (self.head + 1) % self.size_max
        self.dec_size += 1

    def pop_front(self):
        if self.dec_size == 0:
            raise NumberNotInRangeError
        index = (self.head - 1) % self.size_max
        self.dec_size -= 1
        self.head = index
        return self.dec_body[index]


n = int(input())
MyDec = Dec(int(input()))
for i in range(n):
    inp = input().split()
    try:
        if inp[0] == "pop_front":
            print(MyDec.pop_front())
        if inp[0] == "pop_back":
            print(MyDec.pop_back())
        elif inp[0] == "push_front":
            MyDec.push_front(int(inp[1]))
        elif inp[0] == "push_back":
            MyDec.push_back(int(inp[1]))
    except NumberNotInRangeError:
        print("error")
