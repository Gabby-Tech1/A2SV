def subArraySum(nums, k):
    n = len(nums)
    left = 0
    total = 0
    count = 0

    # for right in range(n):
    #     total += nums[right]

    #     while total > k:
    #         total -= nums[left]
    #         left += 1

    #     if total == k:
    #         count += 1

    # return count
    for right in range(1, n+1):
        
        while left < right and total > k:

            total += nums[right-1]

            if total == k:
                count += 1
                break

            if total > k:
                total -= nums[left]
                left += 1

    return count


# Example usage:
nums = [1, 2, 3]
k = 3
result = subArraySum(nums, k)
print(result)