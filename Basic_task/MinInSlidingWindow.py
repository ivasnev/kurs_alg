from collections import deque


def mininslidingwindow(A, k):
    A = [float("inf")]*(k-1) + A
    mins = []
    deq = deque()
    for i in range(len(A)):
        if (len(deq) > 0) and (deq[0] <= i - k):
            deq.popleft()
        while len(deq) > 0 and A[deq[-1]] >= A[i]:
            deq.pop()
        deq.append(i)
        if i >= k - 1:
            mins.append(A[deq[0]])

    return mins[:len(A)-k+1]


n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
res = mininslidingwindow(arr, k)
print(*res)


def mininslidingwindow2(A, k):
    _sum = 0
    res = [0] * len(A)
    mins = []
    deq = deque()
    for i in range(len(A)):
        if (len(deq) > 0) and (deq[0] <= i - k):
            deq.popleft()
        while len(deq) > 0 and A[deq[-1]] >= A[i]:
            deq.pop()
        deq.append(i)

        if i >= k - 1:
            _sum += A[deq[0]]
            mins.append(A[deq[0]])
            res[deq[0]-k+1] += 1

    return res[:len(A)-k+1], _sum


n, k = list(map(int, input().split()))
arr = [float("inf")]*(k-1) + list(map(int, input().split()))
res, s = mininslidingwindow2(arr, k)
print(s)
print(*res)