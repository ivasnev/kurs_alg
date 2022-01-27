#ID 63405967
# Сложность по времени O(nlog n) где n кол. исходных чисел
# На каждом шаге мы снова проделываем O(n)O(n) операций.
# Количество шагов деления (глубина рекурсии) составляет O(log n).
# Поэтому общее число операций будет O(n log n).
# Сложность по памяти O(1) так как мы не создаём доп масивов или переменных зависящих от n
def quicksort(array, start=0, end=None):
    def compare(a, b):
        if a[1] != b[1]:
            return a[1] > b[1]
        elif a[2] != b[2]:
            return a[2] < b[2]
        return a[0] < b[0]

    if end is None:
        end = len(array) - 1
    if start >= end: return
    pivot = array[end]
    left = start
    right = end-1
    while left <= right:
        while left <= right and compare(array[left], pivot):
            left += 1
        while left <= right and compare(pivot, array[right]):
            right -= 1
        if left < right:
            array[left], array[right] = array[right], array[left]
    array[left], array[end] = array[end], array[left]
    quicksort(array, start, left - 1)
    quicksort(array, left + 1, end)


n = int(input())
students = []
for i in range(n):
    students.append(input().split())
    students[i][1] = int(students[i][1])
    students[i][2] = int(students[i][2])
quicksort(students)
for i in students:
    print(i[0])
