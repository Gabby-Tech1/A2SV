nums = [-2, -3, -3, -5, 5, 3, 3, 2, 3, 4, 2, 5, 1]

min_val = min(nums)
max_val = max(nums)

count_size = max_val - min_val + 1
count = [0] * count_size

for num in nums:
    count[num - min_val] += 1

result = []
for i in range(count_size):
    val = i + min_val
    result.extend([val] * count[i])
    
print(result)
