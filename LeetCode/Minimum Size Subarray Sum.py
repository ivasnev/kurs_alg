def minSubArrayLen(s, nums):

    left = right = mini_length = 0
    curr_sum = nums[0] if nums else 0

    while right < len(nums):

        # Adding elements using `right` pointer
        while curr_sum < s:
            right += 1
            if right == len(nums):
                return mini_length
            curr_sum += nums[right]

        # Updating our tracks
        if (right - left + 1) < mini_length or not mini_length:
            mini_length = right - left + 1

        # Get rid of the old elements using `left` pointer
        curr_sum -= nums[left]
        left += 1

    return mini_length

target = 7
nums = [2,3,1,2,4,3]
print(nums)
print(minSubArrayLen(target,nums))
