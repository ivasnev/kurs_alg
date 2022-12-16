def findMaxLength(self, nums: List[int]) -> int:
    hm = {0: -1}
    count = 0
    max_len = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1
        if hm.get(count) is None:
            hm[count] = i
        else:
            max_len = max(max_len, i - hm[count])
    print(hm)
    return max_len