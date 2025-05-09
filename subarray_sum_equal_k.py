def subArraySum(nums, k):
    """
    Given an array of integers nums and an integer k, return the number of continuous subarrays whose sum equals to k.
    """
    count = 0
    sum_map = {0: 1}  # Initialize with sum 0 having one count
    current_sum = 0

    for num in nums:
        current_sum += num
        if current_sum - k in sum_map:
            count += sum_map[current_sum - k]
        sum_map[current_sum] = sum_map.get(current_sum, 0) + 1

    return count