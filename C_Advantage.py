# def Advantage(n, s):
#     for i in range(n):
#         strongest = max(s[i:])

#         result = s[i] - strongest
#         return [result]



# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = list(map(int, input().split()))
#     result = Advantage(n, s)
#     print(*result)

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    max_val = max(s)
    max_count = s.count(max_val)
    second_max = max([x for x in s if x != max_val], default=max_val)

    results = []
    for i in range(n):
        if s[i] == max_val and max_count == 1:
            results.append(s[i] - second_max)
        else:
            results.append(s[i] - max_val)

    print(*results)



        