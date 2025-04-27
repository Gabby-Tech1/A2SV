n, s = list(map(int, input().split()))
elements = list(map(int, input().split()))

left = 0
max_length = 0
for right in range(n):
    s -= elements[right]

    while s < 0:
        s += elements[left]
        left += 1

    max_length = max(max_length, right - left + 1)

print(max_length)