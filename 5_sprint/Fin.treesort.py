#ID 65128374
# Сложность по дополнительной памяти O(1), так как мы не выделяем доп памяти
# а работаем с тем же массивом
# Сложность по времени зависит от просейки, однократная просейка обходится в O(log n).
# где n кол. элементов.
# Для построения кучи мы дела n просейк этот этап занимает O(n log n)
# Во второй части мы выносим n макс. и просейваем оставшуюся не сорт часть так же за O(log n)
# Итого O(n log n) + O(n log n) = O(n log n)


def heapsort(array):
    for start in range(int((len(array) - 2) / 2), -1, -1):
        sift(array, start, len(array) - 1) 
    for end in range(len(array) - 1, 0, -1): 
        array[end], array[0] = array[0], array[end]
        sift(array, 0, end - 1)
    return array


def sift(array, start, end):
    def compare(a, b):
        if a[1] != b[1]:
            return a[1] > b[1]
        elif a[2] != b[2]:
            return a[2] < b[2]
        return a[0] < b[0]

    root = start
    while True:
        child = root * 2 + 1  
        if child > end: 
            break
        if child + 1 <= end and compare(array[child], array[child + 1]):
            child += 1
        if compare(array[root], array[child]):
            array[root], array[child] = array[child], array[root]
            root = child
        else:
            break


n = int(input())
students = []
for i in range(n):
    students.append(input().split())
    students[i][1] = int(students[i][1])
    students[i][2] = int(students[i][2])
heapsort(students)
for i in students:
    print(i[0])