arr = [0,3,2,1]

n = len(arr)
def validMountainArray(arr):
    if len(arr) < 3:
        return False

    i = 0
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    if i == 0 or i == n - 1:
        return False

    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1

print(validMountainArray(arr)) 