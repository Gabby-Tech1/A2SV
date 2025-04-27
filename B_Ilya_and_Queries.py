s = input().strip()

n = len(s)
prefix_sum = [0] * (n + 1) 
for i in range(1, n):
    prefix_sum[i+1] += prefix_sum[i]
    if s[i] == s[i-1]:
        prefix_sum[i+1] += 1
    else:
        prefix_sum[i+1] += 0

m = int(input()) 

for _ in range(m):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    
    print(prefix_sum[r+1] - prefix_sum[l+1])