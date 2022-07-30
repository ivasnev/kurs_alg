import bisect

nums = [10, 9, 2, 5, 3, 1, 7, 101, 18]

f = []
for i in range(len(nums)):
    if not f or nums[i] > f[-1]:
        f.append(nums[i])
    else:
        pos = bisect.bisect_left(f, nums[i])
        f[pos] = nums[i]
    print(f)

print(len(f))
