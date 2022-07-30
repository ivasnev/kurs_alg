def subsetsWithDup(self, nums):
    res = {()}
    n = len(nums)
    nums.sort()

    def helper(idx):
        if idx == n:
            return
        helper(idx + 1)
        for sub in set(res):
            sub = list(sub)
            sub.append(nums[idx])
            res.add(tuple(sub))

    helper(0)
    return res
