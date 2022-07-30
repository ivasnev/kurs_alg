def subsetsWithDup(self, nums):
    n = len(nums)
    nums.sort()
    res = set()
    for i in range(2 ** n):
        j, sub = 0, []
        while i:
            if i & 1:
                sub.append(nums[j])
            j += 1
            i >>= 1
        res.add(tuple(sub))
    return res