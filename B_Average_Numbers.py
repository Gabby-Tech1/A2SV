n = int(input())
elements = list(map(int, input().split()))

total_sum = sum(elements)

result_indices = []

for i in range(n):
    current = elements[i]
    
    remaining_sum = total_sum - current

    if n > 1:
        average = remaining_sum / (n - 1)
        
        if average == current:
            result_indices.append(i + 1)

print(len(result_indices))
print(*result_indices)