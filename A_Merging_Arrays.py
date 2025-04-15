n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = []
i, j = 0, 0

while i < n and j < m:
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

if i >= n:
    c.extend(b[j:])
else:
    c.extend(a[i:])

print(*c)

