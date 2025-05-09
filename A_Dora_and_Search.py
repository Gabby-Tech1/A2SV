t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    l,r = 0, n-1
    max_num, min_num = 1, n
    found = False

    while l <= r:
        if a[l] == max_num:
            l += 1
            max_num += 1
        elif a[r] == max_num:
            r -= 1
            max_num += 1
        elif a[l] == min_num:
            l += 1
            min_num -= 1
        elif a[r] == min_num:
            r -= 1
            min_num -= 1
        else:
            found = True
            print(l+1, r+1)
            break

    if not found:
        print(-1)