t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if k % 2 == 0:
        if n % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")