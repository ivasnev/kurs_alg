#ID 63399494
# Сложность по времени O(log n) где n кол. исходных чисел, так как это бинарный поиск и прикаждой
# итерации мы будем сокращать массив в котором ищем в двое
# Сложность по памяти O(1) так как мы не создаём доп масивов или переменных зависящих от n

def broken_search(nums, k) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == k:
            return mid
        if nums[left] <= nums[mid]:
            if k < nums[mid] and k >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if k > nums[mid] and k <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    else:
        return(-1)
