def exclusivePrefixSum(nums):
    arr = []
    sum = 0

    for i in range(len(nums) - 1):
        sum += nums[i]
        arr.append(sum)

    return arr

# Test the function
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 9, 7, 5]
    print(exclusivePrefixSum(nums))