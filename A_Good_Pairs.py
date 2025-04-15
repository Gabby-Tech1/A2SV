t = int(input())

def goodPairs(n, a):
    min_index = 0
    max_index = 0

    for i in range(n):
        if a[i] < a[min_index]:
            min_index = i
        if a[i] > a[max_index]:
            max_index = i

    return [min_index + 1, max_index + 1]

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = goodPairs(n, a)
    print(*result)
