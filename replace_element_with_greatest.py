arr = [17,18,5,4,6,1]

new_arr = []

for i in range(len(arr)):
    if i == len(arr) - 1:
        new_arr.append(-1)
    else:
        max_val = max(arr[i+1:])
        new_arr.append(max_val)

print(new_arr)