from random import randint
from sortedcontainers import SortedDict
import bisect

class Solution:

    def __init__(self, w: List[int]):
        self.len = sum(w)
        self.dic = SortedDict()
        cur_ind = 0
        cur = 0
        for elem in w:
            self.dic[cur_ind] = cur
            cur_ind += elem
            cur += 1


    def pickIndex(self) -> int:
        keys = self.dic.keys()
        index = bisect.bisect_left(keys,randint(0,self.len-1))
        print(index, self.dic, keys[index])
        if self.dic[keys[index]]:
            pass
        return self.dic[keys[index]]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()