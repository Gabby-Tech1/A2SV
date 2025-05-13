n = int(input())
a = list(map(int, input().split()))

coins_needed = 0
negative_count = 0
zero_count = 0

for num in a:
    if num > 0:
        coins_needed += num - 1
    elif num < 0:
        coins_needed += abs(num) - 1
        negative_count += 1
    else:
        coins_needed += 1
        zero_count += 1

if negative_count % 2 == 1 and zero_count == 0:
    coins_needed += 2

print(coins_needed)