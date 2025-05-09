n = int(input())

arr = list(map(int, input().split()))
arr.sort(reverse=True) 

total_sum = sum(arr)

m = int(input())
queries = list(map(int, input().split()))

for x in queries:
    discounted_sum = total_sum - arr[x-1]
    print(discounted_sum)