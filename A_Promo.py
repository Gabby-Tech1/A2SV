n, queries = list(map(int, input().split()))
prices = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + prices[i - 1]
print(prefix_sum)

for _ in range(queries):
    x, y = list(map(int, input().split()))
    # print(prefix_sum[y] - prefix_sum[x - 1])
    max_cheap = max(prices[x], prefix_sum[y] - prefix_sum[x - 1])
    print(max_cheap)
