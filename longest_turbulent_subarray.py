def maxTurbulenceSize(arr):
    
    n = len(arr)
    if n < 2:
        return n

    max_length = 1
    current_length = 1
    direction = 0

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            if direction <= 0:
                current_length += 1
                direction = 1
            else:
                current_length = 2
        elif arr[i] < arr[i - 1]:
            if direction >= 0:
                current_length += 1
                direction = -1
            else:
                current_length = 2
        else:
            current_length = 1
            direction = 0

        max_length = max(max_length, current_length)

    return max_length