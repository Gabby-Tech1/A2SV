t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    frequency = {}
    result = -1
    
    # Count all frequencies first
    for num in a:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Find the largest number that appears at least 3 times
    for num in a:
        if frequency[num] >= 3:
            result = max(result, num)  # Keep the largest number
    
    print(result)