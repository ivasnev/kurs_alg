a = [1, 2, 4, 3, 2, 1]
d = {}
counter = 0
for el in a:
    if not d.get(el):
        d[el] = counter
        counter += 1
b = [0 for _ in range(counter)]
for key in b.keys():
    b[d[key]] = key

######
ages = [6, 6, 0, 23, 14, 45, 55, 72, 23, 6, 2, ...]
assert len(ages) == 8 * 10 ** 9
assert min(ages) == 0 and max(ages) == 200
ages_sorted = ... # ?
all_ages = {}
for el in ages:
    if all_ages.get(el):
        all_ages[el] += 1
    else:
        all_ages[el] = 1
all_ages = list(all_ages.items())
all_ages.sort(key=lambda x: x[0])
ages_sorted = []
for el in all_ages:
    ages_sorted += [el[0] for _ in range(el[1])]

#######
from time import time
from Collections import deque

class RPSLimiter:
    def __init__(self, rps):
        self.fifo = deque()
        self.rps = rps

    def is_request_limited(self) -> bool:
        if len(self.fifo) == 0:
            self.fifo.append(time())
            return False

        el =  self.fifo.popleft()
        if time() - el <= 1:
            self.fifo.appendleft(el)
        if len(self.fifo) >= self.rps:
            return True
        else:
            self.fifo.append(time())
            return False



limiter = RPSLimiter(5)

def foo():
    if limiter.is_request_limited():
        raise
    ...

foo()
foo()
foo()
foo()
foo()
for _ in range(1000):
    foo() # Exception
time.sleep(1)
foo()
foo()
foo()
foo()
foo()