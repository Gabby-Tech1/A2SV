
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    l,r = 0, n - 1
    cost = 0

    while l < r:
        cost += a[r] - a[l]
        l += 1
        r -= 1   

    print(cost)