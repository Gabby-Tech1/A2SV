arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10

left = 0
right = len(arr)

while left <= right:
    mid = (left + right) // 2
    print("Left:", left, "Right:", right, "Mid:", mid)

    if arr[mid] < target:
        left = mid + 1
    elif arr[mid] > target:
        right = mid - 1
    else:
        print("Found at index", mid)
        print(True)
        break