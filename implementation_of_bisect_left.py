nums = [1, 2, 3, 4, 5, 6,6,6,6, 7, 8, 9]

def bisect_left(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

res = bisect_left(nums, 6)
print(res)