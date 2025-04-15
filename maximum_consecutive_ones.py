def findMaxConsecutiveOnes(nums):
    """
    Find the maximum number of consecutive 1s in a binary array.

    :param nums: List[int] - The input binary array.
    :return: int - The maximum number of consecutive 1s.
    """
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count