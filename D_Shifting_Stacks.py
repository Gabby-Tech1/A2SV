t = int(input())

for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    extra = 0
    possible = True

    for i in range(n):
        required = i

        if h[i] >= required:
            extra += h[i] - required
        else:
            if extra >= required - h[i]:
                extra -= required - h[i]
            else:
                possible = False
                break

    if possible:
        print("YES")
    else:
        print("NO")