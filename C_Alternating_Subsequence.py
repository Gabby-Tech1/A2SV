t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total = 0
    i = 0

    while i < n:
        sign = a[i] > 0
        max_value = a[i]
        j = i

        while j < n and (a[j] > 0) == sign:
            max_value = max(max_value, a[j])
            j += 1

        i = j
        total += max_value
        
    print(total)