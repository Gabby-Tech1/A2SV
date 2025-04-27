def maximumSubArray(nums):
    """
    Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

    :param nums: List[int] - Input array of integers
    :return: int - The sum of the contiguous subarray with the largest sum
    """
    if not nums:
        return 0

    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum