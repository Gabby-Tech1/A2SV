n = int(input())
    
prime_factors_count = [0] * (n + 1)

for i in range(2, n + 1):
    if prime_factors_count[i] == 0:
        prime_factors_count[i] = 1
        
        for j in range(i * 2, n + 1, i):
            prime_factors_count[j] += 1

count = 0
for i in range(2, n + 1):
    if prime_factors_count[i] == 2:
        count += 1
        
print(count)

