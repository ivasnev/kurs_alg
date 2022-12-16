def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    for i in range(1, len(nums)): # from left to right
        res[i] = res[i-1] * nums[i-1]
    tmp = 1
    for i in range(len(nums)-2, -1, -1): # from right to left
        tmp *= nums[i+1]
        res[i] *= tmp
    return res